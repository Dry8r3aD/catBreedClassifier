from keras.models import Sequential
from keras.layers import Dropout, Activation, Dense
from keras.layers import Flatten, Convolution2D, MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
import os
import time
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

"""10473
실제 학습하는 코드
preprocessing 과정에서 나온 데이터셋 결과물을 기반으로 학습을 수행한다.
VGG 모델을 기반으로 작성하였고, 레이어를 추가하면 성능이 더 올라가긴 할 것으로 생각됨...
optimizer 등은 논문 찾아가며 조금씩 바꿔야하고... active function 등도 바꺼가며 테스트 필요
완성된 모델은 hdf5 형식으로 저장하여 사용 할 수 있게끔 함
"""

DATA_PATH = "C:\\Users\\dry8r3ad\\PycharmProjects\\catBreedClassifier\\data\\agumentation\\"
# DATA_PATH = "C:\\Users\\dry8r3ad\\PycharmProjects\\catBreedClassifier\\data\\original\\"

train_batch_size = 1500
test_batch_size = 400
steps_per_epoch = 10472
epoch_cnt = 5

image_w = 64
image_h = 64
image_d = 3
pixels = image_w * image_h * image_d
images = []


def build_cnn_model(class_cnt):
    model = Sequential()
    model.add(Convolution2D(32, (3, 3), input_shape=(image_w, image_h, image_d), padding='same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Convolution2D(64, (3, 3), padding='same'))
    model.add(Activation('relu'))

    model.add(Convolution2D(64, (3, 3)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    # 전결합층
    model.add(Flatten())  # 벡터형태로 reshape
    model.add(Dense(512))  # 출력
    model.add(Activation('relu'))
    model.add(Dropout(0.5))

    model.add(Dense(class_cnt))
    model.add(Activation('softmax'))

    return model


def main():
    # 학습 데이터의 경우 추가 Augmentation은 여기서 해주면 좋음
    data_generator = ImageDataGenerator(
        rescale=1./255,         # Resize (정규화)
        validation_split=0.2    # 8:2로 학습/테스트 데이터셋을 나눔
    )

    train_generator = data_generator.flow_from_directory(
        directory=DATA_PATH,
        target_size=(image_w, image_h),
        batch_size=train_batch_size,
        class_mode="categorical",
        subset="training"
    )

    test_generator = data_generator.flow_from_directory(
        directory=DATA_PATH,
        target_size=(image_w, image_h),
        batch_size=test_batch_size,
        class_mode="categorical",
        subset="validation"
    )

    model = build_cnn_model(len(train_generator.class_indices))
    print(train_generator.class_indices)

    """
    -- Loss(Objective) Function / Optimizer
    1. categorical_crossentropy, rmsprop: 10%
    2. binary_crossentropy, Adam: 15%
    3. binary_crossentropy, Adamax: 24%
    4. Same as 3, with agu. 20% 
    5. Same as 3, with agu. 20% (1600, 2094, 1)
    6. 
    """
    model.compile(loss="binary_crossentropy",
                  optimizer="Adamax",
                  metrics=["accuracy"])

    print(model.summary())
    model_filename = "cnn_model_" + str(time.time()) + ".hdf5"
    print(model_filename)
    if not os.path.exists(model_filename):
        model.save(model_filename)

    model.fit_generator(
        train_generator,
        steps_per_epoch=steps_per_epoch,
        epochs=epoch_cnt,
        validation_data=test_generator,
        validation_steps=5
    )

    # Evaluation
    score = model.evaluate_generator(test_generator)
    print("Loss= ", score[0])
    print("Accuracy= ", score[1])
    print(score)


main()
