from pyspark.sql import  SparkSession

spark = SparkSession.builder.appName("SparkSample").master("local")\
    .getOrCreate()

print("Spark is started and checking now.")
print(spark)