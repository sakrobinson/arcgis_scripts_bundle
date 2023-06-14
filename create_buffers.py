# This assumes that you have an active session running
import arcpy

# Set workspace
arcpy.env.workspace = r"C:\your\workspace\here.gdb"
buffer_radius = 10 #miles
# Set input shapefile
input_shapefile = "your_points_here.shp"

# Set buffer distance parameter in miles
buffer_distance = "{} Miles".format(buffer_radius)

# Set output shapefile
output_shapefile = "{}_{}mi_buffer.shp".format(input_shapefile[:-4], buffer_radius)

# Generate buffers
arcpy.Buffer_analysis(input_shapefile, output_shapefile, buffer_distance)

# Add output shapefile to map
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "*")[0]
addLayer = arcpy.mapping.Layer(output_shapefile)
arcpy.mapping.AddLayer(df, addLayer, "BOTTOM")

# Refresh the map
arcpy.RefreshTOC()
arcpy.RefreshActiveView()
