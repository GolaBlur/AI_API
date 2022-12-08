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
    res = deepFake_execute.image(target_entity=req['target'], source_entity=req['source'])
    return jsonify(res)

@app.route('/video/deepfake/execute', methods=['POST','GET'])
def video_deepfake_execute():
    print('video_deepfake_execute')
    req = request.get_json()
    ## TODO 비디오 딥페이크 로직 설계 및 구현 필요
    res = deepFake_execute.video(target_entity=req['target'], source_entity=req['source'])
    return jsonify(res)

@app.route('/group/images/deepfake/execute', methods=['POST', 'GET'])
def images_deepfake_execute():
    print('group_images_deepfake_execute')
    req = request.get_json()
    ## TODO 이미지 딥페이크 구현 필요
    res = deepFake_execute.groupt_images(target_group_entity_list=req['group'], source_entity=req['source'])
    return jsonify(res)


@app.route('/test')
def test():
    return '200'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8880)