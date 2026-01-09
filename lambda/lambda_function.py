import boto3

def lambda_handler(event, context):
    glue = boto3.client("glue")

    glue.start_job_run(
        JobName="clean-data-job",
        Arguments={
            "--input_path": "s3://raw-bucket-vas/input/",
            "--output_path": "s3://clean-bucket-vas/output/"
        }
    )

    return {
        "statusCode": 200,
        "body": "Glue job triggered"
    }
