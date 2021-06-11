from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import cv2

#np.random.seed(15)

DATA_PATH = "C:\\Users\\dry8r3ad\\PycharmProjects\\catBreedClassifier\\data\\agumentation\\"

generator = ImageDataGenerator(rescale=1. / 255)

batch_size = 4
iterations = 5
images = []

obj = generator.flow_from_directory(
    DATA_PATH,
    target_size=(150, 150),
    batch_size=batch_size,
    class_mode='binary')

for i in enumerate(range(iterations)):
    img, label = obj.next()
    n_img = len(label)
    print(img)

    base = cv2.cvtColor(img[0], cv2.COLOR_RGB2BGR)  # keras는 RGB, openCV는 BGR이라 변경함
    for idx in range(n_img - 1):
        img2 = cv2.cvtColor(img[idx + 1], cv2.COLOR_RGB2BGR)
        base = np.hstack((base, img2))
    images.append(base)

img = images[0]
for idx in range(len(images) - 1):
    img = np.vstack((img, images[idx + 1]))

cv2.imshow('result', img)