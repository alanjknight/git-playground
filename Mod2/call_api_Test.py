import requests

url = 'http://rem-rest-api.herokuapp.com'
ret=requests.get(url)
print ret.status_code

