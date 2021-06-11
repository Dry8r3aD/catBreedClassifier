import numpy as np
import keras
from PIL import Image


def run(data):
    new_model = keras.models.load_model('./model/model_no1.hdf5')
    new_model.summary()

    prediction = new_model.predict(data)
    print(prediction)
    np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

    result = {
        'prd': prediction[0].tolist(),
        'ans': int(prediction[0].argmax())
    }

    return result


def make_data(img_url):
    X = []
    img = Image.open(img_url)

    img = img.convert("RGB")
    img = img.resize((64, 64))

    data = np.asarray(img, dtype='float32')
    X.append(data)
    X = np.array(X)

    return X


def run_model_main(img_file):
    img_data = make_data(img_file)
    return run(img_data)
