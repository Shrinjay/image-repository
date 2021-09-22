from boto3 import client


class S3Manager:
    def __init__(self, bucket):
        self.client = client('s3')
        self.bucket = bucket

    def put(self, key, data):
        self.client.put_object(Bucket=self.bucket, Key=key, Body=data)

    def get(self, key):
        return self.client.get_object(Bucket=self.bucket, Key=key)['Body']

    def get_url(self, key):
        return self.client.generate_presigned_url(ClientMethod='get_object', Params={'Bucket': self.bucket, 'Key': key})
