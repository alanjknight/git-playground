import requests
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():


    resp = requests.get("https://transportapi.com/v3/uk/bus/stop/490008660N/live.json?app_id=f36238d0&app_key=224b784d3583e78b37e4b5187209c7cd&group=no&nextbuses=yes")
    json = resp.json()

    busses = []
    for bus in json['departures']['all']:
        busses.append({'line':bus['line'], 'direction':bus['direction'], 'departuretime':bus['expected_departure_time']}) 

        
    return render_template('index.html', busses=busses)

atcocodes = ["490008660N","490008660S"]

