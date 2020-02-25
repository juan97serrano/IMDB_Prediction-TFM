from pandas import DataFrame
from selenium import webdriver
import pandas as pd
import numpy as np
import os
import csv
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException
import time


def extract_info(film):

    film_list = []

    url = "https://www.imdb.com/title/" + film + "/?ref_=fn_al_tt_1"
    driver.get(url)
    
    img_len = len(driver.find_elements_by_class_name("poster"))
    if img_len == 1:
        img = driver.find_element_by_class_name("poster")      
        src=img.find_element_by_xpath("./a/img").get_attribute("src")
        os.system("wget %s --no-check-certificate -O %s.png" % (src, "data/img/"+film))
        film_list = film_list + [[film,film+".png"]]

    return film_list

def header():
    csv_row=[]
    head = ["CODE","file_name"]
    csv_row.append(head)
    return csv_row


numpy_lista = np.load("lista_final_ids.npy",allow_pickle=True)
ids_film = list(numpy_lista)
print(str(ids_film[:2])+"...")

driver = webdriver.Firefox(executable_path="local/geckodriver")

iter_for_saving = 5
row = 0
for num, film in enumerate(ids_film[441367:]):
    with open('data/IMDBimg_andlikes.csv2', 'a', encoding="utf-8") as f:                
        
        writer = csv.writer(f,delimiter='\t')
        if row == 0 :
            writer.writerows(header())
        try:
            info_film = extract_info(film)
        except NoSuchElementException:
            info_film = [film,"No Img"]
        writer.writerows(info_film)
    
    row += 1
    if row % 200 == 0:
        driver.close()
        time.sleep(1)
        driver = webdriver.Firefox(executable_path="local/geckodriver")

