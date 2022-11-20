### flask
from flask import Flask 

### Service
from service.AIService import *
# from service.awsS3Service import *


app = Flask(__name__)
# api = Api(app)



### Route

# input : AIFunctionDTO
# output : FileEntity
@app.route('/process/deepFake/one/image', methods=['POST'])
def deepFakeOneImage(AIFunctionDTO):
    return DeepFake.image(AIFunctionDTO)

# input : AIFunctionDTO
# output : FileEntity
@app.route('/process/deepFake/one/video', methods=['POST'])
def deepFakeOneVideo(AIFunctionDTO):
    return DeepFake.video(AIFunctionDTO)

# input : AIFunctionDTO
# output : FileEntity
@app.route('/process/delete/one/image', methods=['POST'])
def deleteOneImage(AIFunctionDTO):
    return Delete.image(AIFunctionDTO)

# input : AIFunctionDTO
# output : FileEntity
@app.route('/process/mosaic/one/image', methods=['POST'])
def mosaicOneImage(AIFunctionDTO):
    return Mosaic.image(AIFunctionDTO)

# input : AIFunctionDTO
# output : FileEntity
@app.route('/process/mosaic/one/video', methods=['POST'])
def mosaicOneVideo(AIFunctionDTO):
    return Mosaic.video(AIFunctionDTO)

# input : FileEntity
# output : List<ObjectEntity>
@app.route('/process/detection/image', methods=['POST'])
def detectionOneImage(FileEntity):
    return ObjectDetection.image(FileEntity)

# input : FileEntity
# output : List<ObjectEntity>
@app.route('/process/detection/video', methods=['POST'])
def detectionOneVideo(FileEntity):
    return ObjectDetection.video(FileEntity)


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



