from flask import Flask, jsonify, request
import sys
sys.path.append("C:/Users/eorl6/Documents/golablur")
import golablur
sys.path.append("C:/Users/eorl6/Documents/golablur/AI_API")
from service import useAPIService
from delete import *
import cv2
import json
import base64
app = Flask(__name__)


@app.route('/delete/execute', methods=['GET','POST'])
def execute():
    list = request.get_json()
    test(list)
    return "isee"

@app.route('/test')
def test(list):
    print(list)
    path = list.pop()
    print(list)
    for i in range(len(list)):
        xtl = list[i][1]
        ytl = list[i][2]
        xbr = list[i][3]
        ybr = list[i][4]
        img = golablur.Image(xtl, ytl, xbr, ybr,path)
        img.show_box()
        img.rm_bg()
        # img.change_black()
        # cv2.imshow('img',img)
        # cv2.waitKey(delay=0)
    # print(img.shape)
    # img_str = str(base64.b64encode(cv2.imencode('.jpg', img)[1]).decode())
    # img_dict = {'img':img_str}
    # img_dict = json.dumps(img_dict)
    # print(img_dict)
    # useAPIService.send_api('8884','POST',img_dict)
    return "true"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8881)