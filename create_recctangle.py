import cv2
import numpy as np
import os

LOW_COLOR = np.array([255, 128, 128])
HIGH_COLOR = np.array([255, 128, 128])

img = cv2.imread("data/Lenna.png")

# 画像の大きさを取得
height, width, channels = img.shape[:3]
print("width: " + str(width))  #256
print("height: " + str(height)) #256


#白色で塗りつぶす
base = cv2.rectangle(img, (0, 0), (width, height), (255, 255,255), thickness=-1)
base2 = base.copy()

#合成画像１を青色で塗りつぶす
#面積　60 * 80 = 4800 
src1 = cv2.rectangle(base, (140, 150), (200, 230), (255, 255, 0), thickness=-1)

#合成画像２を赤色で塗りつぶす
#面積　60 * 70 = 4200 
src2 = cv2.rectangle(base2, (120, 130), (180, 200), (255, 0, 255), thickness=-1)

dst = cv2.addWeighted(src1, 0.5, src2, 0.5, 0)

cv2.imwrite('data/opencv_draw_argument.png', dst)

# 色を抽出する
ex_img = cv2.inRange(dst,LOW_COLOR,HIGH_COLOR)

cv2.imwrite('data/roi.png', ex_img)

#重複領域の面積
whitePixels = cv2.countNonZero(ex_img)
print(whitePixels)

jaccard = 0.0
if whitePixels == 0:
    print("重複なし")
else:
    #Jaccard係数で重複度算出
    jaccard = print(whitePixels/(4800 + 4200 - (2* whitePixels)))

    