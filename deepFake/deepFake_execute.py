import sys
sys.path.append("D:/ImmersionProject/FinalProject/GolaBlur/API-AI/AI_API")
from service.awsS3Service import *
from deepFake_image import deepFake_image_func
from deepFake_video import deepFake_video_func
from deepFake_group_image import deepFake_group_image_func
import uuid
import os

class deepFake_execute:
    def image(target_entity, source_entity):
        ## s3에서 처리할 파일 다운로드
        target_file = bring.bring_file_from_s3(file_entity=target_entity)
        source_file = bring.bring_file_from_s3(file_entity=source_entity)
        
        target_file_path = os.path(target_file)
        source_file_path = os.path(source_file)
        
        ## TODO 이미지 딥페이크 기능 함수 구현 후 여기서 호출하여 기능 수행
        ## 기능 수행
        res_file = deepFake_image_func(source_img_path=source_file_path, target_img_path=target_file_path)
                
        ## s3에 처리된 파일 업로드
        res_file_entity = change_file_to_entity_and_store_at_s3(file=res_file, original_file_entity=source_entity)
                
        return res_file_entity
    
    def video(target_entity, source_entity):
        ## s3에서 처리할 파일 다운로드
        target_file = bring.bring_file_from_s3(file_entity=target_entity)
        source_file = bring.bring_file_from_s3(file_entity=source_entity)
        
        target_file_path = os.path(target_file)
        source_file_path = os.path(source_file)
        
        ## TODO 비디오 딥페이크 기능 함수 구현 후 여기서 호출하여 기능 수행
        ## 기능 수행
        res_file = deepFake_video_func(target_video_path=target_file_path, source_img_path=source_file_path)
        
        ## s3에 처리된 파일 업로드
        res_file_entity = change_file_to_entity_and_store_at_s3(file=res_file, original_file_entity=target_entity)
        
        return res_file_entity
    
    def group_images(source_group_entity_list, target_entity):
        ## s3에서 처리할 파일 다운로드
        target_group_file_path_list = []
        for target_entity in source_group_entity_list:
            target_file = bring.bring_file_from_s3(file_entity=target_entity)
            target_group_file_path_list.append(os.path(target_file))
        source_file = bring.bring_file_from_s3(file_entity=target_entity)
        source_file_path = os.path(source_file)
        
        ## TODO 이미지 그룹 딥페이크 기능 함수 구현 후 여기서 호출하여 기능 수행
        ## 하나의 이미지에서의 얼굴을 모든 그룹 이미지에 적용시킴..
        res_file_list = []
        for target_file_path in target_group_file_path_list:
            res_file = deepFake_image_func(target_img_path=target_file_path, source_img_path=source_file_path)
            res_file_list.append(res_file)
        
        ## s3에 처리된 파일 업로드
        res_file_entity_list = []
        for i in range(source_group_entity_list):
            res_file_entity = change_file_to_entity_and_store_at_s3(file=res_file_list[i], original_file_entity=target_group_entity_list[i])
            res_file_entity_list.append(res_file_entity)
        
        return res_file_entity_list


def execute_test(file_entity):
        
    res= {
        'file_ID' : uuid.uuid4(),
        'user_ID' : file_entity['user_ID'],
        'original_File_ID' : file_entity['file_ID'],
        'real_File_Name' : file_entity['real_File_Name'],
        'group_ID' : file_entity['group_ID'],
        'file_Extension' : file_entity['file_Extension'],
        'path' : file_entity['path']
    }
    
    return res


def image_func_test():
    
    target_file_path = 'D:/ImmersionProject/FinalProject/GolaBlur/API-AI/AI_API/deepFake/data/target_img.jpg'
    source_file_path = 'D:/ImmersionProject/FinalProject/GolaBlur/API-AI/AI_API/deepFake/data/source_img.png'
    
    res = deepFake_image_func(target_file_path, source_file_path)
    
    print(res)
    
    return

def video_func_test():
    
    target_file_path = 'D:/ImmersionProject/FinalProject/GolaBlur/API-AI/AI_API/deepFake/data/target_img.jpg'
    source_file_path = 'D:/ImmersionProject/FinalProject/GolaBlur/API-AI/AI_API/deepFake/data/source_video.mp4'
    
    res = deepFake_video_func(target_file_path, source_file_path)
    
    print(res)
    
    return

def group_images_func_test():
    
    
    return
