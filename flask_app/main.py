import flask
from flask import Flask, request, jsonify
import json
import base64
import io
import numpy as np
import ast
import os
from PIL import Image
import io
from PIL import Image
import numpy as np
import yake
import tensorflow as tf
import tensorflow.keras.models as models
from tensorflow.keras.preprocessing import text, sequence
import pandas as pd

import pickle

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
        return str(pred_rating)
    
    if opcion == 2:
        # Cat_data
        datos_cat = valor['datos_categoricos']
        descripcion = valor['Descripcion']

        extract_keywords = text_2_keywords(descripcion)

        datos_cat.append(extract_keywords)

        input_net = datos_cat_2_data(datos_cat)

        result = predict_tab(input_net)

        return jsonify(str(result),extract_keywords)
       
    if opcion == 3:
        # Cat_data + Img
        datos_cat = valor['datos_categoricos']
        descripcion = valor['Descripcion']
        url = valor['url_img']
        
        extract_keywords = text_2_keywords(descripcion)

        img_array = Img_to_array(url)
        img_array = np.array([img_array])

        datos_cat.append(extract_keywords)

        dict = data_img_2_dict(datos_cat,img_array)

     

        result = predict_tab_img(dict)

        return jsonify(result,extract_keywords)
    
    if opcion == 4:
        # titulo
        titulo = valor['titulo']
        titulo = title_preproc(titulo)
        result = predict_title(titulo)
        return result
        
    if opcion == 5:
        # descripcion
        descripcion = valor['Descripcion']
        result = predict_des(descripcion)
        return result

def Img_to_array(url):

    url += "=" * ((4 - len(url) % 4) % 4)

    decoded = base64.b64decode(url)

    path = io.BytesIO(decoded)
    
    im = Image.open(path)
    img = im.resize((32,32), Image.NEAREST)
    img_array = np.array(img)
    
    img_array = img_array/255
    img_array = img_array.astype(int)
    
    return img_array

def predict_img(img_array):

    img = np.array([img_array])

    loaded_model = models.load_model("models/img")

    prediction = loaded_model.predict(img)

    result = np.argmax(prediction)

    result = interpret_result(result)

    return result

def predict_tab_img(dict):

    loaded_model = models.load_model("models/tab_img")
    prediction = loaded_model.predict(dict)

    result = np.argmax(prediction)

    result = interpret_result(result)

    return result

def predict_title(title):

    loaded_model = models.load_model("models/title")

    prediction = loaded_model.predict([title])

    result = np.argmax(prediction)

    result = interpret_result(result)

    return result

def predict_des(desc):

    loaded_model = models.load_model("models/description")

    prediction = loaded_model.predict([desc])

    result = np.argmax(prediction)

    result = interpret_result(result)

    return result

def predict_tab(data):

    loaded_model = models.load_model("models/tab")
    prediction = loaded_model.predict([data])

    result = np.argmax(prediction)

    result = interpret_result(result)

    return result

