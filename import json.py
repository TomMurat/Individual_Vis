import json
import csv

# Load the GeoJSON data
with open('MSOA_(Dec_2011)_Boundaries_Generalised_Clipped_(BGC)_EW_V3 (1).geojson', 'r') as f:
    geojson = json.load(f)

# Load the CSV data
with open('Data_plot.csv', 'r') as f:
    csvdata = list(csv.DictReader(f))

# Loop through the CSV data and add it to the GeoJSON features
for d in csvdata:
    print(d)
    # Find the GeoJSON feature that matches the CSV data row
    feature = next((f for f in geojson['features'] if f['properties']['MSOA11CD'] == d['geography code']), None)

    # If a matching feature is found, add the CSV data as new properties to the feature
    if feature:
                feature['properties']['General Health Bad or Very Bad %'] = float(d['General Health Bad or Very Bad %']);
                feature['properties']['White Resident'] = float(d['White Resident']);
                feature['properties']['Mixed Ethnic'] = float(d['Mixed Ethnic']);
                feature['properties']['Asian'] = float(d['Asian']);
                feature['properties']['Black'] = float(d['Black']);
                feature['properties']['Other'] = float(d['Other']);
            

# Save the modified GeoJSON data to a new file
with open('output.geojson', 'w') as f:
    json.dump(geojson, f)