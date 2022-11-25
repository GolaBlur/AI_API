from flask import Flask, jsonify, request
import sys
sys.path.append("C:/Users/eorl6/Documents/golablur/")
from yolov5 import detect
from detection import *
sys.path.append("C:/Users/eorl6/Documents/golablur/AI_API")
from service import useAPIService
app = Flask(__name__)

@app.route('/detection/execute')
def execute():
    file = request.get_json()
    return

@app.route('/test')
def test():
    list = ex_detection.objects()
    print(list)
    useAPIService.send_api('8881','POST',list)
    return "true"
 
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8883)