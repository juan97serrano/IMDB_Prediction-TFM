# IMDB Rating Prediction
## KSchool:Máster en Inteligencia Artificial y Deep Learning
## Trabajo de Fin de Máster realizado por: Rodrigo Díaz Morón y Juan Serrano Vara

### 1- Datos

Los datos han sido Scrapeados de la Web de IMDB (https://www.imdb.com) a través de la librería Selenium.

![IMDB_Image](https://github.com/juan97serrano/IMDB_Prediction-TFM/blob/master/images_readme/Screenshot%202020-08-30%20at%2012.50.25.png)

Se descargó para cada película de las 540000 la siguiete información: Imagen promocional, Duración, Título, Descripción, Color, Año de publicación, Director, Número de votos, Géneros, Lenguajes, País, Keywords, Escritores, Actores, Rating.

Esto se ha realizdo con los códigos que se encuentran en la carpeta del repositorio llamada Scraper.

### 2- Preprocesamiento

### 3- Clasificadores

### 4- Aplicación

Opción A:
* Acceder a la app: URL

Opción B (Descargar en local):
 
* Instalar Docker.

* Descargar imagen de Docker Hub y la carpeta flask_app del repositorio. Para ello situados dentro de la carpeta ejcutar el siguiente comando. 

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
| Tabular Classificator | Contenido de la celda  | Contenido de la celda  | Contenido de la celda  | Contenido de la celda  | Contenido de la celda  |
| IMG Classificator | Contenido de la celda  | Contenido de la celda  | Contenido de la celda  | Contenido de la celda  | Contenido de la celda  |
| IMG+Tab Classificator | Contenido de la celda  | Contenido de la celda  | Contenido de la celda  | Contenido de la celda  | Contenido de la celda  |
| Description Classificator | 50  | 55  | 63  | 45  | 56  |
| Title Classificator | 31  | 49  | 45  | 42  | 42  |





Nota: Todos los códigos a excepción de los que son de la aplicación web están preparados para ser ejecutados con Google Colaborative Notebooks


