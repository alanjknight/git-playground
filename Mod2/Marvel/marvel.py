import requests
 
api_key = '0b0da139da4e43e63b0e6b2e2625a421'
headers = {'Authorization': 'Bearer {}'.format(api_key)}
resp = requests.get("https://gateway.marvel.com:443/v1/public/characters?apikey=&api_key")
print(resp)
