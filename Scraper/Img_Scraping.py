from pandas import DataFrame
from selenium import webdriver
import pandas as pd
import os

df = pd.read_csv("../data/title.basics.tsv", sep="\t",nrows=1000)
df_filter = df[df['titleType'] == 'movie']
df_filter_reset_index = df_filter.reset_index()
ids_film = df_filter_reset_index['tconst'].tolist()

driver = webdriver.Chrome(executable_path='local/chromedriver')

for num, film in enumerate(ids_film):
    # TODO: - guardar en un dataframe
    #       - que se guarde el dataframe cada x iteraciones
    print("Imagen número:", num, ", ID:", film)
    url = 'https://www.imdb.com/title/' + film + '/?ref_=fn_al_tt_1'
    driver.get(url)

    img_len = len(driver.find_elements_by_class_name('poster'))
    if img_len == 1:
        img = driver.find_element_by_class_name('poster')      
        src=img.find_element_by_xpath("./a/img").get_attribute("src")
        os.system("wget %s --no-check-certificate -O %s.png" % (src, "../data/img/"+film))
   

driver.close()