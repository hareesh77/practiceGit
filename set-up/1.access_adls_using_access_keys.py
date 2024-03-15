# Databricks notebook source
formuala1dl_account_key=dbutils.secrets.get(scope='formula1-scope',key='learningdl01-account-key')

# COMMAND ----------

spark.conf.set("fs.azure.account.key.learningdl01.dfs.core.windows.net",formuala1dl_account_key)


# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@learningdl01.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv('abfss://demo@learningdl01.dfs.core.windows.net',header='True'))

# COMMAND ----------


