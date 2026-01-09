import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME','input_path','output_path'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

df = spark.read.option("header","true").csv(args['input_path'])
clean_df = df.dropna().dropDuplicates()
clean_df.write.mode("overwrite").parquet(args['output_path'])

job.commit()
