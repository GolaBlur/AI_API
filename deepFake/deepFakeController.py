from flask import Flask, jsonify, request
from deepFake_execute import *

app = Flask(__name__)

# input : {FileEntity,FileEntity}
# output : FileEntity


@app.route('/image/deepfake/execute', methods=['POST','GET'])
def image_deepfake_execute():
    print('image_deepfake_execute')
    req = request.get_json()
    ## TODO 이미지 딥페이크 구현 필요
    print(req)
    res = deepFake_execute.image(target_entity=req['target_file'], source_entity=req['source_file'])
    return jsonify(res)

@app.route('/video/deepfake/execute', methods=['POST','GET'])
def video_deepfake_execute():
    print('video_deepfake_execute')
    req = request.get_json()
    ## TODO 비디오 딥페이크 로직 설계 및 구현 필요
    res = deepFake_execute.video(target_entity=req['source_file'], source_entity=req['target_file'])
    return jsonify(res)

## input -> List<FileEntity> sourceFileEntityList
##          FileEntity targetFileEntity
@app.route('/group/images/deepfake/execute', methods=['POST', 'GET'])
def images_deepfake_execute():
    print('group_images_deepfake_execute')
    req = request.get_json()
    print(req)
    ## TODO 그룹 이미지 딥페이크 구현 필요
    res = deepFake_execute.group_images(source_group_entity_list=req['sourceFileEntityList'], target_entity=req['targetFileEntity'])
    return jsonify(res)


@app.route('/test/image', methods=['POST', 'GET'])
def image_test():
    image_func_test()
    return '200'

@app.route('/test/video', methods=['POST', 'GET'])
def video_test():
    video_func_test()
    return '200'

@app.route('/test/group/images', methods=['POST', 'GET'])
def group_images_test():
    group_images_func_test()
    return '200'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8880, threaded= True)