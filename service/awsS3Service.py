import boto3
from aws.aws_connector import *


BUCKET_NAME = 'golablur'

class store:
    
    
    def store_file_at_s3(file_id, file):
        golablur = s3_connector.connect_to_s3_bucket()
        return golablur.upload_file(
            Filename = file, 
            Bucket = BUCKET_NAME,
            Key = 'python/'+file_id+'.jpg'
        )
    
    def store_object_at_s3():
        
        
        
        return


class bring:
    
    def bring_file_from_s3():
        
        
        
        return
    
    def bring_object_from_s3():
        
        
        
        return
    
    



class tests3:
    
    def get_s3_list():
        s3_connector.connect_to_s3_bucket()
        
        s3 = boto3.resource("s3")
        
        for bucket in s3.buckets.all():
            print(bucket.name)