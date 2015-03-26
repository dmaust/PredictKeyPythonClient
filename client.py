__author__ = 'dmaust'

import json
import requests
from pprint import pprint

def get_prediction(text):
    post_data = {
        "text":text,
        "apikey": "demo"
    }
    response = requests.post("http://api.predictkey.com/predict", json=post_data)
    return response.json()

if __name__=="__main__":
    pred = get_prediction("I enjoy writing to APIs with my favorite programming")
    print "Top Prediction:", pred['results'][0]['word']
    print "Full output"
    pprint(pred)