# Databricks notebook source
# MAGIC %md
# MAGIC ###Access Azure Data Lake using cluste scoped credentials
# MAGIC 1.Set the spark config fs.azure.account.kwy in the cluster\
# MAGIC 2.List files from demo container\
# MAGIC 3.Read data frpm circuits.csv file
# MAGIC

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@learningdl01.dfs.core.windows.net"))

# COMMAND ----------

 # Read CSV file
display(spark.read.format("csv").option("header", "true").load("abfss://demo@learningdl01.dfs.core.windows.net"))

# COMMAND ----------


