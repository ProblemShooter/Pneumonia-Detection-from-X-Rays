import os

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import cv2
from PIL import Image
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.applications.vgg19 import VGG19


app = Flask(__name__)

# Global model variable
model_03 = None


def build_model():
    """
    Build model architecture and load trained weights.
    """

    base_model = VGG19(
        include_top=False,
        weights=None,  # Prevent ImageNet download
        input_shape=(224, 224, 3)
    )

    x = base_model.output
    x = Flatten()(x)

    x = Dense(4608, activation='relu')(x)
    x = Dropout(0.2)(x)

    x = Dense(1152, activation='relu')(x)

    output = Dense(2, activation='softmax')(x)

    model = Model(inputs=base_model.input, outputs=output)

    weights_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "model_weights",
            "vgg19_model_02.h5"
        )
    )

    print(f"Loading weights from: {weights_path}")

    model.load_weights(weights_path)

    print("Model loaded successfully.")

    return model


def get_model():
    """
    Lazy-load model only when first prediction is requested.
    """
    global model_03

    if model_03 is None:
        print("Loading model...")
        model_03 = build_model()

    return model_03


def get_className(classNo):
    if classNo == 0:
        return "Normal"
    elif classNo == 1:
        return "Pneumonia"
    return "Unknown"


def getResult(img_path):
    model = get_model()

    image = cv2.imread(img_path)

    if image is None:
        raise FileNotFoundError(
            f"Unable to read uploaded image: {img_path}"
        )

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image = Image.fromarray(image)
    image = image.resize((224, 224))

    image = np.array(image).astype("float32") / 255.0

    input_img = np.expand_dims(image, axis=0)

    prediction = model.predict(input_img, verbose=0)

    predicted_class = int(np.argmax(prediction, axis=1)[0])

    return predicted_class


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def upload():
    try:
        if "file" not in request.files:
            return "No file uploaded"

        file = request.files["file"]

        if file.filename == "":
            return "No file selected"

        upload_dir = os.path.join(
            os.path.dirname(__file__),
            "uploads"
        )

        os.makedirs(upload_dir, exist_ok=True)

        file_path = os.path.join(
            upload_dir,
            secure_filename(file.filename)
        )

        file.save(file_path)

        prediction = getResult(file_path)

        result = get_className(prediction)

        return result

    except Exception as e:
        print("Prediction error:", e)
        return f"Error: {str(e)}"


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        threaded=False
    )