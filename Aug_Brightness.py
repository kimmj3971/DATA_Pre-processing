# -*- coding: utf-8 -*-
from pathlib import Path
import numpy as np
import cv2
import random as rd
import glob

def Aug_bright():
    cnt = 0
    names = []
    source_dir = r"C:\Users\MinJeong\Desktop\512x384" + "/*.jpg"
    destination_dir = r"C:\Users\MinJeong\Desktop\Aug_512x384"

    images = glob.glob(source_dir)

    for img in images:
        names.append(img)

    print("image loading finished")

    for img in images:
        src = cv2.imread(img)
        # val = rd.randrange(30, 81)
        val = 20
        array = np.full(src.shape, (val, val, val), dtype=np.uint8)

        dst = cv2.subtract(src, array)

        # if val%2 == 0:
        #     dst = cv2.add(src, array)
        #     dst = cv2.add(dst, val//3)
        # else:
        #     dst = cv2.subtract(src, array)
        #     dst = cv2.subtract(dst, val//3)

        cv2.imwrite(f'{destination_dir}/Aug_{Path(img).name}', dst)

        cnt += 1

    print("finished")
    print(dst.shape)

if __name__ == '__main__':
    Aug_bright()
