# Fabric notebook source

# METADATA ********************
#

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "1ac48b28-2d17-426f-970f-f02fbb6cf23c",
# META       "default_lakehouse_name": "FabricLakehouse",
# META       "default_lakehouse_workspace_id": "b4a22bcc-f416-427f-b553-dd4bf47921ab",
# META       "known_lakehouses": [
# META         {
# META           "id": "1ac48b28-2d17-426f-970f-f02fbb6cf23c"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("SELECT * FROM FabricLakehouse.dimension_customer LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
