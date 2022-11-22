from configuration.config import *

import requests
import json


def send_api(api_port , method, body):
    
    url = 'localhost:'+api_port+'/do'
    
    headers = {'Content-Type' : 'application/json', 'charset' : 'UTF-8', 'Accept' : '*/*'}
    
    try:
        if method == 'GET':
            response = requests.get(url, headers= headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent='\t'))
        print("response status %r" %response.status_code)
        print("response text %r" %response.text)
    except Exception as ex:
        print(ex)
    
    return response


class useImageAPI:
    
    def deepFake(file_and_object_list):
        return send_api(api_port=deepFake_port , method='POST' , body=file_and_object_list)
    
    def delete(file_and_object_list):
        return send_api(api_port=delete_port , method='POST' , body=file_and_object_list)
    
    def mosaic(file_and_object_list):
        return send_api(api_port=mosaic_port , method='POST' , body=file_and_object_list)
    
    def detection(file):        
        return send_api(api_port=detection_port , method='POST' , body=file)

class useVideoAPI:
    
    def deepFake(file_and_object_list):        
        return send_api(api_port=deepFake_port , method='POST' , body=file_and_object_list)
    
    def delete(file_and_object_list):
        return send_api(api_port=delete_port , method='POST' , body=file_and_object_list)
    
    def mosaic(file_and_object_list):
        return send_api(api_port=mosaic_port , method='POST' , body=file_and_object_list)
    
    def detection(file):
        return send_api(api_port=detection_port , method='POST' , body=file)
