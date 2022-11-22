
from service.awsS3Service import *
from service.useAPIService import *
import os
import uuid

### 파일 정보를 통해 파일 다운로드
def bring_file_object_process(entity_of_file_and_object):
    ### 반환할 딕셔너리
    file_object = {}
    
    ### 이미지 가져와 딕셔너리에 저장
    file_object['file'] = bring.bring_file_from_s3(file_entity = entity_of_file_and_object.file)
    
    ### 처리할 객체 리스트 가져와 딕셔너리에 저장
    file_object['object_list'] = bring.bring_object_from_s3(object_list = entity_of_file_and_object.processingObjectList)
    
    return file_object


### FileEntity 형식으로 파일 정보를 추출
def change_file_to_file_entity(file, original_file_entity):
    file_entity = {}
    
    file_entity['File_ID'] = uuid.uuid4()
    file_entity['User_ID'] = original_file_entity.User_ID
    file_entity['Original_File_ID'] = original_file_entity.File_ID
    file_entity['Real_File_Name'] = original_file_entity.Real_File_Name
    file_entity['Group_ID'] = original_file_entity.Group_ID
    file_entity['File_Extension'] = os.path.splitext(file.name)[1]
    file_entity['Path'] = original_file_entity.Path[len(original_file_entity.Path)
                                                    -len(original_file_entity.File_ID + original_file_entity.File_Extension)
                                                    :] + 'result/' + file_entity.get('File_ID') + file_entity.get('File_Extension')
    
    return file_entity

### ObjectEntity의 리스트 형식으로 파일 정보를 추출
def change_object_to_object_entity(object_list, file_entity):
    object_entity_list = []
    for object_file in object_list:
        object_entity = {}
        
        object_entity['Object_ID'] = uuid.uuid4()
        object_entity['Original_File_ID'] = file_entity.Original_File_ID
        object_entity['User_ID'] = file_entity.User_ID
        object_entity['File_Extension'] = os.path.splitext(object_file.name)[1]
        object_entity['Path'] = file_entity.Path[len(file_entity.Path)
                                                    -len(file_entity.File_ID + file_entity.File_Extension)
                                                    :] + 'object/' +object_entity.get('Object_ID') + object_extension
        
        object_entity_list.append(object_entity)
    return object_entity_list



class DeepFake:
    
    def image(entity_of_file_and_object):
        # s3에서 데이터 가져와 딕셔너리에 담기
        real_file_and_object = bring_file_object_process(entity_of_file_and_object)
        # 기능 수행
        file = useImageAPI.deepFake(real_file_and_object)
        # DB에 저장할 형태로 spring server로 반환
        file_entity = change_file_to_file_entity(file, entity_of_file_and_object.file)
        # s3에 데이터 저장
        store.store_file_at_s3(file_entity = file_entity , file = file) 
        return file_entity
    
    def video(entity_of_file_and_object):
        # s3에서 데이터 가져와 딕셔너리에 담기
        real_file_and_object = bring_file_object_process(entity_of_file_and_object)
        # 기능 수행
        file = useVideoAPI.deepFake(real_file_and_object)
        # DB에 저장할 형태로 spring server로 반환
        file_entity = change_file_to_file_entity(file, entity_of_file_and_object.file)
        # s3에 데이터 저장
        store.store_file_at_s3(file_entity = file_entity , file = file) 
        return file_entity



class Delete:
    
    def image(entity_of_file_and_object):
        # s3에서 데이터 가져와 딕셔너리에 담기
        real_file_and_object = bring_file_object_process(entity_of_file_and_object)
        # 기능 수행
        file = useImageAPI.delete(real_file_and_object)
        # DB에 저장할 형태로 spring server로 반환
        file_entity = change_file_to_file_entity(file, entity_of_file_and_object.file)
        # s3에 데이터 저장
        store.store_file_at_s3(file_entity = file_entity , file = file) 
        return file_entity
    
    def video(entity_of_file_and_object):
        # s3에서 데이터 가져와 딕셔너리에 담기
        real_file_and_object = bring_file_object_process(entity_of_file_and_object)
        # 기능 수행
        file = useVideoAPI.delete(real_file_and_object)
        # DB에 저장할 형태로 spring server로 반환
        file_entity = change_file_to_file_entity(file, entity_of_file_and_object.file)
        # s3에 데이터 저장
        store.store_file_at_s3(file_entity = file_entity , file = file) 
        return file_entity




class Mosaic:
    
    def image(entity_of_file_and_object):
        # s3에서 데이터 가져와 딕셔너리에 담기
        real_file_and_object = bring_file_object_process(entity_of_file_and_object)
        # 기능 수행
        file = useImageAPI.mosaic(real_file_and_object)
        # DB에 저장할 형태로 spring server로 반환
        file_entity = change_file_to_file_entity(file, entity_of_file_and_object.file)
        # s3에 데이터 저장
        store.store_file_at_s3(file_entity = file_entity , file = file) 
        return file_entity
    
    def video(entity_of_file_and_object):
        # s3에서 데이터 가져와 딕셔너리에 담기
        real_file_and_object = bring_file_object_process(entity_of_file_and_object)
        # 기능 수행
        file = useVideoAPI.mosaic(real_file_and_object)
        # DB에 저장할 형태로 spring server로 반환
        file_entity = change_file_to_file_entity(file, entity_of_file_and_object.file)
        # s3에 데이터 저장
        store.store_file_at_s3(file_entity = file_entity , file = file) 
        return file_entity



class ObjectDetection:
    
    def image(entity_of_file):
        print("hihihihihi")
        # s3에서 데이터 가져오기
        file = bring.bring_file_from_s3(entity_of_file)
        # 기능 수행
        object_list = useImageAPI.detection(file)
        # DB에 저장할 형태로 spring server로 반환
        object_entity_list = change_object_to_object_entity(object_list, entity_of_file)
        # s3에 데이터 저장
        store.store_object_at_s3(object_entity_list = object_entity_list, object_list = object_list)
        return object_entity_list
    
    def video(entity_of_file):
        # s3에서 데이터 가져오기
        file = bring.bring_file_from_s3(entity_of_file)
        # 기능 수행
        object_list = useVideoAPI.detection(file)
        # DB에 저장할 형태로 spring server로 반환
        object_entity_list = change_object_to_object_entity(object_list)
        # s3에 데이터 저장
        store.store_object_at_s3(object_entity_list = object_entity_list, object_list = object_list)
        return object_entity_list