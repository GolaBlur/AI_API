from flask import Flask, jsonify, request
import sys
sys.path.append("C:/Users/eorl6/Documents/golablur/")
from yolov5 import detect
from detection import *

app = Flask(__name__)

@app.route('/detection/execute')
def execute():
    file = request.get_json()
    return

@app.route('/test')
def test():
    result = ""
    list = ex_detection.objects()
    print(list)
    result +="탐지된 객체수 : "
    result += str(len(list)) + "\n"
    result += ex_detection.names(list[0][0])+" "
    result += ex_detection.names(list[1][0])
    return result
 
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8883)