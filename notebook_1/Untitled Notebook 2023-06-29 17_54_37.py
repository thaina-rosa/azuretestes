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
df = spark.read.option("header", "true").option("inferSchema", "true").option("delimiter", ";").csv("/mnt/blobthai/Sales.SpecialOfferProduct.csv")

# COMMAND ----------

df.display()

# COMMAND ----------

dfc =df.withColumn("ModifiedDate", 
                   col("ModifiedDate").cast(DateType()))

# COMMAND ----------

# Jogar na tabela
dfc.write \
.mode('overwrite') \
.format("jdbc") \
.option("url", "jdbc:sqlserver://servidora.database.windows.net:1433;database=bancot;user=admin-azure@servidora;password=") \
.option("dbtable", "SpecialOfferProduct") \
.option("databaseName", "bancot") \
.option("user", "admin-azure") \
.option("password", "@Anhembi2020") \
.save()


# COMMAND ----------

