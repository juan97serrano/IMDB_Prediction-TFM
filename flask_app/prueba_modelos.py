import tensorflow as tf 
import tensorflow.keras.preprocessing.image as krs_image
from PIL import Image
import numpy as np

image = krs_image.load_img("foto.jpg", target_size=(268,182))
img_array = krs_image.img_to_array(image, data_format="channels_last")

img_array = np.array([img_array])

print(img_array.shape)

loaded_model = tf.keras.models.load_model("models/Img")

#print(loaded_model.summary())

prediction = loaded_model.predict([[img_array]])


print(prediction)