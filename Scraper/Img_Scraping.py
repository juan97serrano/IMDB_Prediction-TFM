from pandas import DataFrame
from selenium import webdriver
import pandas as pd
import os
import csv

def extract_info(film):

    film_list = []

    url = "https://www.imdb.com/title/" + film + "/?ref_=fn_al_tt_1"
    driver.get(url)

    img_len = len(driver.find_elements_by_class_name("poster"))
    if img_len == 1:
        img = driver.find_element_by_class_name("poster")      
        src=img.find_element_by_xpath("./a/img").get_attribute("src")
        os.system("wget %s --no-check-certificate -O %s.png" % (src, "../data/img/"+film))
        film_list = film_list + [[film,film+".png"]]

    return film_list

def header():
    csv_row=[]
    head = ["CODE","file_name"]
    csv_row.append(head)
    return csv_row


df = pd.read_csv("../data/title.basics.tsv", sep="\t",nrows=1000)
#df_filter = df[df["titleType"] == "movie"]
df_filter_reset_index = df.reset_index()
ids_film = df_filter_reset_index["tconst"].tolist()

driver = webdriver.Chrome(executable_path="local/chromedriver")

iter_for_saving = 5
row = 0
for num, film in enumerate(ids_film[:20]):
    with open('../data/Result_Scraper_CSV/img/IMDBimg_andlikes.csv', 'a', encoding="utf-8") as f:                
        
        writer = csv.writer(f,delimiter='\t')
        if row == 0 :
            writer.writerows(header())
        writer.writerows(extract_info(film))
    
    row += 1

