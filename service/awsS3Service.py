import boto3
from config.config import *


### S3 Connection ###
def s3_connection():
    s3_bucket = boto3.client('s3',
                          aws_access_key_id = AWS_ACCESS_KEY,
                          aws_secret_access_key = AWS_SECRET_KEY)
    return s3_bucket



class store:
    
    
    def store_file_at_s3():
        
        
        return
    
    def store_object_at_s3():
        
        
        
        return


class bring:
    
    def bring_file_from_s3():
        
        
        
        return
    
    def bring_object_from_s3():
        
        
        
        return
    
    



class tests3:
    
    def test_upload_file(file):
        
        s3 = s3_connection()
        
        s3.put_object(
            Bucket = BUCKET_NAME,
            Body = file,
            Key = 'hihi/ttt.jpg',
            ACL = 'public-read'
        )
        
        return '200'
        
    def test_download_file():
        
        s3 = s3_connection()
        
        s3.download_file(BUCKET_NAME, 'hihi/ttt.jpg', 'resources/file/download/wow.jpg')
        
        return '200'