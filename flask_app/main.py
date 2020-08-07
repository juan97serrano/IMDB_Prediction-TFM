import flask
from flask import Flask, request
import json
import base64
import io
import numpy as np
import ast
import os
from PIL import Image
import io

import keras.preprocessing.image as krs_image
import tensorflow.keras.models as models

from PIL import Image
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def template():
    return flask.render_template('index.html')

@app.route("/put_prediction/", methods=['GET', 'POST'])
def read_and_predict():


    valor = request.get_json(force = True)

    opcion = int(valor['opcion'])

    if opcion == 1:
        # Img
        url = valor['url_img']
        img_array = Img_to_array(url)
        pred_rating = predict_img(img_array)
        return "Esta imagen es de la categoría: " + str(pred_rating)
    
    if opcion == 4:
        # titulo
        titulo = valor['titulo']
        pred_rating = predict_title(titulo)
        return "Este titulo es de la categoría: " + str(pred_rating)
        
    if opcion == 5:
        # descripcion
        descripcion = valor['Descripcion']
        return str(descripcion)
           
    if opcion == 6:
        # titulo + descripción
        return str("ambas")
        

    return "holi"

def Img_to_array(url):

    url += "=" * ((4 - len(url) % 4) % 4)

    decoded = base64.b64decode(url)

    path = io.BytesIO(decoded)
    
    #image = krs_image.load_img(path, target_size=(268,182))
    #img_array = krs_image.img_to_array(image, data_format="channels_last")
    im = Image.open(path)
    img = im.resize((182,268), Image.ANTIALIAS)
    img_array = np.array(img)


    return img_array

def predict_img(img_array):

    img = np.array([img_array])

    loaded_model = models.load_model("models/img")

    prediction = loaded_model.predict(img)

    result = np.argmax(prediction)

    return result

def predict_title(title):

    loaded_model = models.load_model("models/title")
    prediction = loaded_model.predict([title])

    result = np.argmax(prediction)

    return result



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')