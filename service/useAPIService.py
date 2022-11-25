from configuration.config import *

import json
import requests
import datetime


def json_default(value):
  if isinstance(value, datetime.date):
    return value.strftime('%Y-%m-%d')
  raise TypeError('not JSON serializable')

def send_api(url , method, body):
    print("send_api")
    
    
    headers = {'Content-Type' : 'application/json', 'charset' : 'UTF-8', 'Accept' : '*/*'}
    
    data = {}
    data['file'] = body
    
    
    try:
        if method == 'GET':
            response = requests.get(url, headers= headers)
        elif method == 'POST':
            data = json.dumps(body, ensure_ascii=False, indent='\t', default=json_default)
            print(data)
            response = requests.post(url, headers=headers, data=data)
        print("response status %r" %response.status_code)
        print("response json %r" %response.json())
    except Exception as ex:
        print(ex)
    
    return response.json()


# class useImageAPI:
    
#     def deepFake(file_and_object_entity_list):
#         print("useImageAPI - deepFake")
#         return send_api(url='http://localhost:'+ deepFake_port +'/deepFake/execute' , method='POST' , body=file_and_object_entity_list)
    
#     def delete(file_and_object_entity_list):
#         print("useImageAPI - delete")
#         return send_api(url='http://localhost:'+ delete_port +'/delete/execute' , method='POST' , body=file_and_object_entity_list)
    
#     def mosaic(file_and_object_entity_list):
#         print("useImageAPI - mosaic")
#         return send_api(url='http://localhost:'+ mosaic_port +'/mosaic/execute' , method='POST' , body=file_and_object_entity_list)
    
#     def detection(file_entity):        
#         print("useImageAPI - detection")
#         return send_api(url='http://localhost:'+ detection_port +'/detection/execute' , method='POST' ,  body=file_entity)

# class useVideoAPI:
    
#     def deepFake(file_and_object_entity_list):
#         print("useVideoAPI - deepFake")        
#         return send_api(url='http://localhost:'+ deepFake_port +'/deepFake/execute' , method='POST' , body=file_and_object_entity_list)
    
#     def delete(file_and_object_entity_list):
#         print("useImageAPI - delete")
#         return send_api(url='http://localhost:'+ delete_port +'/delete/execute' , method='POST' ,  body=file_and_object_entity_list)
    
#     def mosaic(file_and_object_entity_list):
#         print("useImageAPI - mosaic")
#         return send_api(url='http://localhost:'+ mosaic_port +'/mosaic/execute' , method='POST' , body=file_and_object_entity_list)
    
#     def detection(file_entity):
#         print("useImageAPI - detection")
#         return send_api(url='http://localhost:'+ detection_port +'/detection/execute' , method='POST' , body=file_entity)
