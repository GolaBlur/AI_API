import sys
sys.path.append("D:\ImmersionProject\FinalProject\GolaBlur\API-AI\AI_API")
# from AI_API.service import awsS3Service
from service.awsS3Service import *
import uuid

# from yolov5 import detect

class detection_execute:
    
    def image(file_entity):
        ## s3에서 처리할 파일 다운로드
        file = bring.bring_file_from_s3(file_entity=file_entity)
        
        ## TODO 기능 수행
        object_list = '기능수행!'
        
        ## s3에 탐지된 객체 업로드
        # object_entity_list = change_object_to_entity_and_store_at_s3(object_list=object_list, file_entity=file_entity)
        
        ## Test
        object_entity_list = execute_test(file_entity=file_entity)
        print(object_entity_list)
        ### 로컬 스토리지 초기화
        # initialization
        return object_entity_list
    
    def video():
        
        return


### TODO TEST
def execute_test(file_entity):
    object_list = [{
        'object_ID' : uuid.uuid4(),
        'file_ID' : file_entity['file_ID'],
        'user_ID' : file_entity['user_ID'],
        'object_Name' : 'ex',
        'file_Extension' : file_entity['file_Extension'],
        'path' : file_entity['path']
    },{
        'object_ID' : uuid.uuid4(),
        'file_ID' : file_entity['file_ID'],
        'user_ID' : file_entity['user_ID'],
        'object_Name' : 'ex',
        'file_Extension' : file_entity['file_Extension'],
        'path' : file_entity['path']
    },{
        'object_ID' : uuid.uuid4(),
        'file_ID' : file_entity['file_ID'],
        'user_ID' : file_entity['user_ID'],
        'object_Name' : 'ex',
        'file_Extension' : file_entity['file_Extension'],
        'path' : file_entity['path']
    }]
    
    ## 좌표는 없음
    
    return object_list



# class ex_detection:

#     def objects():
#         path = 'C:/Users/eorl6/Documents/golablur/car.jpg'
#         list = detect.run(source=path,weights='yolov5n6.pt', save_txt=True)
#         print(list)
#         for i in range(len(list)):
#             list[i][0] = names(list[i][0])
#         list.append(path)
#         return list



# from yolov5 import detect
#
# class ex_detection:
#     def objects():
#         list = detect.run(source='C:/Users/eorl6/Documents/golablur/car.jpg',weights='yolov5n6.pt', save_txt=True)
#         return list

#     def names(num):
#         num = int(num)
#         names={
#             0: "person",
#             1: "bicycle",
#             2: "car",
#             3: "motorcycle",
#             4: "airplane",
#             5: "bus",
#             6: "train",
#             7: "truck",
#             8: "boat",
#             9: "traffic light",
#             10: "fire hydrant",
#             11: "stop sign",
#             12: "parking meter",
#             13: "bench",
#             14: "bird",
#             15: "cat",
#             16: "dog",
#             17: "horse",
#             18: "sheep",
#             19: "cow",
#             20: "elephant",
#             21: "bear",
#             22: "zebra",
#             23: "giraffe",
#             24: "backpack",
#             25: "umbrella",
#             26: "handbag",
#             27: "tie",
#             28: "suitcase",
#             29: "frisbee",
#             30: "skis",
#             31: "snowboard",
#             32: "sports ball",
#             33: "kite",
#             34: "baseball bat",
#             35: "baseball glove",
#             36: "skateboard",
#             37: "surfboard",
#             38: "tennis racket",
#             39: "bottle",
#             40: "wine glass",
#             41: "cup",
#             42: "fork",
#             43: "knife",
#             44: "spoon",
#             45: "bowl",
#             46: "banana",
#             47: "apple",
#             48: "sandwich",
#             49: "orange",
#             50: "broccoli",
#             51: "carrot",
#             52: "hot dog",
#             53: "pizza",
#             54: "donut",
#             55: "cake",
#             56: "chair",
#             57: "couch",
#             58: "potted plant",
#             59: "bed",
#             60: "dining table",
#             61: "toilet",
#             62: "tv",
#             63: "laptop",
#             64: "mouse",
#             65: "remote",
#             66: "keyboard",
#             67: "cell phone",
#             68: "microwave",
#             69: "oven",
#             70: "toaster",
#             71: "sink",
#             72: "refrigerator",
#             73: "book",
#             74: "clock",
#             75: "vase",
#             76: "scissors",
#             77: "teddy bear",
#             78: "hair drier",
#             79: "toothbrush"
#         }
#         return str(names[num])