def title_preproc(titulo):

    with open('models/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    
    titulo = np.array([titulo])
    title = tokenizer.texts_to_sequences(titulo)
    title = sequence.pad_sequences(title, maxlen=30)
   
    return title
    

def interpret_result(result):

    if result == 0:

        return ("El rating obtenido será entre 0-5")

    elif result == 1:

        return ("El rating obtenido será entre 5-6,5")

    elif result == 2:

        return ("El rating obtenido será entre 6,5-10")

def text_2_keywords(description):

    language = "en"
    max_ngram_size = 1
    deduplication_thresold = 0.9
    deduplication_algo = 'seqm'
    windowSize = 1
    numOfKeywords = 1

    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(description)

    return keywords[0][0]

def data_img_2_dict(data,img):

    list_dict = load_dicts("dict_multi/")

    datos_cat = pd.DataFrame(data)

    print("longuitud: ",len(list_dict))

    color = datos_cat.iloc[0].map(list_dict[0]).fillna(0).values
    director = datos_cat.iloc[1].map(list_dict[1]).fillna(0).values
    generos0 = datos_cat.iloc[2].map(list_dict[2]).fillna(0).values
    generos1 = datos_cat.iloc[3].map(list_dict[3]).fillna(0).values
    generos2 = datos_cat.iloc[4].map(list_dict[4]).fillna(0).values
    lenguaje = datos_cat.iloc[5].map(list_dict[5]).fillna(0).values
    pais = datos_cat.iloc[6].map(list_dict[6]).fillna(0).values
    keywords0 = datos_cat.iloc[7].map(list_dict[7]).fillna(0).values
    keywords1 = datos_cat.iloc[8].map(list_dict[8]).fillna(0).values
    keywords2 = datos_cat.iloc[9].map(list_dict[9]).fillna(0).values
    escritor = datos_cat.iloc[10].map(list_dict[10]).fillna(0).values
    content_rating = datos_cat.iloc[11].map(list_dict[11]).fillna(0).values
    actores0 = datos_cat.iloc[12].map(list_dict[12]).fillna(0).values
    actores1 = datos_cat.iloc[13].map(list_dict[13]).fillna(0).values
    actores2 = datos_cat.iloc[14].map(list_dict[14]).fillna(0).values
    duracion = int(datos_cat.iloc[15])
    anio = int(datos_cat.iloc[16])
    descripcion = datos_cat.iloc[17].map(list_dict[15]).fillna(0).values

    tabular_dict= {
      'Input_COLOR':np.array(color),
      "Input_DIRECTOR":np.array(director),
      "Input_GENRES_0":np.array(generos0),
      "Input_GENRES_1":np.array(generos1),
      "Input_GENRES_2":np.array(generos2),
      "Input_LANGUAGE_0":np.array(lenguaje),
      "Input_COUNTRY_0":np.array(pais),
      "Input_KEYWORDS_0":np.array(keywords0),
      "Input_KEYWORDS_1":np.array(keywords1),
      "Input_KEYWORDS_2":np.array(keywords2),
      "Input_WRITERS_0":np.array(escritor),
      "Input_CONTENT_RATING":np.array(content_rating),
      "Input_KEYWORDS_DESCRIPTION":np.array(descripcion),
      "Input_ACTOR_0":np.array(actores0),
      "Input_ACTOR_1":np.array(actores1),
      "Input_ACTOR_2":np.array(actores2),
      "DURATION_Input":np.array([duracion]),
      "YEAR_Input":np.array([anio])
    }

    cnn_input = {"IMG_Input":img}

    tabular_dict.update(cnn_input)

    return tabular_dict

def datos_cat_2_data(datos_cat):

    # ORDEN CORRECTO
    #categorical_vars = ['COLOR','DIRECTOR','GENRES_0','GENRES_1','GENRES_2','LANGUAGE_0','COUNTRY_0','KEYWORDS_0','KEYWORDS_1','KEYWORDS_2','WRITERS_0','CONTENT_RATING','KEYWORDS_DESCRIPTION','ACTOR_0','ACTOR_1','ACTOR_2','DURATION','YEAR']
    
    #ORDEN LISTA DEL DICCIONARIO
    #categorical_vars = ['COLOR','DIRECTOR','GENRES_0','GENRES_1','GENRES_2','LANGUAGE_0','COUNTRY_0','KEYWORDS_0','KEYWORDS_1','KEYWORDS_2','WRITERS_0','CONTENT_RATING','ACTOR_0','ACTOR_1','ACTOR_2','KEYWORDS_DESCRIPTION']
    
    # ORDEN EN EL QUE LLEGAN 
    # data = [color,director,generos0,generos1,generos2,lenguaje,pais,keywords0,keywords1,keywords2,escritor,content_rating,actores0,actores1,actores2,duracion,anio,descripcion]   

    list_dict = load_dicts("dict_tab/")
  

    datos_cat = pd.DataFrame(datos_cat)

    print("longuitud: ",len(list_dict))

    color = datos_cat.iloc[0].map(list_dict[0]).fillna(0).values
    director = datos_cat.iloc[1].map(list_dict[1]).fillna(0).values
    generos0 = datos_cat.iloc[2].map(list_dict[2]).fillna(0).values
    generos1 = datos_cat.iloc[3].map(list_dict[3]).fillna(0).values
    generos2 = datos_cat.iloc[4].map(list_dict[4]).fillna(0).values
    lenguaje = datos_cat.iloc[5].map(list_dict[5]).fillna(0).values
    pais = datos_cat.iloc[6].map(list_dict[6]).fillna(0).values
    keywords0 = datos_cat.iloc[7].map(list_dict[7]).fillna(0).values
    keywords1 = datos_cat.iloc[8].map(list_dict[8]).fillna(0).values
    keywords2 = datos_cat.iloc[9].map(list_dict[9]).fillna(0).values
    escritor = datos_cat.iloc[10].map(list_dict[10]).fillna(0).values
    content_rating = datos_cat.iloc[11].map(list_dict[11]).fillna(0).values
    actores0 = datos_cat.iloc[12].map(list_dict[12]).fillna(0).values
    actores1 = datos_cat.iloc[13].map(list_dict[13]).fillna(0).values
    actores2 = datos_cat.iloc[14].map(list_dict[14]).fillna(0).values
    duracion = int(datos_cat.iloc[15])
    anio = int(datos_cat.iloc[16])
    descripcion = datos_cat.iloc[17].map(list_dict[15]).fillna(0).values

    data= [np.array(color),
            np.array(director),
            np.array(generos0),
            np.array(generos1),
            np.array(generos2),
            np.array(lenguaje),
            np.array(pais),
            np.array(keywords0),
            np.array(keywords1),
            np.array(keywords2),
            np.array(escritor),
            np.array(content_rating),
            np.array(descripcion),
            np.array(actores0),
            np.array(actores1),
            np.array(actores2),
            np.array([duracion]),
            np.array([anio])]
    
    return data

def load_dicts(folder):

    categorical_vars = ['COLOR','DIRECTOR','GENRES_0','GENRES_1','GENRES_2','LANGUAGE_0','COUNTRY_0','KEYWORDS_0','KEYWORDS_1','KEYWORDS_2','WRITERS_0','CONTENT_RATING','ACTOR_0','ACTOR_1','ACTOR_2','KEYWORDS_DESCRIPTION']
    list_dict = []
    for cat in categorical_vars:
        print(cat)
        dict = np.load(folder+cat+'.npy',allow_pickle='TRUE').item()
        list_dict.append(dict)
    return list_dict



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')