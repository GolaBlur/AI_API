from flask import Flask
from detection.detection import *

app = Flask(__name__)


@app.route('/do')
def do_detection(file):
    
    return

@app.route('/test')
def test():
    return '200'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8883)