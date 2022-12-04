from flask import Flask, jsonify, request
import base64
import numpy as np
import cv2
import background
# sys.path.append("C:/Users/eorl6/Documents/golablur/AI_API")
# from delete import deleteController
app = Flask(__name__)
# np.set_printoptions(threshold=sys.maxsize)

@app.route('/delete/execute', methods=['GET','POST'])
def execute():
    print("받음")
    file_and_object_list = request.get_json()
    list = file_and_object_list.split(',')
    for i in range(len(list)):
        str = list[i]
        file = base64.b64decode(str[9:-1])
        jpg_arr = np.frombuffer(file, dtype=np.uint8)
        img = cv2.imdecode(jpg_arr, cv2.COLOR_BGR2GRAY)
        cv2.imshow("img",img)
        cv2.waitKey(delay=0)
        rgb = np.array(img, dtype=np.uint8)
        rgb = np.where(rgb == 255, 1 , 0)
        rgb = np.array(rgb, dtype=np.uint8)
        print(rgb.shape)
        model = background.diffusion()
        model.img(rgb)


    return "good"

@app.route('/test')
def test():
    return '200'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8884)