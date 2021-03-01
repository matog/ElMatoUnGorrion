from bs4 import BeautifulSoup
import requests
import csv

url = 'https://letrasbd.com/el-mato-a-un-policia-motorizado/'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

content_titulos = soup.find_all('div', 'thesongs clearfix')
# enlace_cancion = []

filename = 'el_mato.csv'
f = open(filename,'w')
headers = 'grupo\tcancion\tletra\n'
f.write(headers)

for tit in content_titulos:
    sub= tit.find_all('a')
    for titulo in sub:
        enlace = titulo.attrs.get('href')
        print(titulo.text)
        print(enlace)
        page_letra = requests.get(enlace)
        source = BeautifulSoup(page_letra.content, "html.parser")
        content_letra = source.find_all('article', 'lyrics')
        csv = ''
        for lyrics in content_letra:
            sub_letra = lyrics.find_all('p')
            letra_csv =''
            for subs in sub_letra[1:]:
                parrafo = subs.get_text(strip=True, separator="|")
                # print(parrafo)
                # print("-----------")
                letra_csv += parrafo + "|"
        # print(" - - - - - - - - - - - - - - - - - - - - ")
        # print(letra_csv)
        # print(" - - - - - - - - - - - - - - - - - - - - ")
        csv = 'Él mató a un policía motorizado' + '\t' + titulo.text + '\t' + letra_csv + '\n'
        print(csv)
        f.write(csv)
        csv = ""
f.close()