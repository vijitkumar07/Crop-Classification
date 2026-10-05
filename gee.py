import ee

# Initialize Earth Engine
ee.Initialize(project='crop-classification-476512')

# Define your Area of Interest (AOI) — for example, a small area in India
aoi = ee.Geometry.Rectangle([77.5, 12.8, 77.7, 13.0])  # [xmin, ymin, xmax, ymax]

# Load Sentinel-2 surface reflectance image collection
s2 = ee.ImageCollection('COPERNICUS/S2_SR') \
        .filterBounds(aoi) \
        .filterDate('2024-01-01', '2024-12-31') \
        .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 10))

# Select one median composite image
median = s2.median().clip(aoi)

# Print info
print("✅ Sentinel-2 Image Collection loaded successfully!")
print("Total images found:", s2.size().getInfo())

# Get some info about bands
print("Available bands:", median.bandNames().getInfo())

# Export (optional later)
# You can export this image later to Google Drive or Cloud Storage
