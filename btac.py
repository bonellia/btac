import requests
import json

CLIENT_ID = '8dda116418894e0895884c99d106ce92'
CLIENT_SECRET = 'cae4026256d5468e84851f58ccf5aed0'
SPOTIFY_USER = 'sillybearbuddy'

GRANT_TYPE = 'client_credentials'
body_params = {'grant_type' : GRANT_TYPE}

url = 'https://accounts.spotify.com/api/token'
response = requests.post(url, data=body_params, auth = (CLIENT_ID, CLIENT_SECRET))

token_raw = json.loads(response.text)
token = token_raw["access_token"]

headers = {"Authorization" : "Bearer {}".format(token)}

testurl = f'https://api.spotify.com/v1/users/{SPOTIFY_USER}/playlists'
r = requests.get(url=testurl, headers=headers)

print (r.text)