settings = {
	"aoi":"https://gdh-data-sandbox.ams3.digitaloceanspaces.com/data/brazil_polygon.json",
  "systems":["GI", "TRANS", "URBAN", "AG", "HYDRO"],
  
  # "systems": ['GI'],
	"outputdirectory":"output",
	"workingdirectory": "working", 
	"sentinelscene": "S2B_MSIL1C_20171010T133209_N0205_R081_T23LKC_20171010T133528",
  "rivers":"rivers/rivers.shp",
  "watersheds":"watershed/watershed.shp"
}
processchains = {
	"GI":{"list": [{"id": "importer_1",
          "module": "importer",
          "inputs": [{"import_descr": {"source": settings['sentinelscene'],
                                       "type": "sentinel2",
                                       "sentinel_band": "B04"},
                      "param": "map",
                      "value": "B04"},
                     {"import_descr": {"source": settings['sentinelscene'],
                                       "type": "sentinel2",
                                       "sentinel_band": "B08"},
                      "param": "map",
                      "value": "B08"},
                      {"import_descr": {"source": settings['aoi'],
                      	                "type": "vector"},
                       "param": "map",
                       "value": "aoi"}]},

         {"id": "g_region_1",
          "module": "g.region",
          "inputs": [{"param": "raster",
                      "value": "B04"}],
          "flags": "g"},

          {"id": "g_region_2",
          "module": "g.region",
          "inputs": [{"param": "vector",
                      "value": "aoi"}],
          "flags": "g"},

          {"id": "r_mask",
          "module": "r.mask",
          "inputs": [{"param": "vector",
                      "value": "aoi"}]},

         {"id": "rmapcalc_1",
          "module": "r.mapcalc",
          "inputs": [{"param": "expression",
                      "value": "NDVI = float((B08 - B04)/(B08 + B04))"}]},

          {"id": "r_univar_ndvi",
          "module": "r.univar",
          "inputs": [{"param": "map",
                      "value": "NDVI"}],
          "flags": "g"},

         {"id": "r_slope_aspect",
          "module": "r.slope.aspect",
          "inputs": [{"param": "elevation",
                      "value": "srtmgl1_v003_30m@srtmgl1_30m"},
                      {"param": "slope",
                      "value": "slope"}]},\
         {"id": "exporter_1",
          "module": "exporter",
          "outputs": [{"export": {"type": "raster", "format": "GTiff"},
                       "param": "map",
                       "value": "NDVI"},
                       {"export": {"type": "raster", "format": "GTiff"},
                       "param": "map",
                       "value": "slope"},
                       # {"export": {"type": "raster", "format": "GTiff"},
                       # "param": "map",
                       # "value": "B04"},
                       # {"export": {"type": "raster", "format": "GTiff"},
                       # "param": "map",
                       # "value": "B08"}
                       ]}
         ],
"version": "1"}
}
