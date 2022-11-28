from flask import Flask, jsonify, request
import sys
# sys.path.append("D:\ImmersionProject\FinalProject\GolaBlur")
# import golablur
# sys.path.append("D:\ImmersionProject\FinalProject\GolaBlur\API-AI\AI_API")
# from ..service import useAPIService
from delete_execute import *
import cv2
import json
import base64

app = Flask(__name__)

# input : FileObjectDTO
# output : FileEntity

# @app.route('/delete/execute', methods=['GET','POST'])
# def execute():
#     list = request.get_json()
#     test(list)
#     return "isee"

# @app.route('/test')
# def test(list):
#     print(list)
#     path = list.pop()
#     print(list)
#     for i in range(len(list)):
#         xtl = list[i][1]
#         ytl = list[i][2]
#         xbr = list[i][3]
#         ybr = list[i][4]
#         img = golablur.Image(xtl, ytl, xbr, ybr,path)
#         img.show_box()
#         img.rm_bg()
#         # img.change_black()
#         # cv2.imshow('img',img)
#         # cv2.waitKey(delay=0)
#     # print(img.shape)
#     # img_str = str(base64.b64encode(cv2.imencode('.jpg', img)[1]).decode())
#     # img_dict = {'img':img_str}
#     # img_dict = json.dumps(img_dict)
#     # print(img_dict)
#     # useAPIService.send_api('8884','POST',img_dict)
#     return "true"

@app.route('/image/delete/execute', methods=['POST','GET'])
def image_delete_execute():
    print('image_delete_execute')
    req = request.get_json()
    print(req)
    res = delete_execute.image(file_entity= req['file'], object_entity_list= req['objectList'])
    return jsonify(res)


# @app.route('/video/delete/execute', methods=['POST','GET'])
# def video_delete_execute():
#     print('video_delete_execute')
#     req = request.get_json()
#     res = delete.video(req)
#     return jsonify(res)


# @app.route('/test')
# def test():
#     img = golablur.Image(381,158,381,29,'C:/Users/eorl6/Documents/golablur/car.jpg')
#     useAPIService.send_api('8884','POST',img.rm_bg())
#     return str(img.rm_bg())


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8881)