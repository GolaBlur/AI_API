import sys
sys.path.append("C:/Users/eorl6/Documents/golablur/AI_API")
from service import useAPIService
from service.awsS3Service import *
import cv2
sys.path.append("C:/Users/eorl6/Documents/golablur")
import golablur
import numpy as np
import uuid
import json

class delete_execute:
    
    def image(file_entity, object_entity_list):
        print('- delete execute image')
        # print('======================image 들어옴======================')
        ## s3에서 처리할 파일 다운로드
        file = bring.bring_file_from_s3(file_entity=file_entity)

        object_list = bring.bring_object_from_s3(object_entity_list=object_entity_list)
        ### 객체의 좌표값 추출
        coordinate = get_object_coordinate(object_entity_list=object_entity_list)
        # print("file:",file.name)
        # print("object_list:",object_list)
        # print("coordinate:",coordinate)
        ## TODO 기능 수행
        mask_list = []
        for mask in object_list:
            mask_list.append(mask.name)
        print(mask_list)
        res_file_entity = delete_object(file.name,mask_list,coordinate[0],file_entity)
        
        ## s3에 처리된 파일 업로드
        # res_file_entity = change_file_to_entity_and_store_at_s3(file=res_file, original_file_entity=file_entity)
        
        ### Test  -  return  FileEntity
        # res_file_entity = execute_test(file_entity=file_entity)
        
        return res_file_entity


def execute_test(file_entity):
        
    res = {
        'file_ID' : file_entity['file_ID'],
        'user_ID' : file_entity['user_ID'],
        'original_File_ID' : file_entity['file_ID'],
        'real_File_ID' : file_entity['real_File_ID'],
        'group_ID' : file_entity['group_ID'],
        'file_Extension' : file_entity['file_Extension'],
        'path' : file_entity['path']
    }
    
    return res


def delete_object(file_path, mask_path, xyxy,entity):

    img = golablur.Image(int(xyxy['xtl']),int(xyxy['ytl']),int(xyxy['xbr']),int(xyxy['ybr']),'obj',file_path)
    img.m_path = mask_path
    print("===================mask path 받음================")
    print(mask_path)

    mask = cv2.imread(mask_path[0])
    if 1 < len(mask_path):
        for i in range(len(mask_path)):

            img = cv2.imread(mask_path[i+1])

            unique, counts = np.unique(mask, return_counts=True)
            print(dict(zip(unique, counts)))
            unique, counts = np.unique(img, return_counts=True)
            print(dict(zip(unique, counts)))

            mask = cv2.multiply(mask,img)

            cv2.imshow('mask.png',mask)
            cv2.waitKey(0)
            

    # lista, mask_path = img.change_black()
    original = cv2.imread(img.path)
    original = cv2.multiply(original,mask)
    cv2.imshow('ORIGINAL.png',original)
    cv2.waitKey(0)

    cv2.imwrite('ORIGINAL.png',original)
    cv2.imwrite('mask.png',mask)


    path = 'C:/Users/eorl6/Documents/golablur/AI_API/delete/'
    original = path+'ORIGINAL.png'
    mask = path+'mask.png'
    dict = {
        'original':original,
        'mask':mask,
        'entity':entity
    }

    # return useAPIService.send_api('http://localhost:8884/delete/execute','POST',dict)