import sys
import numpy as np
import keras
from PIL import Image


def run_model(data):
    new_model = keras.models.load_model('./model/cnn_model_1622697570.2869382.hdf5')
    new_model.summary()

    prediction = new_model.predict(data)
    np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

    pred_str = prediction[0]
    pred_ans = prediction[0].argmax()
    print("Prediction: ", pred_str, pred_ans)


def make_data(img_url):
    X = []
    img = Image.open(img_url)
    img = img.convert("RGB")
    img = img.resize((64, 64))
    data = np.asarray(img, dtype='float32')
    X.append(data)
    X = np.array(X)

    return X


def main(img_url):
    img_data = make_data(img_url)
    run_model(img_data)


if __name__ == '__main__':
    # ./venv/bin/python ./loadModel.py ./data/test_sample.jpeg
    if len(sys.argv) > 1:
        # "./data/test_sample.jpeg"
        img_url = sys.argv[1]
        main(img_url)
