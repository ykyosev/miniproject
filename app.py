from flask import Flask, render_template, request, jsonify, make_response
from functools import wraps
import json
import requests
from pprint import pprint
from flask import  Response
from cassandra.cluster import Cluster

cluster = Cluster(['35.246.127.142'], port = 9042)
session = cluster.connect()
app = Flask(__name__)

def authorization(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'admin' and auth.password == 'pass':
            return f(*args,**kwargs)

        return make_response ('Login not Successfu', 401, {'WWW-Authenticate': 'Basic realm= "Login needed"'})

    return decorated

weather_url_template = 'http://api.apixu.com/v1/current.json?key={mykey}&q={location}'

@app.route('/')
def login():
    if request.authorization and request.authorization.username == 'admin' and request.authorization.password == 'pass':
        return render_template('home.html')

    return make_response ('Login not Successful', 401, {'WWW-Authenticate': 'Basic realm= "Login required"'})

@app.route('/current',  methods=['GET'])
@authorization
def current():
    my_key = request.args.get('mykey','70702aa939cb4945856111842191303')
    my_location = request.args.get('location','London')

    weather_url = weather_url_template.format(mykey = my_key, location = my_location)

    resp = requests.get(weather_url)
    if resp.ok:
        show = resp.json()

    else:
        print(resp.reason)

    return jsonify("TODAY'S WEATHER",show)

@app.route('/forecast',  methods=['GET', 'POST'])
@authorization
def forecast():
    my_key = request.args.get('mykey','70702aa939cb4945856111842191303')
    my_location = request.form.get('location')
    my_days = request.args.get('days')

    # row = session.execute (""" select days from asd.stats where location ='{}' ALLOW FILTERING """.FORMAT())
    row = session.execute (""" select days from asd.stats where location ='{}' ALLOW FILTERING """.format(my_location))
    for asd in row:
        asdid = asd.days
    
    url_template = 'http://api.apixu.com/v1/forecast.json?key={mykey}&q={location}&days={days}'
    weather_url = url_template.format(mykey = my_key, location = my_location, days = asdid)

    resp = requests.get(weather_url)
    if resp.ok:
        show = resp.json()

    else:
        print(resp.reason)

    return jsonify(show)




if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)

