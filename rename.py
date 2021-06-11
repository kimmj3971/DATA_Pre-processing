# -*- coding: utf-8 -*-
from pathlib import Path
# import numpy as np
import cv2
import glob

def Rename():
    cnt = 0
    names = []
    source_dir = r"C:\Users\MinJeong\Desktop\Source_dir" + "/*.jpg"
    destination_dir = r"C:\Users\MinJeong\Desktop\directory1\destination_Dir"

    images = glob.glob(source_dir)

    for img in images:
        src = cv2.imread(img)
        cv2.imwrite(f'{destination_dir}/Aug_{Path(img).name}', src)

    print("finished")

if __name__ == '__main__':
    Rename()
