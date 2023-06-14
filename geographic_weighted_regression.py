# Script is a template used for geographic weighted regression in arcpy.
# You will want to update parameters to best give context to your problem.

import arcpy

# Set workspace
arcpy.env.workspace = r"C:\your\workspace\here.gdb"

# Set input feature class representing the dependent variable
dependent_variable = "your_dependent_variable_fc"

# Set input feature class representing the independent variables
independent_variables = ["independent_variable_1_fc", "independent_variable_2_fc"]

# Set input feature class representing the distance to neighboring features
distance_feature_class = "your_distance_fc"

# Set the output feature class for the GWR results
output_feature_class = "your_gwr_results_fc"

# Set the spatial weights matrix type to use
# Options: "K_NEAREST_NEIGHBORS", "DISTANCE_BAND", "ADAPTIVE_KERNEL"
spatial_weights_matrix_type = "K_NEAREST_NEIGHBORS"

# Set the number of nearest neighbors to use for KNN or AK spatial weights matrix types
k = 4

# Set the distance band threshold to use for DISTANCE_BAND spatial weights matrix type
distance_band = 500

# Set the adaptive kernel type to use for ADAPTIVE_KERNEL spatial weights matrix type
# Options: "FIXED", "VARIABLE"
adaptive_kernel_type = "FIXED"

# Set the bandwidth value for the adaptive kernel
adaptive_kernel_bandwidth = 1000

# Set the dependent variable field name
dependent_variable_field = "your_dependent_variable_field_name"

# Set the independent variable field names
independent_variable_fields = [["independent_variable_1_field_name_1", "independent_variable_1_field_name_2"],
                              ["independent_variable_2_field_name_1", "independent_variable_2_field_name_2"]]

# Set the distance field name in the distance feature class
distance_field = "your_distance_field_name"

# Create a spatial weights matrix object using the specified parameters
spatial_weights = arcpy.stats.GenerateSpatialWeightsMatrix(dependent_variable, distance_feature_class, 
                                                           spatial_weights_matrix_type, distance_field, 
                                                           k=k, distance_band=distance_band, 
                                                           adaptive_kernel_type=adaptive_kernel_type, 
                                                           adaptive_kernel_bandwidth=adaptive_kernel_bandwidth)

# Create a multivariate GWR model object using the specified parameters
gwr_model = arcpy.stats.MultivariateGeographicallyWeightedRegression(dependent_variable, independent_variables, 
                                                                     spatial_weights, dependent_variable_field, 
                                                                     independent_variable_fields)

# Run the GWR model and save the results to the output feature class
arcpy.management.CopyFeatures(gwr_model, output_feature_class)
