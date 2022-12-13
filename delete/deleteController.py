from flask import Flask, jsonify, request
import sys
sys.path.append("C:/Users/eorl6/Documents/golablur")
import golablur
sys.path.append("C:/Users/eorl6/Documents/golablur/AI_API")
from service import useAPIService
from delete_execute import *
from time import sleep
import math
import cv2
import json
import base64
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

# input : FileObjectDTO
# output : FileEntity

@app.route('/delete/execute', methods=['GET','POST'])
def execute():
    list = request.get_json()
    obj_list = test(list)
    print("요청받고 보냄")
    return jsonify(obj_list)

@app.route('/test')
def test(list):
    # print(list)
    path = list.pop()


    obj_path = []

    img = None
    for i in range(len(list)):
        w,h,c = cv2.imread(path).shape
        xtl = math.ceil(list[i][1] + (w - list[i][1])/10)
        ytl = math.ceil(list[i][2] + (h - list[i][2])/10)
        xbr = math.ceil(list[i][3] + (w - list[i][3])/10)
        ybr = math.ceil(list[i][4] + (h - list[i][4])/10)
        img = golablur.Image(xtl, ytl, xbr, ybr,list[i][0],path)
        img.show_box()
        obj_path.append(img.rm_bg())
        img, path = img.change_black()
        print("================mask생성=========================")
        print(path)
        obj_path.append(path)
    # print(obj_path)
    # print(masks)
    
    print("=================================================")
    return obj_path

@app.route('/image/delete/execute', methods=['POST','GET'])
def image_delete_execute():
    print('image_delete_execute')
    print('시간지연중...')
    sleep(1)
    req = request.get_json()
    res = delete_execute.image(req['file'],req['objectList'])
    result = res.json()
    return result

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8881, threaded=True)