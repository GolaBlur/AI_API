from ..configuration.config import *

import json
import requests

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
