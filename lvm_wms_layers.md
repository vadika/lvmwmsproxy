# LVM GeoServer WMS Layers

## Address and Road Network
- **Adreses ar ielu un autoceļu tīklu**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:Adreses_celu_tikls&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Ceļi (Roads)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:arisroad&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Ielas (Streets)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:arisstreet&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Ēku adreses (Building addresses)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:arisbuilding&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

## Terrain and Relief
- **Reljefa modelis ar horizontālēm (DTM with contours)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:DTM_contours&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Digitāls reljefa modelis, 1. cikls**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:ZemeLKS&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Digitāls reljefa modelis, 2. cikls**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:ZemeLKS2&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Horizontāles ar augstumu vērtībām**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:Contours&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Horizontāles**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:Contours_nolabels&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

## Cadastral Data
- **Kadastra karte**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:Kadastra_karte&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Zemes vienību daļas**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:kkparcelpart&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Zemes vienības**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:kkparcel&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Robežpunkti**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:kkparcelborderpoint&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Kadastra grupas**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:kkcadastralgroup&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Administratīvās robežas**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:region&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Ēkas**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:kkbuilding&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Inženierbūves**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:kkengineeringstructurepoly&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

## LVM Forest Infrastructure
- **Meža infrastruktūra (LVM)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:LVM_Meza_infrastruktura&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Meža ceļi (LVM)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:road&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Attīstāmie meža ceļi (LVM)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:planedroads&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Tilti un lielās caurtekas (LVM)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:bridge&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Caurtekas (LVM)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:culvert&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Grāvji (LVM)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:ditches&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Meliorācijas sistēmas (LVM)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:drainagesystem&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

## LVM Forestry Data
- **Mežkopības dati (LVM)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:LVM_Mezkopibas_dati&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Meža stigas (LVM)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:firebreak&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Mineralizētās joslas (LVM)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:fireline&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Ugunsgrēku vietas, aktuālais gads (LVM)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:vmdfirepoints_actualYear&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Ugunsgrēku teritorijas, aktuālais gads (LVM)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:vmdfirepolygons_actualYear&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Bojājumu teritorijas (LVM)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:damage&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Ūdens ņemšanas vietas (LVM)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:watersupplypoint&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

## LVM Administrative Divisions
- **LVM teritoriālais dalījums**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:LVM_Teritorialais_dalijums&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **LVM iecirkņi**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:lvmdistrict&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **LVM reģioni**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:lvmforestry&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

## Tourism Infrastructure (LVM)
- **Tūrisma vietu infrastruktūra (LVM)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:LVM_Turisma_infrastruktura&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Dabas takas (LVM)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:naturetrail&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Velotakas (LVM)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:naturetrail_velo&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Piknika vietas (LVM)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:tourismrestingplace&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Atpūtas vietas (LVM)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:recreationplace_AtpV&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Skatu torņi (LVM)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:recreationplace_towers&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

## Forest Data
- **Mežaudžu dati (LVM)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:LVM_meza_dati&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Meža nogabali (LVM)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:pubcompartments_LVM&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Meža kvartāli (LVM)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:pubblock_LVM&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Mežaudžu dati (citi apsaimniekotāji)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:LVM_meza_dati_CITIaps&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Mežaudžu plāns (VMD pub. dati)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:vmdpubliccompartments&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

## Administrative Divisions
- **Latvijas administratīvais iedalījums**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:LV_admin_vienibas&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Ciemi**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:arisvillage&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Mazciemi**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:arissmallvillage&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Pagasti**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:arisparish&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Novadi**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:arisregion&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Pilsētas**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:ariscity&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

## Satellite and Aerial Imagery
- **Sentinel-2 pēdējo bezmākoņu attēlu mozaīka**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:Sentinel-2&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Ortofoto 7/8. cikls**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:Orto_LKS&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Ortofoto IS 7/8. cikls**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:OrtoIR_LKS&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Ortofoto NGR 7./8. cikls**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:OrtoNGR_LKS&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

## Topographic Maps
- **Topo10 ar reljefa ēnojumu un horizontālēm**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:Topo10DTM_contours&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Topokarte 1:10 000**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:Topo10&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Topokarte 1:50 000**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:Topo50&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Topokarte 1:75 000**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:Topo75LKS&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

