




######## TEST ###########

## 객체 파일을 모자이크함.

## cv2 사용해서 모자이크된 객체를 원래 객체 위치에 삽입해줌.

import cv2
import numpy as np

### 객체 좌표값
xtl = 70
xbr = 268
ytl = 8
ybr = 188


obj = cv2.imread('D:/delete.png')
img = cv2.imread('D:/dog.jpg')

cv2.imshow('obj', obj)
cv2.imshow('img', img)
cv2.imshow('img-obj', img[ytl:ybr,xtl:xbr])

### 검은 배경만 흰색으로

## 외곽선 검출
gray = cv2.cvtColor(obj, cv2.COLOR_GRAY2BGR)

contours, hierarchy = cv2.findContours(image=gray,
                                       mode=cv2.RETR_EXTERNAL,
                                       method=cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    obj_contour = cv2.drawContours(obj, [contour], -1, (0,0,255), 2)

cv2.imshow('obj_contour', obj_contour)

## 검은 배경 외에는 모두 흰색으로

xor = cv2.bitwise_and()





# img = cv2.imread('D:/delete.jpg')

# # cv2.imshow('image',img)

# # subimg = img[100:200,200:300]

# # cv2.imshow('subimg', subimg)

# # img[200:300, 100:200] = subimg

# # cv2.imshow('res', img)

# # def mosaic(src, ratio=0.1):
# #     small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
# #     return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

# # # res_01 = mosaic(del_img)
# res_01 = cv2.blur(img, (20,20))
# cv2.imshow('res', res_01)

# print(res_01.shape)

# # _, test_01 = cv2.threshold(img[:,:,3], 1, 255, cv2.THRESH_BINARY)
# # cv2.imshow('test',test_01)
# cv2.imshow('res',res_01)

# b, g, r = cv2.split(img)

# b = np.where(b < 10, 255, b)
# g = np.where(g < 10, 255, g)
# r = np.where(r < 10, 255, r)


# res_02 = cv2.merge([b,g,r])
# cv2.imshow('res02',res_02)

# res_03 = cv2.blur(res_02,(20,20))
# cv2.imshow('res3',res_03)
# cv2.imshow('img', img)

# dog_img = cv2.imread('D:/dog.jpg')
# # ### 아쉬운 결과물
# ######## ytl,ybr,xtl,xbr
# # dog_img[8:188, 70:268] = cv2.bitwise_xor(dog_img[8:188, 70:268],cv2.bitwise_xor(img,res_01))
# # dog_img[8:188, 70:268] = cv2.bitwise_xor(dog_img[8:188, 70:268],cv2.bitwise_xor(img,res_01))
# # dog_img[7:167, 53:280] = cv2.bitwise_xor(dog_img[7:167, 53:280],cv2.bitwise_xor(img,res_01))


# # rr = cv2.bitwise_or(res_01, test_01)
# # cv2.imshow('rr',rr)

# print(dog_img.shape)

# cv2.imshow('resres', dog_img)
# cv2.imshow('ddd',dog_img[7:167, 53:280])
# # dog_img[8:188, 70:268] = cv2.blur(dog_img[8:188, 70:268], (20,20))
# dog_img[7:167, 53:280] = cv2.blur(dog_img[7:167, 53:280], (20,20))
# cv2.imshow('blur', dog_img)

# unique, counts = np.unique(res_01, return_counts=True)
# print(dict(zip(unique, counts)))

# # res_03 = np.where(res_03 == 0, 255, res_03)
# # arr = np.where(arr == 255, 0, arr)

# cv2.imshow('where', res_03)

# dog_img[8:188, 70:268] = cv2.bitwise_xor(res_02,cv2.bitwise_and(img,dog_img[8:188, 70:268]))
# cv2.imshow('iii', cv2.bitwise_xor(res_01,img))
# cv2.imshow('ob_blur', dog_img)

# img

cv2.waitKey(0)







