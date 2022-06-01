
from dotenv import load_dotenv
import requests
import pandas as pd
import json
import os

load_dotenv()  # take environment variables from .env.

API_KEY = os.getenv('YT_KEY')
channelID = "UCCezIgC97PvUuR4_gbFUs5g"
params = {'key': API_KEY, 'channelId': channelID, 'part': 'snippet'}
response = requests.get('https://www.googleapis.com/youtube/v3/search', params=params).json()
# print(type(response))

df = pd.DataFrame(response['items'])
print(df)

# print(os.getenv('API_KEY'))