from selenium import webdriver 
import csv   
from selenium.common.exceptions import *
import time
import pandas as pd
import numpy as np

def film_info(film):
    film_info = []
    csv_row = []
    
    film_info.append(film) #1 CODIGO 
    
    try:
        title = browser.find_element_by_xpath("//span[contains(@id, 'titleYear')]/parent::h1") #2 TITULO
        head, sep, tail = title.text.partition(' (')
        film_info.append(head)
    except NoSuchElementException:
        film_info.append("unknown")
  
    try:
        description = browser.find_element_by_class_name('summary_text') #3 DESCRIPCIÓN
        film_info.append(description.text)
    except NoSuchElementException:
        film_info.append("unknown")
  
    try:
        duration = browser.find_element_by_tag_name('time') #4 DURACIÓN
        film_info.append(duration.text)
    except NoSuchElementException:
        film_info.append("unknown")
        
    try:
        color = browser.find_element_by_xpath("//h4[text()='Color:']/following-sibling::a") #5 COLOR
        film_info.append(color.text)
    except NoSuchElementException:
        film_info.append("unknown")
    
    try:
        year = browser.find_element_by_id('titleYear') #6 AÑO
        film_info.append(year.text)
    except NoSuchElementException:
        film_info.append("unknown")
    
    try:
        director = browser.find_element_by_xpath("//h4[text()='Director:']/following-sibling::a") #7 DIRECTOR
        film_info.append(director.text)
    except NoSuchElementException:
        film_info.append("unknown")  
    
    try:
        budget = browser.find_element_by_xpath("//h4[text()='Budget:']/parent::div") #8 BUDGET
        if "(estimated)" in budget.text:
            head, sep, tail = budget.text.partition(':')
            film_info.append(tail[:-12])
        else:
            head, sep, tail = budget.text.partition(':')
            film_info.append(tail)
    except NoSuchElementException:
        film_info.append("unknown") 
        
    try:    
        cwg = browser.find_element_by_xpath("//h4[text()='Cumulative Worldwide Gross:']/parent::div") #9 CUMULATIVE WORLDWIDE GROSS
        head, sep, tail = cwg.text.partition(': ')
        film_info.append(tail)
    except NoSuchElementException:
        film_info.append("unknown")    
    
    try:
        IMBD_rating = browser.find_element_by_xpath("//span[@itemprop='ratingValue']") #10 RATING
        film_info.append(IMBD_rating.text)
    except NoSuchElementException:
        film_info.append("unknown")    
    
    try:
        votes = browser.find_element_by_xpath("//span[@itemprop='ratingCount']") #11 NUM VOTOS
        film_info.append(votes.text)
    except NoSuchElementException:
        film_info.append("unknown")    
    
    try:
        metascore_rating = browser.find_element_by_xpath("//div[contains(@class, 'metacriticScore')]") #12 METASCORE RATING
        film_info.append(metascore_rating.text)
    except NoSuchElementException:
        film_info.append("unknown")        
    
    try:
        genres = browser.find_element_by_xpath("//h4[text()='Genres:']/parent::div") #13 GENERO
        head, sep, tail = genres.text.partition(': ')
        film_info.append(tail)
    except NoSuchElementException:
        film_info.append("unknown")
        
    try:
        language = browser.find_element_by_xpath("//h4[text()='Language:']/parent::div") #14 LENGUA
        head, sep, tail = language.text.partition(': ')
        film_info.append(tail)
    except NoSuchElementException:
        film_info.append("unknown")    
        
    try:    
        country = browser.find_element_by_xpath("//h4[text()='Country:']/parent::div") #15 COUNTRY
        head, sep, tail = country.text.partition(': ')
        film_info.append(tail)
    except NoSuchElementException:
        film_info.append("unknown")
        
    try:   
        certification = browser.find_element_by_xpath("//h4[text()='Certificate:']/parent::div") #16 EDAD
        head, sep, tail = certification.text.partition(': ')
        film_info.append(tail)
    except NoSuchElementException:
        film_info.append("unknown")
        
    try:   
        keywords = browser.find_element_by_xpath("//h4[text()='Plot Keywords:']/parent::div") #17 PALABRAS CLAVE
        head, sep, tail = keywords.text.partition(': ')
        film_info.append(tail)
    except NoSuchElementException:
        film_info.append("unknown")
        
    try:
        writer = browser.find_element_by_xpath("//h4[text()='Writers:']/parent::div | //h4[text()='Writer:']/parent::div ") #18 ESCRITORES
        head, sep, tail = writer.text.partition(': ')
        film_info.append(tail)
    except NoSuchElementException:
        film_info.append("unknown")
        
    try:   
        opening_weekend = browser.find_element_by_xpath("//h4[text()='Opening Weekend USA:']/parent::div") #19 FIN DE SEMANA DE LANZAMIENTO
        head, sep, tail = opening_weekend.text.partition(': ')
        film_info.append(tail)
    except NoSuchElementException:
        film_info.append("unknown")
    
    csv_row.append(film_info)

    return csv_row


def header():
    csv_row=[]
    head = ["CODE","TITLE","DESCRIPTION", "DURATION", "COLOR", "YEAR", "DIRECTOR", "BUDGET", "CWG", "RATING", \
            "VOTES", "METASCORE RATING", "GENRES", "LANGUAGE", "COUNTRY", "CONTENT RATING", "KEYWORDS", \
            "WRITERS", "OPENING WEEKEND"]
    csv_row.append(head)
    return csv_row


#test_films = ['tt0004667','tt0071562', 'tt7286456','tt0187393','tt0000001','tt0000002','tt0000003','tt0000004']
#id_films = test_films
id_films = np.load('../data/lista_final_ids.npy',allow_pickle=True).tolist()
id_films = id_films[512019:]
browser = webdriver.Firefox()
row = 0
for film in id_films:
    
    url = 'https://www.imdb.com/title/'+film+'/?ref_=fn_al_tt_1' 
    browser.get(url)
    
    with open('IMBD_data_8.csv', 'a', encoding="utf-8") as f:                
        
        writer = csv.writer(f,delimiter='\t')
        if row == 0 :
            writer.writerows(header())
        writer.writerows(film_info(film))
    
    row += 1
    if row % 500 == 0:
        print(row)
    
    if row % 200 == 0:
        browser.close()
        time.sleep(1)
        browser = webdriver.Firefox()
        
   id_films = np.load('../data/lista_final_ids.npy',allow_pickle=True).tolist()
   id_films.index("tt9916754")
   id_films[542067:]
