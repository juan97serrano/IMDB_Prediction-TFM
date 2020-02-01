from pandas import DataFrame
from selenium import webdriver
import pandas as pd
import os

df = pd.read_csv("../data/title.basics.tsv", sep="\t",nrows=1000)
#df_filter = df[df["titleType"] == "movie"]
df_filter_reset_index = df.reset_index()
ids_film = df_filter_reset_index["tconst"].tolist()

driver = webdriver.Chrome(executable_path="local/chromedriver")

film_list = []

iter_for_saving = 10

for num, film in enumerate(ids_film[:50]):
    url = "https://www.imdb.com/title/" + film + "/?ref_=fn_al_tt_1"
    driver.get(url)

    img_len = len(driver.find_elements_by_class_name("poster"))
    if img_len == 1:
        img = driver.find_element_by_class_name("poster")      
        src=img.find_element_by_xpath("./a/img").get_attribute("src")
        os.system("wget %s --no-check-certificate -O %s.png" % (src, "../data/img/"+film))
        film_list = film_list + [[film,film+".png"]]
    
    if num % iter_for_saving == 0:      # Guardamos el dataframe cada x iteraciones   
        films_df = pd.DataFrame(film_list)
        films_df.to_csv("../data/Result_Scraper_CSV/img/IDfilmsandImg_Iter_"+str(num)+".csv")

films_df = pd.DataFrame(film_list)
films_df.to_csv("../data/Result_Scraper_CSV/img/IDfilmsandImg_Finished.csv")
driver.close()
