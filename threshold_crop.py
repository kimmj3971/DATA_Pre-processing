import glob
import pandas as pd
import shutil

def func1():
    names1 = []
    names2 = []
    tmp = []

    cnt = 0

    destination_dir = r"C:\Users\user\Desktop\dsr_dir"
    source_dir1 = r"C:\Users\user\Desktop\source\sample(1)" + "/*.bmp"
    source_dir2 = r"C:\Users\user\Desktop\source\sample(2)" + "/*.bmp"

    images1 = glob.glob(source_dir1)
    images2 = glob.glob(source_dir2)

    for img in images1:
        names1.append(img[49:])
        tmp.append(img)

    for img in images2:
        names2.append(img[42:])

    print("image loading finished")

    for i in range(len(names1)):
        for j in range(len(names2)):
            if names2[j] in names1[i]:
                cnt+=1
                break
            cnt = 0
        if cnt == 0:
            print(names1[i])
            shutil.copy2(tmp[i], destination_dir)


if __name__ == '__main__':
    func1()
