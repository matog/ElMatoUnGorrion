### Él Mató un Gorrión

Es un bot para twitter creado en python, utilizando la librería tweepy. Mezcla letras al azar de Él Mató un Policia Motorizado y Peligrosos Gorriones, y las publica en twitter.

Para ver cómo funciona, visitar la cuenta de twitter: [ElMatoUnGorrion](https://twitter.com/ElMatoUnGorrion)

#### Archivos

- scrapping_el_mato.py: Archivo de scrapping de las letras de Él Mató a un Policía Motorizado. Las letras se descargan de https://letrasbd.com/. Genera el archivo el_mato.csv
- scrapping_peligoroso_gorriones: Archivo de scrapping de las letras de Peligrosos Gorriones. Las letras se descargan de https://www.buscaletras.com/. Genera el archivo peligrosos_gorriones.csv
- twitter.py: Lee las letras de los dos archivos csv, elige dos estrofas al azar, de una canción también seleccionada al azar de cada banda. Luego, intercala las estrofas las publica en twitter. Se necesitan los token de acceso que se gestionan en twitter.

Se necesita un archivo _.env_ con la siguiente información (entre ''):
        
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    ACCESS_TOKEN = ''
    ACCESS_TOKEN_SECRET  = ''

![image](https://user-images.githubusercontent.com/660448/109560254-6e6bdb00-7aba-11eb-940b-a1922b4bd803.png)
