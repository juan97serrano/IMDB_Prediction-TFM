from pandas import DataFrame
from selenium import webdriver
import pandas as pd
import os

df = pd.read_csv("../data/title.basics.tsv", sep="\t",nrows=1000)
df_filter = df[df['titleType'] == 'movie']
df_filter_reset_index = df_filter.reset_index()

ids_film = df_filter_reset_index['tconst'].tolist()

driver = webdriver.Chrome(executable_path='local/chromedriver')
correct_films = 0

# test_list = ['tt7286456',ids_film[538827],'tt0187393']

for num, film in enumerate(ids_film):
    print("Imagen número:", num, ", ID:", film)

    url = 'https://www.imdb.com/title/' + film + '/?ref_=fn_al_tt_1'
    # url = 'https://pro.imdb.com/title/'+film
    driver.get(url)

    # Busca los elementos que tienen en el contenido un determinado texto, budget y cumulative...
    # description = driver.find_element_by_class_name('title_wrapper')
    img = driver.find_element_by_class_name('poster').find_element_by_class_name()
    src = img.get_attribute('src')
    tag_name = "film"
    os.system("wget %s --no-check-certificate -O %s.png" % (src, tag_name))
    print(img.text)

driver.close()