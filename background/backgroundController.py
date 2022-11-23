from flask import Flask, jsonify, request
import sys
sys.path.append("C:/Users/eorl6/Documents/golablur")
from diffusion import inpaint
# sys.path.append("C:/Users/eorl6/Documents/golablur/AI_API")
# from delete import deleteController
app = Flask(__name__)


@app.route('/delete/execute')
def execute():
    file_and_object_list = request.get_json()
    return

@app.route('/test')
def test():
    return '200'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8884)