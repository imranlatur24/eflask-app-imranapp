from flask import *
import sqlite3
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    #try:
    action = req.get('queryResult').get('action')
    cityname = req.get('queryResult').get('queryText')
    not_yet = req.get('queryResult').get('queryText')
       
       #name = req.get('parameters').get('name.original')
    print('this is name of user '+not_yet)
       
    #except AttributeError:
    #    return 'errro by json'
    print(req)
    print("Hallo world")
    #matching action value

     
       https://api.openweathermap.org/data/2.5/weather?appid=3e90723e72e3e77055f8c10dccb120f8&q=

    if action == "hi":
            return make_response(jsonify({'fulfillmentText': "I h've headphones",
                 "fulfillmentMessages":[
      {"platform":"PLATFORM_UNSPECIFIED","text":{"text":["enter your city name.."],"mesasage":"text"},
           ] }))


   
    elif action == "city":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            cityname = req.get('queryResult').get('queryText')
            api_address='https://api.openweathermap.org/data/2.5/weather?appid=3e90723e72e3e77055f8c10dccb120f8&q='
            # city = input('City Name :')
            city = cityname
            url = api_address + city
            json_data = requests.get(url).json()
            formatted_data = json_data['main']['temp']
            print(formatted_data)
            return make_response(jsonify({'fulfillmentText': "your city tempreture is: ",formatted_data))
        

@app.route("/") 
def home_view(): 
		return "<h1>Welcome 2 Imran Server</h1>"
