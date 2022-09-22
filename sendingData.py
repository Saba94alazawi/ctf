import requests
from requests.auth import HTTPBasicAuth
import time



def dataSend(user, password, data):
    url = 'http://127.0.0.1:8000/fine/'
    r = requests.post(url=url, auth=HTTPBasicAuth(user, password), data=data)
    print('SENT')