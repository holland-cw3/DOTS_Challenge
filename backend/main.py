from flask import Flask, request
from flask_restful import Resource, Api
import pandas as pd
from specialFilter import specialFilter
from semesterFilter import semesterFilter
from flask_cors import CORS
from permFilter import permFilter

lots = []
with open('lots.txt', 'r') as file:
    lines = file.read().splitlines() 
    lots.extend(lines) 

def filter (date, time, lots, permissions):
    lots = specialFilter(date, lots)
    lots, perms = semesterFilter(date, lots)
    if perms == False:
        print(lots)
        return lots
    else:
        lots = permFilter(date, time, lots, permissions)
    return lots


app = Flask(__name__)
CORS(app)  
api = Api(app)

class GetItems(Resource):
    def get(self):
        date = request.args.get('date')
        time = request.args.get('time')
        permissions = request.args.getlist('permissions')  
        
        date = pd.to_datetime(date)
        time = pd.to_datetime(time).strftime('%H:%M')
      
        filtered_lots = filter(date, time, lots, permissions)

        if isinstance(filtered_lots, set):
            filtered_lots = list(filtered_lots)
                    
        return {'Lots': filtered_lots}

api.add_resource(GetItems, '/')

if __name__ == '__main__':
    app.run(debug=True)