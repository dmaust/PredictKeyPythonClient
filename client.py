__author__ = 'dmaust'

import json
import requests
from pprint import pprint

def get_prediction(text, partial_words=False):
    post_data = {
        "text":text,
        "apikey": "demo",
        "partial": partial_words
    }
    response = requests.post("http://api.predictkey.com/predict", json=post_data)
    return response.json()

def show_prediction_debug(text, partial_words=False):
    pred = get_prediction(text, partial_words=partial_words)
    print "Predictions for:", text
    print "Partial words:", "enabled" if partial_words else "disabled"
    print "Top Prediction:", pred['results'][0]['word']
    print "Full output:"
    pprint(pred)
    print ""

if __name__=="__main__":
    show_prediction_debug("I enjoy writing to APIs with my favorite programming") # Top result: Language
    show_prediction_debug("Have a good d", partial_words=True) # Top result "day"
    show_prediction_debug("Have a good n", partial_words=True) # Top result "night"
