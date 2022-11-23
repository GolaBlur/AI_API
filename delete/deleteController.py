from flask import Flask, jsonify, request
from delete.delete import *

app = Flask(__name__)


@app.route('/delete/execute')
def execute():
    file_and_object_list = request.get_json()
    return

@app.route('/test')
def test():
    return '200'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8881)