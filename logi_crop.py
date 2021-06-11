 #-*- coding: utf-8 -*-
from pathlib import Path
import numpy as np
import cv2
import glob

def crop_img(img, x ,y, w, h):
    dst = img[y:y+h, x:x+w]
    return dst

def logi_crop():
    cnt = 0
    names = []
    source_dir = r"C:\Users\Minjeong\Desktop\2021-02-24"+"/*.bmp"
    destination_dir = r"C:\Users\Minjeong\Desktop\new logi_1"

    images = glob.glob(source_dir)

    # for img in images:
    #     names.append(img)

    # print(names)
    # print(cv2.imread(images[0]).shape)
    # print("image loading finished")

    for img in images:
        src = cv2.imread(img)

        # src = cv2.resize(src, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA) # resize

        x = 110
        y = 50
        w = 1100 # 1065
        h = 705

        dst = crop_img(src, x, y, w, h)
        # dst = cv2.resize(dst, None, fx=1, fy=1, interpolation=cv2.INTER_CUBIC) # 사이즈 원본으로 바꾸기 2048
        
        cv2.imwrite(f'{destination_dir}/Crop_{Path(img).name}.png', dst)

        cnt += 1


if __name__ == '__main__':
    logi_crop()