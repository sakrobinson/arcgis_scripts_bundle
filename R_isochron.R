library(sp)
library(raster)
library(gdistance)

# Set workspace
setwd("C:/your/workspace/here")

# Set input point shapefile
points_shapefile <- "your_points_shapefile.shp"

# Set input cost raster
cost_raster <- raster("your_cost_raster.tif")

# Convert the input point shapefile to a SpatialPointsDataFrame object
points_spdf <- readOGR(dsn = ".", layer = points_shapefile)

# Set the maximum travel distance in meters
max_distance <- 5000

# Set the travel direction as "from" (i.e., calculate isochrones from the points)
travel_direction <- "from"

# Convert the cost raster to a cost surface object
cost_surface <- transition(cost_raster, mean)

# Calculate the isochrone using the cumulative cost function
isochrone <- costDistance(cost_surface, points_spdf, max_distance = max_distance, direction = travel_direction)

# Convert the isochrone to a raster object
isochrone_raster <- raster(isochrone)

# Save the isochrone raster to a file
writeRaster(isochrone_raster, "isochrone.tif", format = "GTiff", overwrite = TRUE)

# Plot the isochrone raster
plot(isochrone_raster)
