# Databricks notebook source
# MAGIC %md
# MAGIC ### Access Azure data lake using SAS Token
# MAGIC 1.set the spark config for SAS Token\
# MAGIC 2.List files from demo container\
# MAGIC 3.read data from circuits.csv file

# COMMAND ----------

formula1dl_demo_sas_token=dbutils.secrets.get(scope='formula1-scope',key='formula1dl-demo-sas-token')

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.learningdl01.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.learningdl01.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.learningdl01.dfs.core.windows.net",formula1dl_demo_sas_token)

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@learningdl01.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv('abfss://demo@learningdl01.dfs.core.windows.net',header=True))

# COMMAND ----------


