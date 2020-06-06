from flask import *
import sqlite3
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    try:
       action = req.get('queryResult').get('action')
       cityname = req.get('queryResult').get('queryText')
       not_yet = req.get('queryResult').get('queryText')
       
       #name = req.get('parameters').get('name.original')
       print('this is name of user '+not_yet)
       
    except AttributeError:
        return 'errro by json'
    print(req)
    print("Hallo world")
    #matching action value
                             
    if action == "hi":
           #if 'username'  request.args:
            #return 'Hello ' + request.args['name']
                 speech = "You said " + cityname
                 return tell(speech)
    
@app.route("/") 
def home_view(): 
		return "<h1>Welcome 2 Imran Server</h1>"
