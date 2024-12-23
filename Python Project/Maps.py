import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
import os
from shapely.geometry import point

# Load a shapefile of Nigeria's administrative boundaries (you need to obtain this shapefile)
# For example, you might have 'nigeria_admin.shp' which contains various states
nigeria_shapefile =os.path.abspath("ne_10m_admin_1_states_provinces.shp")
print(nigeria_shapefile)
nigeria = gpd.read_file(nigeria_shapefile)
print(nigeria.columns)

# List of states to map
states_to_map = ['Osun', 'Oyo', 'Ekiti', 'Ondo', 'Ogun', 'Lagos']

# Create a directory to save the maps
import os
output_dir = 'maps'
os.makedirs(output_dir, exist_ok=True)

# Loop through each state and create a map
for state in states_to_map:
    # Filter state
    state_data = nigeria[nigeria['name'] == state]  # Adjust 'NAME' based on your shapefile's attribute
    
    # Plot
    fig, ax = plt.subplots(figsize=(10, 10))
    state_data.plot(ax=ax, color='lightblue', edgecolor='black')

# Define the locations for each state
locations_data = {
    'Osun': {
        'Ifewara': (7.466136, 4.678154),
        'Osogbo': (7.782669, 4.541811),
        'Ilesha': (7.610345, 4.709638)
    },
    'Oyo': {
        'Saki': (8.672554, 3.394332),
        'Iseyin': (7.976494, 3.591391)
    },
    'Ekiti': {
        'Aramoko-Ekiti': (7.709372, 5.041659)
    },
    'Ondo': {
        'Okitipupa': (6.502477, 4.779518)
    },
    'Ogun': {
        'Ewekoro': (6.900274, 3.203076)
    },
    'Lagos': {
        'Ikorodu': (6.619418, 3.510450)
    }
}

# Create a GeoDataFrame for all locations
all_locations = []
for state, cities in locations_data.items():
    for city, (latitude, longitude) in cities.items():
        all_locations.append({'State': state, 'City': city, 'Latitude': latitude, 'Longitude': longitude})

locations_df = gpd.GeoDataFrame(all_locations, 
                                  geometry=gpd.points_from_xy([loc['Longitude'] for loc in all_locations],
                                                                [loc['Latitude'] for loc in all_locations]))

# Set the CRS (Coordinate Reference System) to WGS84
locations_df.set_crs(epsg=4326, inplace=True)

# Define colors for each state
state_colors = {
    'Osun': 'lightblue',
    'Oyo': 'lightgreen',
    'Ekiti': 'lightcoral',
    'Ondo': 'lightyellow',
    'Ogun': 'lightpink',
    'Lagos': 'lightgray'
}

# Create a plot for each state
fig, axs = plt.subplots(2, 3, figsize=(18, 12))  # Adjust the number of rows and columns as needed
axs = axs.flatten()  # Flatten the 2D array of axes

for ax, (state, color) in zip(axs, state_colors.items()):
    # Filter locations for the current state
    state_locations = locations_df[locations_df['State'] == state]
    
    # Plot the Nigeria map
    nigeria.plot(ax=ax, color='lightgrey', edgecolor='black')
    
    # Plot the locations for the current state
    state_locations.plot(ax=ax, color=color, markersize=100, label=state, alpha=0.7)
    
    # Annotate the locations
    for x, y, label in zip(state_locations.geometry.x, state_locations.geometry.y, state_locations['City']):
        ax.text(x, y, label, fontsize=9, ha='right')
    
    # Set title and legend
    ax.set_title(f'{state} Locations')
    ax.legend()

# Adjust layout
# plt.tight_layout()
# plt.show()

# Plotting the map with different colors for each state
# Replace 'NAME' with the actual column name that contains state names or identifiers
fig, ax = plt.subplots(figsize=(10, 10))
state_data.plot(column= 'name',  # Change 'NAME' to the appropriate column for states
             cmap='Set3',   # Choose a colormap
             legend=True,   # Show legend
             edgecolor='black',  # Color of the edges
             linewidth=0.5,  # Edge line width
             ax=ax)

# Title and display
# plt.title('Map of Nigeria by State')
# plt.show()

    # Add basemap
    # ctx.add_basemap(ax, crs=state_data.crs.to_string(), source=ctx.providers.Stamen.Terrain)

# Title and labels
ax.set_title(f'Map of {state}', fontsize=15)
ax.set_axis_off()  # Turn off the axis

    # Save the map
plt.savefig(os.path.join(output_dir, f'{state}_map.png'), bbox_inches='tight')
plt.close()

print("Maps have been created and saved in the 'maps' directory.")





# Osun
# ifewara = 7.466136, 4.678154
# osogbo = 7.782669, 4.541811
# ilesha = 7.610345, 4.709638

# Oyo
# saki = 8.672554, 3.394332
# iseyin = 7.976494, 3.591391

# Ekiti
# aramoko-ekiti = 7.709372, 5.041659

# Ondo
# okitipupa = 6.502477, 4.779518

# Ogun
# ewekoro = 6.900274, 3.203076

# Lagos
# Ikorodu = 6.619418, 3.510450