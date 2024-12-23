import geopandas as gpd
import matplotlib.pyplot as plt
import osmnx as ox


# Load the shapefile
nigeria_shapefile = "ne_10m_admin_1_states_provinces.shp"
nigeria = gpd.read_file(nigeria_shapefile)

# Specify the state to map
state_name = "Osun"
d_state = nigeria[nigeria['name'] == state_name]
places = ['Osogbo',  'Ede']
gdfs = [ox.geocode_to_gdf(f"{place}, Osun, Nigeria") for place in places]
gdf_places = ox.features_from_polygon(d_state.geometry.iloc[0], tags={'place':True})

# Define places (districts/cities) within the state
# Replace with actual subdivisions if available in your data
places = gpd.GeoDataFrame({
    'name': gdf_places['name'],  # Place names
    'geometry': gdf_places['geometry']  # Polygons of each place
}, crs=d_state.crs)
# Assign unique colors to each place
place_colors = {
    'Osogbo': 'blue',
    'Ile-Ife': 'pink',
    'Ede': 'green'
}

# Add a color column to the GeoDataFrame
places['color'] = places['name'].map(place_colors)
print(places)
places['color'] = places['name'].map(place_colors).fillna('purple')

# Plotting
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the state with subdivisions colored
d_state.plot(ax=ax, color='lightblue', edgecolor='black')

for _, row in places.iterrows():
    # Create a temporary GeoDataFrame for each place
    temp_gdf = gpd.GeoDataFrame([row], crs=places.crs)
    # Plot the place with its color
    temp_gdf.plot(ax=ax, color=row['color'], edgecolor='black', label=row['name'])

# Add a title and legend
ax.set_title(f"Map of {state_name} with Key Places", fontsize=16)
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.legend(title="Places", loc="upper left", fontsize=10)

# Show the plot
plt.show()
