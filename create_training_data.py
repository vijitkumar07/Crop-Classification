import ee
import geemap

# Initialize Google Earth Engine
ee.Initialize(project='crop-classification-476512')

# 👉 Paste the coordinates you copied from Google Maps here (latitude, longitude):
lat, lon = 22.385024918689236, 82.82977579992216   # ← Replace these values with the ones you copied

# Create the map centered at the pasted coordinates
Map = geemap.Map(center=[lat, lon], zoom=16)  # zoom=16 for close-up view
Map.add_basemap('SATELLITE')                 # Google Satellite imagery

# Optional: add a point marker where you pasted the coordinates
crop_point = ee.Geometry.Point([lon, lat]) 
Map.addLayer(crop_point, {'color': 'red'}, 'Crop Point')

# Display the map
Map
