import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
from PIL import Image
import cv2
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.applications.vgg19 import VGG19


def build_model():
    base_model = VGG19(include_top=False, input_shape=(224, 224, 3))
    x = base_model.output
    flat = Flatten()(x)
    class_1 = Dense(4608, activation='relu')(flat)
    drop_out = Dropout(0.2)(class_1)
    class_2 = Dense(1152, activation='relu')(drop_out)
    output = Dense(2, activation='softmax')(class_2)
    model = Model(base_model.inputs, output)
    weights_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model_weights', 'vgg19_model_02.h5'))
    model.load_weights(weights_path)
    return model


try:
    model_03 = build_model()
    print('Model loaded. Check http://127.0.0.1:5000/')
except Exception as e:
    model_03 = None
    print('Error loading model:', e)

app = Flask(__name__)


def get_className(classNo):
	if classNo==0:
		return "Normal"
	elif classNo==1:
		return "Pneumonia"


def getResult(img):
    if model_03 is None:
        raise RuntimeError('Model not loaded')

    image = cv2.imread(img)
    if image is None:
        raise FileNotFoundError(f'Unable to read image: {img}')

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image = image.resize((224, 224))
    image = np.array(image).astype('float32') / 255.0
    input_img = np.expand_dims(image, axis=0)
    result = model_03.predict(input_img, verbose=0)
    return int(np.argmax(result, axis=1)[0])


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        value=getResult(file_path)
        result=get_className(value) 
        return result
    return None


if __name__ == '__main__':
    app.run(debug=False, threaded=False, use_reloader=False)