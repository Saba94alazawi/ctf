import requests
from requests.auth import HTTPBasicAuth
import time




def connecting(user, password):
    url = 'http://127.0.0.1:8000/connecting/'
    r = requests.post(url=url, auth=HTTPBasicAuth(user, password), data={'status':True})
    print('Connection Check Sent')