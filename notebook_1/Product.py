# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *


# COMMAND ----------

# criando a conexao com blob 
container = "blobthai" #- nome do container 
key = "uPjSvs0p0LfxMTL+6k2dDYAB/k+6YaKxwHd55kDTBR2uAPcio3GsKhaz6avEbhUGKRjlNzLt9r7D+ASt52jnkw==" 
storage = "blobthai"

# COMMAND ----------

spark.conf.set(f'fs.azure.sas.{container}.{storage}.blob.core.windows.net', key )

# COMMAND ----------

#verificando se existe um mount point caso já exista sera desmontado
def sub_unmount(str_path):
    if any(mount.mountPoint == str_path for mount in dbutils.fs.mounts()):
      
        dbutils.fs.unmount(str_path)
        
sub_unmount('/mnt/blobthai')

# COMMAND ----------

#criando o mont
dbutils.fs.mount(
source = f'wasbs://{container}@{storage}.blob.core.windows.net',
mount_point = '/mnt/blobthai',
extra_configs = {f'fs.azure.account.key.{storage}.blob.core.windows.net': key}
)

# COMMAND ----------

#listando arquivos dentro do blob
dbutils.fs.ls("/mnt/blobthai")

# COMMAND ----------

#pegando arquivos 
df = spark.read.option("header", "true").option("inferSchema", "true").option("delimiter", ";").csv("/mnt/blobthai/Production.Product.csv")

# COMMAND ----------

df.display()

# COMMAND ----------

dfp = df.toPandas()

# COMMAND ----------

dfp.loc[dfp['Color'] == 'NULL', 'Color'] = 'NaoInformado'

# COMMAND ----------

dfp.loc[dfp['Style'] == 'NULL', 'Style'] = 'NaoInformado'

# COMMAND ----------

#dfp.loc[dfp['SellEndDate'] == 'NULL', 'SellEndDate'] = 'NaoInformado'

# COMMAND ----------

dfp.loc[dfp['Weight'] == 'NULL', 'Weight'] = 'NaoInformado'

# COMMAND ----------

dfp.loc[dfp['WeightUnitMeasureCode'] == 'NULL', 'WeightUnitMeasureCode'] = 'NaoInformado'

# COMMAND ----------

dfp.loc[dfp['SizeUnitMeasureCode'] == 'NULL', 'SizeUnitMeasureCode'] = 'NaoInformado'

# COMMAND ----------

#dfp.loc[dfp['DiscontinuedDate'] == 'NULL', 'DiscontinuedDate'] = 'NaoInformado'

# COMMAND ----------

dfp.loc[dfp['Class'] == 'NULL', 'Class'] = 'NaoInformado'

# COMMAND ----------

dfp.loc[dfp['ProductLine'] == 'NULL', 'ProductLine'] = 'NaoInformado'

# COMMAND ----------

dfp.loc[dfp['ProductSubcategoryID'] == 'NULL', 'ProductSubcategoryID'] = 'NaoInformado'

# COMMAND ----------

dfp.loc[dfp['SizeUnitMeasureCode'] == 'NULL', 'SizeUnitMeasureCode'] = 'NaoInformado'

# COMMAND ----------

dfp.loc[dfp['WeightUnitMeasureCode'] == 'NULL', 'WeightUnitMeasureCode'] = 'NaoInformado'

# COMMAND ----------

dfp.loc[dfp['ProductSubcategoryID'] == 'NULL', 'ProductSubcategoryID'] = 'NaoInformado'

# COMMAND ----------

dfp.loc[dfp['ProductModelID'] == 'NULL', 'ProductModelID'] = 'NaoInformado'

# COMMAND ----------

dfs = spark.createDataFrame(dfp)

# COMMAND ----------

dfs.display()

# COMMAND ----------

dfd = dfs.withColumn("SellStartDate",col('SellStartDate').cast(DateType()))\
         .withColumn("DiscontinuedDate",col('DiscontinuedDate').cast(DateType()))\
         .withColumn("SellEndDate",col('SellEndDate').cast(DateType()))

# COMMAND ----------

dfd.display()

# COMMAND ----------



# COMMAND ----------

# Jogar na tabela
dfd.write \
.mode('overwrite') \
.format("jdbc") \
.option("url", "jdbc:sqlserver://servidora.database.windows.net:1433;database=bancot;user=admin-azure@servidora;password=") \
.option("dbtable", "Product") \
.option("databaseName", "bancot") \
.option("user", "admin-azure") \
.option("password", "@Anhembi2020") \
.save()

# COMMAND ----------

