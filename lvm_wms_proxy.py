#!/usr/bin/env python3
"""
LVM WMS Coordinate Translation Proxy

This proxy server translates WGS84 coordinates to Latvian LKS-92 (EPSG:3059)
coordinate system for LVM GeoServer WMS services.

Usage:
    python lvm_proxy.py

Then access: http://localhost:8080/wms?...

Requirements:
    pip install flask requests pyproj
"""

from flask import Flask, request, Response, jsonify
import requests
from pyproj import Transformer
import logging
from urllib.parse import urlencode, parse_qs
import re

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# LVM GeoServer base URL
LVM_BASE_URL = "https://lvmgeoserver.lvm.lv/geoserver/ows"

# Create coordinate transformers
# WGS84 (EPSG:4326) to Latvian LKS-92 (EPSG:3059)
wgs84_to_lks92 = Transformer.from_crs("EPSG:4326", "EPSG:3059", always_xy=True)
# Web Mercator (EPSG:3857) to Latvian LKS-92 (EPSG:3059)  
webmercator_to_lks92 = Transformer.from_crs("EPSG:3857", "EPSG:3059", always_xy=True)

def transform_bbox(bbox_str, source_crs, wms_version="1.3.0"):
    """
    Transform bounding box coordinates from source CRS to EPSG:3059
    
    Args:
        bbox_str: Comma-separated bbox string 
        source_crs: Source coordinate system ("EPSG:4326", "CRS:84", "EPSG:3857")
        wms_version: WMS version to determine axis order
    
    Returns:
        Transformed bbox string in EPSG:3059
    """
    try:
        coords = [float(x.strip()) for x in bbox_str.split(',')]
        if len(coords) != 4:
            raise ValueError("BBOX must have 4 coordinates")
        
        logger.info(f"Raw input coordinates: {coords}")
        logger.info(f"Source CRS: {source_crs}, WMS Version: {wms_version}")
        
        # Always treat as x,y,x,y order for simplicity
        minx, miny, maxx, maxy = coords
        logger.info(f"Input BBOX: minx={minx}, miny={miny}, maxx={maxx}, maxy={maxy}")
        
        # Test transformation with known coordinates
        # Riga center: approximately 24.1, 56.95 in WGS84 should be around 500000, 300000 in LKS-92
        if source_crs.upper() == "EPSG:3857":
            # Test point transformation for debugging
            test_transformer = Transformer.from_crs("EPSG:3857", "EPSG:4326", always_xy=True)
            test_lon, test_lat = test_transformer.transform(minx, miny)
            logger.info(f"Test: Web Mercator ({minx}, {miny}) -> WGS84 ({test_lon}, {test_lat})")
        
        # Choose appropriate transformer
        if source_crs.upper() in ["EPSG:4326", "CRS:84"]:
            transformer = wgs84_to_lks92
        elif source_crs.upper() == "EPSG:3857":
            transformer = webmercator_to_lks92
        else:
            # If it's already EPSG:3059 or another system, pass through
            logger.warning(f"Unsupported source CRS: {source_crs}, passing through")
            return bbox_str
        
        # Transform all four corners to handle potential coordinate system flipping
        sw_x, sw_y = transformer.transform(minx, miny)  # Southwest (bottom-left)
        ne_x, ne_y = transformer.transform(maxx, maxy)  # Northeast (top-right)
        se_x, se_y = transformer.transform(maxx, miny)  # Southeast (bottom-right)
        nw_x, nw_y = transformer.transform(minx, maxy)  # Northwest (top-left)
        
        logger.info(f"Corner transformations:")
        logger.info(f"  SW ({minx}, {miny}) -> ({sw_x}, {sw_y})")
        logger.info(f"  NE ({maxx}, {maxy}) -> ({ne_x}, {ne_y})")
        logger.info(f"  SE ({maxx}, {miny}) -> ({se_x}, {se_y})")
        logger.info(f"  NW ({minx}, {maxy}) -> ({nw_x}, {nw_y})")
        
        # Find the actual min/max values from all transformed corners
        all_x = [sw_x, ne_x, se_x, nw_x]
        all_y = [sw_y, ne_y, se_y, nw_y]
        
        final_minx = min(all_x)
        final_miny = min(all_y)
        final_maxx = max(all_x)
        final_maxy = max(all_y)
        
        # Check if coordinates are reasonable for Latvia
        # Latvia is roughly between X: 300000-700000, Y: 50000-400000 in LKS-92
        if final_minx < 200000 or final_maxx > 800000:
            logger.error(f"X coordinates outside Latvia range: {final_minx}, {final_maxx}")
        if final_miny < 0 or final_maxy > 500000:
            logger.error(f"Y coordinates outside Latvia range: {final_miny}, {final_maxy}")
        
        logger.info(f"Final BBOX: minx={final_minx}, miny={final_miny}, maxx={final_maxx}, maxy={final_maxy}")
        
        # Return transformed coordinates in target CRS format
        transformed_bbox = f"{final_minx},{final_miny},{final_maxx},{final_maxy}"
        logger.info(f"Transformed BBOX from {source_crs}: {bbox_str} -> EPSG:3059: {transformed_bbox}")
        
        return transformed_bbox
        
    except Exception as e:
        logger.error(f"Error transforming BBOX {bbox_str}: {e}")
        return bbox_str  # Return original on error

