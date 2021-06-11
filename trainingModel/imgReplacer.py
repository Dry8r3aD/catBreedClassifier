import glob
import shutil
import os
import numpy as np

BASE_PATH = "C:\\Users\\dry8r3ad\\PycharmProjects\\catBreedClassifier\\data\\agumentation\\"

def main():
    breeds = os.listdir(BASE_PATH)

    for breed in breeds:
        breed_path = BASE_PATH + breed
        images = os.listdir(breed_path)

        for image in images:
            image_dir_path = breed_path + "\\" + image
            cnt = 0

            for src_file in glob.glob(image_dir_path + "\\*.jpg"):
                print(src_file)
                shutil.move(src_file, breed_path + "\\" + image + "_" + str(cnt) + ".jpg")
                cnt += 1

        l = [name for name in os.listdir(BASE_PATH + breed) if os.path.isdir(os.path.join(BASE_PATH + breed, name))]
        for d in l:
            os.rmdir(BASE_PATH + breed + "\\" + d)

main()
