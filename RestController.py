### flask
from flask import Flask, jsonify, request

### Service
from service.AIService import *
# from service.awsS3Service import *


app = Flask(__name__)
# api = Api(app)

### TEST
@app.route('/test')
def test():
    return '200'


### Route

# input : FileObjectDTO
# output : FileEntity
@app.route('/process/deepFake/one/image', methods=['POST'])
def deepFakeOneImage():
    print("rest controller - deepFakeOneImage")
    FileObjectDTO = request.get_json()
    print(FileObjectDTO)
    return jsonify(DeepFake.image(FileObjectDTO))

# input : FileObjectDTO
# output : FileEntity
@app.route('/process/deepFake/one/video', methods=['POST'])
def deepFakeOneVideo():
    print("rest controller - deepFakeOneVideo")
    FileObjectDTO = request.get_json()
    print(FileObjectDTO)
    return jsonify(DeepFake.video(FileObjectDTO))

# input : FileObjectDTO
# output : FileEntity
@app.route('/process/delete/one/image', methods=['POST'])
def deleteOneImage():
    print("rest controller - deleteOneImage")
    FileObjectDTO = request.get_json()
    print(FileObjectDTO)
    return jsonify(Delete.image(FileObjectDTO))

# input : FileObjectDTO
# output : FileEntity
@app.route('/process/mosaic/one/image', methods=['POST'])
def mosaicOneImage():
    print("rest controller - mosaicOneImage")
    FileObjectDTO = request.get_json()
    print(FileObjectDTO)
    return jsonify(Mosaic.image(FileObjectDTO))

# input : FileObjectDTO
# output : FileEntity
@app.route('/process/mosaic/one/video', methods=['POST'])
def mosaicOneVideo():
    print("rest controller - mosaicOneVideo")
    FileObjectDTO = request.get_json()
    print(FileObjectDTO)
    return jsonify(Mosaic.video(FileObjectDTO))

# input : FileEntity
# output : List<ObjectEntity>
@app.route('/process/detection/image', methods=['POST'])
def detectionOneImage():
    print("rest controller - detectionOneImage")
    FileEntity = request.get_json()
    print(FileEntity)
    print(FileEntity['file_ID'])
    return jsonify(ObjectDetection.image(FileEntity))

# input : FileEntity
# output : List<ObjectEntity>
@app.route('/process/detection/video', methods=['POST'])
def detectionOneVideo():
    print("rest controller - detectionOneVideo")
    FileEntity = request.get_json()
    print(FileEntity)
    return jsonify(ObjectDetection.video(FileEntity))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)





# # TEST

# @app.route('/test/upload/image', methods=['POST'])
# def upload_image():
    
#     data = open('resources/file/upload/ttt.jpg', 'rb')
    
#     return tests3.test_upload_image(data)

# @app.route('/test/download/image', methods = ['POST'])
# def download_image():
    
#     tests3.test_download_image()
    
#     return '200'

# @app.route('/test/upload/video', methods = ['POST'])
# def upload_video():
    
#     data = open('resources/file/upload/yeye.mp4', 'rb')
    
#     tests3.test_upload_video(data)
    
#     return '200'

# @app.route('/test/download/video', methods = ['POST'])
# def download_video():
    
#     tests3.test_download_video()
    
#     return '200 '



