from flask import Flask, jsonify, request
from detection.detection import *

app = Flask(__name__)


@app.route('/detection/execute')
def execute():
    file = request.get_json()
    return

@app.route('/test')
def test():
    return '200'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8883)