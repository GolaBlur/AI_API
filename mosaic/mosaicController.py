from flask import Flask
from mosaic.mosaic import *

app = Flask(__name__)


@app.route('/do')
def do_mosaic(file_and_object_list):
    
    return

@app.route('/test')
def test():
    return '200'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8882)