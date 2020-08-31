# IMDB Rating Prediction
## KSchool: Máster en Inteligencia Artificial y Deep Learning
## Trabajo de Fin de Máster realizado por: Rodrigo Díaz Morón y Juan Serrano Vara

### 1- Datos

Los datos han sido Scrapeados de la Web de IMDB (https://www.imdb.com) a través de la librería Selenium.

![IMDB_Image](https://github.com/juan97serrano/IMDB_Prediction-TFM/blob/master/images_readme/Screenshot%202020-08-30%20at%2012.50.25.png)

Se descargó para cada película de las 540000 la siguiete información: Imagen promocional, Duración, Título, Descripción, Color, Año de publicación, Director, Número de votos, Géneros, Lenguajes, País, Keywords, Escritores, Actores,Content Rating Metascore Rating, Budget CWG (Cumulative Worldwide Gross), Rating.

Esto se ha realizdo con los códigos que se encuentran en la carpeta del repositorio llamada "Scraper·.

Los datos ORIGINALES se encuentran en el siguiente directorio en la carpeta Original las imágenes se encuentran comprimidas en un fichero .zip:

https://drive.google.com/drive/folders/1eqbmKMAjCjl1AWGqrRhgdbuQZzzm8pSU?usp=sharing

### 2- Preprocesamiento

Las técnicas de preprocesamiento implementadas se encuentran explicadas en el Punto 2 en el informe del TFM. Todas las técnicas realizadas se encuentran en  los ficheros de la carpeta llamada "Preprocesamiento". Ahí encontraremos una seríe de ficheros numerados del 0-7 que indican el orden en el que se han ido realizado los cambios en el dataset original hasta obtener el fichero final llamado "imdb_data.csv".

FICHEROS (en la carpeta Preprocesamiento):

0-Data_concat.ipynb: Unimos todos los ficheros resultantes del Scraper.

1-Data_pre_process.ipynb: Seleccionamos solo las películas que tienen la información que nos interesa (quitamos las películas que tienen unknown en una serie de variables). Fichero resultante: FILTERED_FINAL_IMBD_DATA.csv

2-Filtered_per_images.ipynb: Filtra los datos obtenidos por solo los que tienen imagen. Fichero resultante: filtered_df_with_imgNames.csv

3-Tabular_preprocess.ipynb: Reazliamos el preprocesamiento básico indicado en el punto 2 del informe. Fichero resultante imdb_data.csv

4-Tabular_Preprocess_with_actors.ipynb: Nos vemos oblgados a realizar el scraper de solo los actores y el fichero resultante lo unimos con el generado en el punto 3. Fichero resultante imdb_data.csv

5-get_votes.ipynb: Formateamos de manera correcta la variable votos. Fichero resultante imdb_data.csv

6-Filter_per_votes.ipynb: Filtramos las películas por las que tienen mas de 125 votos. Fichero resultante imdb_data.csv

7-Downsampling_Img_to_Array.ipynb: Lee todas la imágenes resultantes de realizar el filtro por votos y convierte cada imagen en un fichero .npy que contiene en array de la imagen con el reescalado a 32*32. El fichero resultante img_numpy.zip contiene todos los arrays de cada imagen.

Los datos resultantes de todos los pasos del preprocesamiento se encuentran en el siguiente directorio (ficehros imdb_data.csv, code_train_dv.csv y code_test_dv.csv, img_numpy.zip) todos los demas archivos generados en los pasos intermedios se encuentran en la carpeta antiguos:

https://drive.google.com/drive/folders/1eqbmKMAjCjl1AWGqrRhgdbuQZzzm8pSU?usp=sharing

### 3- Clasificadores

**Tabular classificator**

##### Baselines
Los codigos que se han utilizado de Machine Learning para la realización de los **baselines** se encuentran en la carpeta Tabular classification/Pruebas ML.
##### Entity Embeddings
EL codigo que se ha utlizado para hacer la clasificacion es: Tabular classification/Tabular_classification.ipynb

**Image+Tab classificator**

EL codigo que se ha utlizado para hacer la clasificacion es: ClasificadorMultiInput/Clasificador_Multi_Input.ipynb

**Image classificator**

EL codigo que se ha utlizado para hacer la clasificacion es: Img classification/IMG_Clasiffier-ModeloPropio.ipynb

**Title classificator**

EL codigo que se ha utlizado para hacer la clasificacion es: Text/Text Classification/Title_classification_from_scratch.ipynb

**Description classificator**

EL codigo que se ha utlizado para hacer la clasificacion es: Text/Text Classification/Description_classification_with_tensorflowhub.ipynb


### 4- Aplicación

Opción A:
* Acceder a la app: http://34.106.165.107:5000

Opción B (Descarga en local):
 
* Instalar Docker.

* Descargar imagen de Docker Hub y la carpeta flask_app del repositorio. Para ello situados dentro de la carpeta ejcutar el siguiente comando.

* Descargar esta carpeta (https://drive.google.com/file/d/1R7FlSWD1lKl91_9lmHRhf_k90ruYoh_k/view?usp=sharing) y ponerla en dentro de la carpeta flask_app.

```
bash docker_buildImg.sh
```

* Ejecutar el fichero .bash “docker_buildContainer.sh”. Dentro del fichero tenemos que cambiar el ID de la imágen por el ID que le ha asignado docker en nuestra máquina. (Ejecutar docker image ls)

```
docker_buildContainer.sh
```
* En nuestro navegador introducir en el campo de la URL: http://localhost:5000.


![IMDB_APP](https://github.com/juan97serrano/IMDB_Prediction-TFM/blob/master/images_readme/Screenshot%202020-08-30%20at%2012.33.39.png)

### 4- Resultados


#### Métricas para conjunto de test.

| Algoritmo | Recall Clase 0 | F1 Score Clase 1 | Precision Clase 2 | Accuracy | Custom Metric |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Tabular Classificator | 65  | 62 | 73  | 63  | 66  |
| IMG Classificator | 27  | 56  | 48  | 45  | 44  |
| IMG+Tab Classificator | 57  | 60  | 68  | 61  | 62  |
| Description Classificator | 50  | 55  | 63  | 45  | 56  |
| Title Classificator | 31  | 49  | 45  | 42  | 42  |


Nota: Todos los códigos a excepción de los que son de la aplicación web están preparados para ser ejecutados con Google Colaborative Notebooks


