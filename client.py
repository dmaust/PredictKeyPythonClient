__author__ = 'dmaust'

import json
import requests
from pprint import pprint

post_data = {
    "text":"I enjoy writing to APIs with my favorite programming",
    "apikey": "demo"
}
response = requests.post("http://demo.predictkey.com/predict", json=post_data)
pprint(response.json())
