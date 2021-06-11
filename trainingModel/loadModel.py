import numpy as np
import keras
from PIL import Image


new_model = keras.models.load_model('./cnn_model_1622697570.2869382.hdf5')
new_model.summary()

X = []
img = Image.open("./data/test_sample.jpg")
img = img.convert("RGB")
img = img.resize((64, 64))
data = np.asarray(img, dtype='float32')
X.append(data)

X = np.array(X)

prediction = new_model.predict(X)
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

pred_str = prediction[0]
pred_ans = prediction[0].argmax()
print("Prediction: ", pred_str, pred_ans)