def get_layer_native_crs(layer_name):
    """
    Determine the native CRS for a layer based on LVM capabilities.
    Most LVM layers use EPSG:3059 as their native CRS.
    """
    # Special cases for Baltic region layers
    if "baltic:DTW" in layer_name and "_EE" in layer_name:
        return "EPSG:3301"  # Estonian coordinate system
    elif "baltic:DTW" in layer_name and "_LT" in layer_name:
        return "EPSG:3346"  # Lithuanian coordinate system
    else:
        return "EPSG:3059"  # Default Latvian LKS-92

@app.route('/wms', methods=['GET'])
def wms_proxy():
    """
    WMS proxy endpoint that translates coordinates and forwards requests to LVM GeoServer
    """
    try:
        # Get all query parameters
        params = dict(request.args)
        
        # Log incoming request
        logger.info(f"Incoming WMS request: {request.url}")
        
        # Check if this is a WMS request (case-insensitive)
        service = params.get('SERVICE') or params.get('service') or ''
        if service.upper() != 'WMS':
            return jsonify({"error": "Only WMS service is supported"}), 400
        
        # Get the request type (case-insensitive)
        wms_request = (params.get('REQUEST') or params.get('request') or '').upper()
        
        if wms_request == 'GETCAPABILITIES':
            # For GetCapabilities, just forward the request
            response = requests.get(LVM_BASE_URL, params=params)
            return Response(response.content, 
                          mimetype=response.headers.get('content-type', 'text/xml'),
                          headers={'Access-Control-Allow-Origin': '*'})
        
        elif wms_request == 'GETMAP':
            # For GetMap, transform coordinates if needed
            
            # Get source CRS from request (case-insensitive)
            source_crs = params.get('CRS') or params.get('crs') or params.get('SRS') or params.get('srs') or 'EPSG:4326'
            
            # Get layer name to determine target CRS (case-insensitive)
            layers = params.get('LAYERS') or params.get('layers') or ''
            target_crs = get_layer_native_crs(layers)
            
            # Get WMS version for proper axis order handling
            wms_version = params.get('VERSION') or params.get('version') or '1.3.0'
            
            # Transform BBOX if needed (case-insensitive)
            bbox_key = 'BBOX' if 'BBOX' in params else 'bbox' if 'bbox' in params else None
            if bbox_key and source_crs.upper() in ['EPSG:4326', 'CRS:84', 'EPSG:3857']:
                original_bbox = params[bbox_key]
                logger.info(f"Original BBOX: {original_bbox}, Source CRS: {source_crs}, WMS Version: {wms_version}")
                
                # TEMPORARY: Skip transformation to test if the issue is with coordinate transformation
                logger.info("SKIPPING COORDINATE TRANSFORMATION FOR DEBUGGING")
                # transformed_bbox = transform_bbox(original_bbox, source_crs, wms_version)
                # params[bbox_key] = transformed_bbox
                
                # Don't update CRS - keep original
                # if 'CRS' in params:
                #     params['CRS'] = target_crs
                # elif 'crs' in params:
                #     params['crs'] = target_crs
                # if 'SRS' in params:
                #     params['SRS'] = target_crs
                # elif 'srs' in params:
                #     params['srs'] = target_crs
                
                logger.info(f"Keeping original CRS: {source_crs}")
            
            # Forward request to LVM GeoServer
            response = requests.get(LVM_BASE_URL, params=params, timeout=30)
            
            # Return response with CORS headers
            return Response(response.content,
                          status=response.status_code,
                          mimetype=response.headers.get('content-type', 'image/png'),
                          headers={'Access-Control-Allow-Origin': '*'})
        
        else:
            # Forward other WMS requests as-is
            response = requests.get(LVM_BASE_URL, params=params)
            return Response(response.content,
                          status=response.status_code,
                          mimetype=response.headers.get('content-type', 'text/xml'),
                          headers={'Access-Control-Allow-Origin': '*'})
            
    except requests.exceptions.RequestException as e:
        logger.error(f"Request error: {e}")
        return jsonify({"error": f"Request failed: {str(e)}"}), 502
    except Exception as e:
        logger.error(f"Proxy error: {e}")
        return jsonify({"error": f"Proxy error: {str(e)}"}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "service": "LVM WMS Proxy"})

