from flask import Flask, jsonify, request
# import sys
# sys.path.append("C:/Users/eorl6/Documents/golablur")
# import golablur
# sys.path.append("C:/Users/eorl6/Documents/golablur/AI_API")
# from service import useAPIService
from delete import *

app = Flask(__name__)

# input : FileObjectDTO
# output : FileEntity


@app.route('/image/delete/execute', methods=['POST','GET'])
def image_delete_execute():
    print('image_delete_execute')
    req = request.get_json()
    res = delete.image(req)
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