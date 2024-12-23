import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt
# Get boundary polygon for Osun state (this is already defined in your shapefile)
state_name = "Osun"
nigeria_shapefile = "ne_10m_admin_1_states_provinces.shp"
nigeria = gpd.read_file(nigeria_shapefile)
d_state = nigeria[nigeria['name'] == state_name]

# Download all places (towns, cities, villages) within the state boundary using Overpass API
gdf_places = ox.features_from_polygon(d_state.geometry.iloc[0], tags={'place':True})

# Display the places GeoDataFrame
print(gdf_places)

# Plot all places on a map
gdf_places.plot(figsize=(10, 10), color='purple', edgecolor='black')
plt.title(f"Places in {state_name}")
plt.show()
