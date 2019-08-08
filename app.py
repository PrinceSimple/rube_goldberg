from flask import Flask, render_template
import json, urllib
import requests

app = Flask(__name__)

@app.route('/')

def index():
    return render_template(
    'home.html', Trains=Trains)

r = requests.get('https://bvg-grabber-api.herokuapp.com/actual?station=Oderbruchstrasse&vehicles=Tram').json()
data = r[0][1]
Trains = []
for train in data:
    if not 'Zingster' in train['end'] and not 'Marzahn' in train['end'] and not 'Hellersdorf' in train['end']:
        Trains.append(train)
print(Trains)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
