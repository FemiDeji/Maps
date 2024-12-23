import os
import geopandas as gpd
import folium
from shapely.geometry import box

nigeria_shapefile =os.path.abspath("ne_10m_admin_1_states_provinces.shp")
nigeria = gpd.read_file(nigeria_shapefile)

states_to_map = ['Osun', 'Oyo', 'Ekiti', 'Ondo', 'Ogun', 'Lagos']
global_bounds = box(-180, -90, 180, 90)

for state in states_to_map:
  d_state = nigeria[nigeria['name'] == state]
  centroid = d_state.geometry.centroid.iloc[0]
  m = folium.Map(location=(centroid.y, centroid.x), zoom_start=7)
  mask = gpd.GeoDataFrame(geometry=[global_bounds.difference(d_state.geometry.union_all())], 
                        crs=nigeria.crs)
  folium.GeoJson(mask, style_function=lambda x: {'fillColor': 'black', 'color': 'black'}).add_to(m)

# Add the mask as a layer to folium

  m.save(f"Mapss/{state}_cutout_map.html")
