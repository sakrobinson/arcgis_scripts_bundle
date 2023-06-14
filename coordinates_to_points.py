# use this tempalte to convert from coordinates (lat/long) to a points file. 
# CAUTION: plot against a basemap to see if the coordinate system is OK!
import arcpy

# Set the workspace and input/output file paths
arcpy.env.workspace = r"C:\data"
input_file = "coordinates.csv"
output_file = "points.shp"

# Create a new point feature class
arcpy.CreateFeatureclass_management(arcpy.env.workspace, output_file, "POINT")

# Add fields for latitude and longitude
arcpy.AddField_management(output_file, "Latitude", "DOUBLE")
arcpy.AddField_management(output_file, "Longitude", "DOUBLE")

# Open an insert cursor and add the points to the feature class
with arcpy.da.InsertCursor(output_file, ["SHAPE@", "Latitude", "Longitude"]) as cursor:
    # Open the input file and loop through each row
    with open(input_file, "r") as f:
        for line in f:
            # Split the line into latitude and longitude values
            lat, lon = line.strip().split(",")

            # Create a point object and set the latitude and longitude fields
            point = arcpy.Point(float(lon), float(lat))
            feature = [point, float(lat), float(lon)]

            # Insert the new feature into the feature class
            cursor.insertRow(feature)

# Print the results
print("Points created. Output file: " + output_file)
