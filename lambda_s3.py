import json
import boto3
import os


def lambda_handler(event, context):
    # TODO implement
    
    bucket_name = os.environ['bucketName']
    
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket(bucket_name)
    fileList = []
    
    try:
        for file in my_bucket.objects.all():
            fileList.append(file.key)
        
        return {
            'statusCode': 200,
            'body': json.dumps(fileList)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': e
        }