## LiDAR and Terrain Models
- **Veģetācijas virsmas modelis, 1./2. cikls**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:CanopyHeightLKSnew&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Digitāls virsmas modelis, 1. cikls**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:DSM_LKS&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Digitāls virsmas modelis, 2. cikls**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:DSM_LV2&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Reljefa slīpuma modelis, 1/2. cikls**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:SlopesLKS2&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **LiDAR datu intensitāte**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:Intensity&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

## Environmental Models
- **Gruntsūdeņu modelis mālainiem nogulumiem**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:DTW10ha&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Gruntsūdeņu modelis smilšainiem nogulumiem**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:DTW30ha&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Pārmitro teritoriju modelis**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:WAM&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Vēja enerģijas blīvums**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:Wind_power_density&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Vēja ātrums**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:Wind_speed&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

## Geological Data
- **Kvartāra nogulumu karte**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:quaternary&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Augsnes laukumi**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:soils&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

## Other Maps and References
- **OpenStreetMap karte**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:OSM&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Military Grid Reference System**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:Mgrd&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Orientēšanās kartes**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:Okartes&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Rekreācijas zonas**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:recreationzone&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Reljefa krituma virzieni**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:Slope_aspect&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

## Forest Protection Areas
- **Vērtīgo egļu aizsardzības zona**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:vmdspruceprotbuffers&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Vērtīga egļu mežaudze (A zona)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=publicwfs:vmdspruceprotcompartments&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

## Additional Ortophoto Layers (Individual Cycles)
- **Ortofoto 1.cikls**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:Orto_1cikls&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Ortofoto 2.cikls**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:Orto_2cikls&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Ortofoto 3.cikls**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:Orto_3cikls&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Ortofoto 4.cikls**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:Orto_4cikls&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Ortofoto 5.cikls**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:Orto_5cikls&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Ortofoto 6.cikls**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:Orto_6cikls&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Ortofoto 7.cikls**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:Orto_7cikls&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Ortofoto 8.cikls**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:Orto_8cikls&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

## Infrared Ortophoto Layers
- **Ortofoto IS 3.cikls**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:OrtoIR_3cikls&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Ortofoto IS 5.cikls**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:OrtoIR_5cikls&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Ortofoto IS 6.cikls**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:OrtoIR_6cikls&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Ortofoto IS 7.cikls**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:OrtoIR_7cikls&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Ortofoto IS 8.cikls**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:OrtoIR_8cikls&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Ortofoto NGR 7.cikls**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:OrtoNGR_7cikls&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

## Sentinel-2 Time Series
- **Sentinel-2 vasaras RGB mozaīkas**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:S2_RGB_summers&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Sentinel-2 vasaras NGR mozaīkas**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:S2_NGR_summers&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Sentinel-2 vasaras NIR mozaīkas**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:S2_NIR_summers&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

## Baltic Region DTW Models
- **Depth-to-water map for areas with clayey soil bedrock (Estonia)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=baltic:DTW10ha_EE&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Depth-to-water map for areas with sandy soil bedrock (Estonia)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=baltic:DTW30ha_EE&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Depth-to-water map for areas with clayey soil bedrock (Lithuania)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=baltic:DTW10ha_LT&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

- **Depth-to-water map for areas with sandy soil bedrock (Lithuania)**
  - `https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=baltic:DTW30ha_LT&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX={left},{bottom},{right},{top}&WIDTH={tilesize}&HEIGHT={tilesize}`

---

## Usage Instructions

To use these WMS layers:

1. Replace `{left},{bottom},{right},{top}` with your bounding box coordinates in EPSG:3857 (Web Mercator)
2. Replace `{tilesize}` with your desired image width and height (e.g., 256, 512, 1024)

### Example:
For a 512x512 tile covering Riga area:
```
https://lvmgeoserver.lvm.lv/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&LAYERS=public:Orto_LKS&STYLES=&FORMAT=image/png&CRS=EPSG:3857&BBOX=2700000,7700000,2750000,7750000&WIDTH=512&HEIGHT=512
```

### Supported Formats:
- image/png
- image/jpeg
- image/gif
- image/tiff
- application/pdf
- image/svg+xml

### Supported CRS:
- EPSG:3857 (Web Mercator)
- EPSG:3059 (Latvia LKS-92)
- EPSG:4326 (WGS84)
- CRS:84