# -*-coding:utf-8-*-
import cv2
import numpy as np
import os

"""
이 스크립트는 기본적으로 수집한 원본 데이터를 기반으로 데이터 증가 작업을 수행하여
딥러닝 모델이 학습 할 수 있는 데이터셋을 늘리기 위한 스크립트이다.
openCV 라이브러리를 직접 사용하여 이미지 수정 및 저장을 하였으나, 나중에 찾아보니
Keras 에서는 ImageGenerator를 사용해서 유사한 작업을 할 수 있다고 한다... ㅎ
"""

TS_PATH = "C:\\Users\\dry8r3ad\\PycharmProjects\\catBreedClassifier\\data\\"
TS_ORIG_PATH = TS_PATH + "original\\"
TS_MODI_PATH = TS_PATH + "argumentation\\"

original_file_list = os.listdir(TS_ORIG_PATH)

blur_ks_list = [3, 5]
gaussian_std_list = [5, 10, 15, 20]
translation_list = [5, 10]
rotation_list = [-10, -5, 5, 10]


def blur_img(img, blur_ks):
    return cv2.blur(img, (blur_ks, blur_ks))


def gaussian_img(img, std):
    mean = 0
    row, col, ch = img.shape
    gauss = np.random.normal(mean, std, (row, col, ch))
    img = img + gauss

    return img


def translate_img(img, trans):
    row, col = img.shape[:2]
    m = np.float32([[1, 0, trans], [0, 1, trans]])

    return cv2.warpAffine(img, m, (col, row))


def rotate_img(img, rotate):
    row, col = img.shape[:2]
    m = cv2.getRotationMatrix2D((col / 2, row / 2), rotate, 1)

    return cv2.warpAffine(img, m, (col, row))


def data_arg(orig_file, argumentation_dir_path, original_dir_path):
    idx = 0
    print(original_dir_path + orig_file)
    if not cv2.haveImageReader(original_dir_path + orig_file):
        print("Invalid file(non-processable) was entered (filename:" + orig_file + "). Skipping")
        return

    img = cv2.imread(original_dir_path + orig_file)

    working_path = argumentation_dir_path + orig_file
    if not os.path.exists(working_path):
        os.mkdir(working_path)

    for blur_ks in blur_ks_list:
        img = blur_img(img, blur_ks)

        for gaussian_std in gaussian_std_list:
            img = gaussian_img(img, gaussian_std)

            for trans in translation_list:
                img = translate_img(img, trans)

                for rotate in rotation_list:
                    img = rotate_img(img, rotate)

                    filename = str(idx) + ".jpg"
                    cv2.imwrite(os.path.join(working_path, filename), img)
                    idx += 1
                    img = cv2.imread(original_dir_path + orig_file)
    return


def check_exclude_breed(breed):
    done_list = ["Abyssinian", "American Bobtail", "American Curl", "American Shorthair",
                 "American Wirehair","Applehead Siamese", "Balinese", "Bengal", "Birman", "Bombay",
                 "British Shorthair", "Burmese", "Burmilla", "Calico", "Canadian Hairless",
                 "Chartreux", "Chausie", "Chinchilla", "Cornish Rex", "Cymric", "Devon Rex",
                 "Dilute Calico", "Dilute Tortoiseshell", "Domestic Long Hair", "Domestic Medium Hair",
                 "Domestic Short Hair", "Egyptian Mau", "Exotic Shorthair", "Extra-Toes Cat - Hemingway Polydactyl",
                 "Havana", "Himalayan", "Japanese Bobtail", "Javanese", "Korat", "LaPerm", "Maine Coon",
                 "Manx", "Munchkin", "Nebelung", "Norwegian Forest Cat", "Ocicat", "Oriental Long Hair",
                 "Oriental Short Hair", "Oriental Tabby", "Persian", "Pixiebob", "Ragamuffin", "Ragdoll",
                 "Russian Blue", "Scottish Fold", "Selkirk Rex", "Siamese", "Siberian", "Silver",
                 "Singapura", "Snowshoe", "Somali", "Sphynx - Hairless Cat", "Tabby"]
    exclude_list = ["York Chocolate", "Chinchilla", "Canadian Hairless", "Burmilla", "LaPerm",
                    "Cymric", "American Wirehair", "Singapura", "Chausie", "Javanese", "Somali",
                    "Oriental Long Hair", "Korat", "Selkirk Rex", "Chartreux", "Silver",
                    "Domestic Long Hair", "Domestic Medium Hair", "Domestic Short Hair"]

    if breed in done_list:
        return True

    if breed in exclude_list:
        return True

    return False


def main():
    original_file_list.sort()

    for breed in original_file_list:
        if check_exclude_breed(breed):
            continue

        print("Data Argumentation: " + breed)

        working_breed_dir = TS_MODI_PATH + breed
        if not os.path.exists(working_breed_dir):
            os.mkdir(working_breed_dir)

        original_dir_path = (TS_ORIG_PATH + breed)
        for img_file in os.listdir(original_dir_path):
            data_arg(img_file, working_breed_dir + "\\", original_dir_path + "\\")


if __name__ == "__main__":
    main()
