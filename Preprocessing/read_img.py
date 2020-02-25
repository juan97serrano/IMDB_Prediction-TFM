import os
from tensorflow.keras.preprocessing import image
import numpy as np


def load_imgs(img_list, dir='../data/img/'):
    """
    :param img_list: list with the image names.
    :param dir: directory where the images are located
    :return: list with imgs
    """
    array_img = []
    for img in img_list:
        img_load = image.load_img(dir + img)
        # img_load = image.load_img(dir + img)
        img_array = image.img_to_array(img_load)

        array_img = array_img + [img_array]

    return array_img


imgs_list = os.listdir('../data/img/')
imgs_list.remove('.DS_Store')
array_img = np.array(load_imgs(imgs_list))

np.save('images', array_img)

