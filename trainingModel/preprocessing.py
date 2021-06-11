from PIL import Image
import os, glob
import numpy as np
from sklearn.model_selection import train_test_split

"""
이미지 전처리 작업
agumentation 작업을 끝으로 학습/테스트에 사용할 데이터를 모두 모았고,
이제 이 데이터들을 행렬형태로 저장하여 모델에 학습시킬 수 있게 해주어야한다.
numpy의 ndarray로 변환을 할건데, 이 과정에서 몇가지 이미지 전처리를 한다.
1. 크기 조정 -> 64 X 64 X 3(RGB)
2. (TODO) RGB에서 RGB의 평균값을 빼주면 더 높은 성능이 나온다고 한다. 나중에 해보는걸로...

전처리가 끝나면 npy 형식으로 저장하고, 이러면 추후 학습 시 바로 사용이 가능하다. 
"""

DATA_PATH = "C:\\Users\\dry8r3ad\\PycharmProjects\\catBreedClassifier\\data\\original\\"
categories = ["Abyssinian", "American Bobtail", "American Curl", "American Shorthair", "Applehead Siamese",
   "Balinese", "Bengal", "Birman", "Bombay", "British Shorthair", "Burmese", "Calico", "Cornish Rex",
   "Devon Rex", "Dilute Calico", "Dilute Tortoiseshell", "Egyptian Mau", "Exotic Shorthair",
   "Extra-Toes Cat - Hemingway Polydactyl", "Havana", "Himalayan", "Japanese Bobtail", "Maine Coon",
   "Manx", "Munchkin", "Nebelung", "Norwegian Forest Cat", "Ocicat", "Oriental Short Hair",
   "Oriental Tabby", "Persian", "Pixiebob", "Ragamuffin", "Ragdoll", "Russian Blue", "Scottish Fold",
   "Siamese", "Siberian", "Snowshoe", "Sphynx - Hairless Cat", "Tabby", "Tiger", "Tonkinese",
   "Torbie", "Tortoiseshell", "Turkish Angora", "Turkish Van", "Tuxedo"]
nb_classes = len(categories)

# 이미지 크기 지정
image_w = 64
image_h = 64
image_d = 3
pixels = image_w * image_h * image_d


def check_img_shape(data):
    if data.ndim != 3:
        return False

    if data.shape[0] != image_w or data.shape[1] != image_h or data.shape[2] != 3:
        return False

    if data.size != pixels:
        return False

    return True


def main():
    X = []
    Y = []

    for idx, breed in enumerate(categories):
        label = [0 for i in range(nb_classes)]
        label[idx] = 1 # Ex. [0, 1, 0, 0, 0] or [1, 0, 0, 0, 0]

        breed_root_dir = DATA_PATH + breed + "\\"
        #image_dir_list = os.listdir(breed_root_dir)

        #for dir in image_dir_list:
        files = glob.glob(breed_root_dir + "\\*.jpg")
        print(files)

        for i, f in enumerate(files):
            img = Image.open(f)
            img = img.convert("RGB")
            img = img.resize((image_w, image_h))
            data = np.asarray(img, dtype=object).astype('float32')  # numpy 배열로 변

            if not check_img_shape(data):
                continue

            X.append(data)
            Y.append(label)
            if i % 100 == 0:
                print(i, "\n", data)


    X = np.array(X)
    Y = np.array(Y)
    # 학습 전용 데이터와 테스트 전용 데이터 구분
    X_train, X_test, y_train, y_test = train_test_split(X, Y)
    xy = (X_train, X_test, y_train, y_test)

    print('>>> data 저장중 ...')
    np.save("./image_data_with_agu.npy", xy)
    print("ok,", len(Y))


main()
