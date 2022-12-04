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
    # file_and_object_list = request.get_json()
    # print(file_and_object_list)
    # list = file_and_object_list.split(',')
    img = None
    mask = None
    img_list = []
    # for i in range(len(list)):
    #     str = list[i]
    #     str = str.replace('"','')
    #     str = str.replace('}','')
    #     print(str[7:])
    #     file = base64.b64decode(str[7:])
    #     jpg_arr = np.frombuffer(file, dtype=np.uint8)
    #     if i ==1:
    #         img = cv2.imdecode(jpg_arr,0)
    #         print(img.shape)
    #     else:
    #         img = cv2.imdecode(jpg_arr,cv2.IMREAD_COLOR)

    #     unique, counts = np.unique(img, return_counts=True)
    #     print(dict(zip(unique, counts)))
        
    #     img_list.append(img)

        # rgb = np.array(img, dtype=np.uint8)
        # rgb = np.where(rgb == 255, 1 , 0)
        # rgb = np.array(rgb, dtype=np.uint8)
    img_list = ['C:/Users/eorl6/Documents/golablur/AI_API/resources/diffusion/mask/MASK1234.png','C:/Users/eorl6/Documents/golablur/AI_API/resources/diffusion/original/ORIGINAL1.png']
    model = background.diffusion()
    model.img(img_list)


    return "good"

@app.route('/test')
def test():
    return '200'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8884)