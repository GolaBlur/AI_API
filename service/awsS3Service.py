import boto3
from configuration.config import *
import os


### S3 Connection ###
def s3_connection():
    s3_bucket = boto3.client('s3',
                          aws_access_key_id = AWS_ACCESS_KEY,
                          aws_secret_access_key = AWS_SECRET_KEY)
    return s3_bucket


### 저장할 경로 설정
def set_s3_path(entity):
    return entity.User_ID + '/' + entity.File_ID + '/'

def set_s3_file_name(entity):
    return entity.File_ID + '.' + entity.File_Extension


### S3에 파일 업로드 후 DB에 저장할 형태로 반환
class store:
    
    def store_file_at_s3(file_entity, file):
        
        s3 = s3_connection()
        
        ### 다운로드할 파일의 s3에서의 경로
        file_name = set_s3_file_name(entity= file_entity)
        path = set_s3_path(entity = file_entity) + 'result/' + file_name
        
        s3.put_object(
            Bucket = BUCKET_NAME,
            Body = file,
            Key = path,
            ACL = 'public-read'
        )
        
    
    def store_object_at_s3(object_entity_list, object_list):
        
        s3 = s3_connection()
        
        ### 다운로드할 파일의 s3에서의 경로
        if object_entity_list.__sizeof__ != 0:
            entity = object_entity_list[0]
            path = set_s3_path(entity=entity) + 'object/'
        
        ### for each 문을 통해 list 내의 객체들 저장
        for object_ in object_list:
            file_name = object_.name[len('resources/object/upload'):]
            object_path = path + file_name
            
            s3.put_object(
                Bucket = BUCKET_NAME,
                Body = object_,
                Key = object_path,
                ACL = 'public-read'
            )
            


class bring:
    
    def bring_file_from_s3(file_entity):
        
        s3 = s3_connection()
        
        ### 가져올 파일의 경로
        file_name = set_s3_file_name(entity=file_entity)
        s3_path = set_s3_path(entity=file_entity) + file_name        
        
        ### 저장할 경로 및 파일 명
        local_path = 'resources/file/download/' + file_name
        
        
        s3.download_file(
            BUCKET_NAME,
            s3_path,
            local_path
        )
        
        return open(local_path, 'rb')
    
    def bring_object_from_s3(object_list):
        
        ### object file list
        object_file_list = []
        
        s3 = s3_connection()
        
        ### for each  문을 통해 list 내의 객체들을 다운로드 후 리스트에 추가하여 반환
        for object_entity in object_list:
            ### 가져올 파일의 경로   
            file_name = set_s3_file_name(object_entity)
            s3_path = set_s3_path(object_entity) + 'object/' + file_name
            ### 저장할 경로 및 파일 명
            local_path = 'resources/object/download/' + file_name
            
            s3.download_file(
                BUCKET_NAME,
                s3_path,
                local_path
            )
            
            object_file_list.append(open('local_path','rb'))
        
        return object_file_list





# class tests3:
    
#     def test_upload_image():
        
#         s3 = s3_connection()
        
#         s3.put_object(
#             Bucket = BUCKET_NAME,
#             Body = file,
#             Key = 'hihi/ttt.jpg',
#             ACL = 'public-read'
#         )
        
#         return '200'
        
#     def test_download_image():
        
#         s3 = s3_connection()
        
#         s3.download_file(
#             BUCKET_NAME, 
#             'hihi/ttt.jpg', 
#             'resources/file/download/wow.jpg'
#             )
        
#         return '200'
    
    
#     def test_upload_video():
        
#         s3 = s3_connection()
        
#         s3.put_object(
#             Bucket = BUCKET_NAME,
#             Body = file,
#             Key = 'video/hi.mp4',
#             ACL = 'public-read'
#         )
        
#         return
    
#     def test_download_video():
        
#         s3 = s3_connection()
        
#         s3.download_file(
#             BUCKET_NAME,
#             'video/hi.mp4',
#             'resources/file/download/yaya.mp4'
#             )
        
#         return
    