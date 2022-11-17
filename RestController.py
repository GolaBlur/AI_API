### flask
from flask import Flask 
### os
import os


### Service
from service.DeepFakerSerivce import *
from service.DeleteService import *
from service.MosaicService import *
from service.ObjectDetection import *

app = Flask(__name__)
# api = Api(app)


# TEST
from service.awsS3Service import *
@app.route('/test/iii', methods=['POST'])
def test():
    data = open('resources/file/upload/test.jpg','rb')
    return store.store_file_at_s3(test, data)

@app.route('/test/s3/list', methods = ['POST'])
def s3_list():
    tests3.get_s3_list()
    return '200'
### Route

# input : aiFunctionDTO
# output : FileEntity
@app.route('/process/deepFake/one/image', methods=['POST'])
def deepFakeOneImage():
    return DeepFake.image()

# input : aiFunctionDTO
# output : FileEntity
@app.route('/process/deepFake/one/video', methods=['POST'])
def deepFakeOneVideo():
    return DeepFake.video()

# input : aiFunctionDTO
# output : FileEntity
@app.route('/process/delete/one/image', methods=['POST'])
def deleteOneImage():
    return Delete.image()

# input : aiFunctionDTO
# output : FileEntity
@app.route('/process/mosaic/one/image', methods=['POST'])
def mosaicOneImage():
    return Mosaic.image()

# input : aiFunctionDTO
# output : FileEntity
@app.route('/process/mosaic/one/video', methods=['POST'])
def mosaicOneVideo():
    return Mosaic.video()

# input : FileEntity
# output : List<ObjectEntity>
@app.route('/process/detection', methods=['POST'])
def detection():
    return ObjectDetection.image()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)