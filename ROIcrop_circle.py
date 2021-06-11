from pathlib import Path
import numpy as np
import cv2
import glob
import os


def crop_img(img, x, y, w, h, rad):
    img1 = img
    # height, width = img.shape
    centX = img.shape[0]//2
    centY = img.shape[1]//2
    mask = np.zeros((img.shape[0], img.shape[1]), np.int8)
    circle_img = cv2.circle(mask, (centX, centY), rad, (255, 255, 255), thickness=-1)
    masked_data = cv2.bitwise_and(img1, img1, mask=circle_img)
    dst = masked_data[y:(y+h), x:(x+w)]

    return dst

def Circlecrop():
    names = []
    destination_dir = r"C:\Users\MinJeong\Desktop\destination_dir"

    source_dir = r"C:\Users\MinJeong\Desktop\source_dir" + "/*.bmp"
    images = glob.glob(source_dir)
    cnt = 0

    for img in images:
        names.append(img)
        cnt += 1

        # print(names)
        # print(cv2.imread(images[0]).shape)
    print("%d image loading finished"%cnt)

    for img in images:
        src = cv2.imread(img)

        if src.shape[0] == 1835 and src.shape[1] == 1834:
            x = 67
            y = 67
            w = 1706  # 1065
            h = 1706

            src = cv2.imread(img)
            dst = crop_img(src, x, y, w, h, w//2)
            cv2.imwrite(f'{destination_dir}/{Path(img).name}', dst)
            # remove source image
            # try: os.remove(img)
            # except: pass

        else: continue

#                cnt += 1


if __name__ == '__main__':
    Circlecrop()