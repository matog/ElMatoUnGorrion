# Scrapper de letras de Peligrosos gorriones

from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.buscaletras.com/autor/peligrosos-gorriones/'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

content_titulos = soup.find_all('p', 'entry-title')
# enlace_cancion = []

filename = 'peligros_gorriones2.csv'
f = open(filename,'w')
headers = 'grupo\tcancion\tletra\n'
f.write(headers)

for tit in content_titulos:
    sub = tit.find_all('a')
    for titulo in sub:
        enlace = titulo.attrs.get('href')
        page_letra = requests.get(enlace)
        source = BeautifulSoup(page_letra.content, "html.parser")
        main = source.article
        titulo = main.find('h1','entry-title').text
        letras = main.find('div','entry-content').get_text(strip=True, separator="|")
        csv = 'Peligrosos Gorriones' + '\t' + titulo + '\t' + letras + '\n'
        print(csv)
        f.write(csv)
f.close()
