import folium

# Create a map with specific width and height
my_map = folium.Map(location=[7.4244,  4.1084], zoom_start=7, width='500px', height='300px' )

# Add a marker
# folium.Marker(location=[7.4244, 4.1084], popup="Location 1").add_to(my_map)

# Example locations
locations = [
    {"name": "Shaki", "coords": [8.672557, 3.394336]},
    {"name": "Iseyin", "coords": [7.978027, 3.591025]},
    {"name": "Ilesha", "coords": [7.610866, 4.709997]},
    {"name": "Ikirun", "coords": [7.926275, 4.666292]},
    {"name": "Ife", "coords": [7.490538, 4.552202]},
    {"name": "Ewekoro", "coords": [6.9048750, 3.2072176]},
    {"name": "Aramoko-Ekiti", "coords": [7.706935, 5.04311]},
    {"name": "Okitipupa", "coords": [6.502736, 4.777146]},
    {"name": "Sagamu", "coords": [6.832415, 3.63216]},
    {"name": "Ikorodu", "coords": [6.618608, 3.510785]},
]

bounds = [[6.0000,  3.0000] , [8.7000, 5.000]]

# # Calculate bounds for the rectangle
# latitudes = [loc["coords"][0] for loc in locations]
# longitudes = [loc["coords"][1] for loc in locations]
# bounds = [[min(6.0000), min(3.0000)], [max(8.0000), max(5.0000)]]

# # Create a rectangle to form a frame around the specified locations
# folium.Rectangle(bounds=bounds, color='red', fill=True, fill_opacity=0.2).add_to(my_map)

# my_map.fit_bounds(bounds,max_zoom=0)

# Add markers for each location
for loc in locations:
    folium.Marker(
        location=loc["coords"],
        popup=loc["name"],
        icon=folium.Icon(color='blue')
    ).add_to(my_map)

# Create a list of coordinates for the polyline
latlngs = [loc["coords"] for loc in locations]

# Add a polyline connecting the locations
folium.PolyLine(locations=latlngs, color='red').add_to(my_map)

# Save the map to an HTML file
my_map.save("my_map.html")

print("Map has been created and saved as 'my_map.html'")