@app.route('/transform', methods=['GET'])
def coordinate_transform():
    """
    Standalone coordinate transformation endpoint for testing
    
    Usage: /transform?x=24.1&y=56.9&from=EPSG:4326&to=EPSG:3059
    """
    try:
        x = float(request.args.get('x', 0))
        y = float(request.args.get('y', 0))
        from_crs = request.args.get('from', 'EPSG:4326')
        to_crs = request.args.get('to', 'EPSG:3059')
        
        transformer = Transformer.from_crs(from_crs, to_crs, always_xy=True)
        x_transformed, y_transformed = transformer.transform(x, y)
        
        return jsonify({
            "input": {"x": x, "y": y, "crs": from_crs},
            "output": {"x": x_transformed, "y": y_transformed, "crs": to_crs}
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/', methods=['GET'])
def index():
    """
    Simple documentation page
    """
    return """
    <html>
    <head><title>LVM WMS Proxy</title></head>
    <body>
        <h1>LVM WMS Coordinate Translation Proxy</h1>
        <p>This proxy translates coordinates from WGS84/Web Mercator to Latvian LKS-92 for LVM GeoServer.</p>
        
        <h2>Endpoints:</h2>
        <ul>
            <li><code>/wms</code> - WMS proxy endpoint</li>
            <li><code>/health</code> - Health check</li>
            <li><code>/transform</code> - Coordinate transformation testing</li>
        </ul>
        
        <h2>Example Usage:</h2>
        <h3>WMS GetMap (using WGS84 coordinates):</h3>
        <pre>
/wms?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0
&LAYERS=public:Orto_LKS
&CRS=EPSG:4326
&BBOX=20.5,55.5,28.5,58.5
&WIDTH=512&HEIGHT=512
&FORMAT=image/png
        </pre>
        
        <h3>Coordinate Transformation Test:</h3>
        <pre>/transform?x=24.1&y=56.9&from=EPSG:4326&to=EPSG:3059</pre>
        
        <h2>Supported Input Coordinate Systems:</h2>
        <ul>
            <li>EPSG:4326 (WGS84)</li>
            <li>CRS:84 (WGS84)</li>
            <li>EPSG:3857 (Web Mercator)</li>
        </ul>
        
        <p>The proxy automatically translates to the appropriate Latvian coordinate system (usually EPSG:3059).</p>
    </body>
    </html>
    """

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    print("Starting LVM WMS Coordinate Translation Proxy...")
    print("Access the proxy at: http://localhost:8118")
    print("WMS endpoint: http://localhost:8118/wms")
    print("Health check: http://localhost:8118/health")
    print("Coordinate test: http://localhost:8118/transform?x=24.1&y=56.9&from=EPSG:4326&to=EPSG:3059")
    
    app.run(host='0.0.0.0', port=8118, debug=True)
