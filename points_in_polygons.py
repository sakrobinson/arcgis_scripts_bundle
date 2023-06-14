# Points in polygons - spatial join. You can update parameters including the "match_option", and "join_type"
import arcpy

# Set workspace
arcpy.env.workspace = r"C:\your\workspace\here.gdb"

# Set input polygon shapefile
polygon_shapefile = arcpy.GetParameterAsText(0)

# Set input point shapefile
point_shapefile = arcpy.GetParameterAsText(1)

# Set output shapefile
output_shapefile = "{}_joined.shp".format(point_shapefile[:-4])

# Create a spatial join between the polygon and point shapefiles
arcpy.SpatialJoin_analysis(target_features=polygon_shapefile, join_features=point_shapefile, 
                           out_feature_class=output_shapefile, join_operation="JOIN_ONE_TO_MANY", 
                           join_type="KEEP_ALL", match_option="WITHIN")

# Add output shapefile to map
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "*")[0]
addLayer = arcpy.mapping.Layer(output_shapefile)
arcpy.mapping.AddLayer(df, addLayer, "BOTTOM")

# Refresh the map
arcpy.RefreshTOC()
arcpy.RefreshActiveView()
