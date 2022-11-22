from flask import Flask
from deepFake.deepFake import *

app = Flask(__name__)


@app.route('/do')
def do_deepFake(file_and_object_list):
    
    return

@app.route('/test')
def test():
    return '200'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8880)