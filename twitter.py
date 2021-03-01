import tweepy
import json
import pandas as pd
import random
from dotenv import load_dotenv
import os

# Credentials
load_dotenv('.env')

# Twitter
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

### TEST
# data = api.me()
# print(json.dumps(data._json, indent=2))


# Cargamos el dataset con las letras
gorrion = pd.read_csv('peligros_gorriones.csv', sep = '\t')
motorizado = pd.read_csv('el_mato.csv', sep = '\t')

# Elegimos un registro al azar de cada dataset
# y lo convertimos en una lista, lo dividimos por "|! y filtramos los vacios
gorrion = gorrion.sample(n=1)
gorrion = gorrion['letra'].tolist()
gorrion = [i.split('|') for i in gorrion]
gorrion = list(filter(None, gorrion[0]))

motorizado = motorizado.sample(n=1)
motorizado = motorizado['letra'].tolist()
motorizado = [i.split('|') for i in motorizado]
motorizado = list(filter(None, motorizado[0]))

combi_twit = ''
combi_twit = combi_twit + random.choice(motorizado) + "\n"
combi_twit = combi_twit + random.choice(gorrion) + "\n"
combi_twit = combi_twit + random.choice(motorizado) + "\n"
combi_twit = combi_twit + random.choice(gorrion) + "\n"
combi_twit = combi_twit.capitalize()
print(combi_twit)

api.update_status(combi_twit)





