from flask import Flask, request
from flask_restful import Resource, Api
import pandas as pd
from specialFilter import specialFilter
from semesterFilter import semesterFilter
from flask_cors import CORS


# from permFilter import permFilter

date = '1/1/2024'
time = '03:00'
permissions = []

date = pd.to_datetime(date)

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
    # else:
        # filter permissions
        # lots = permFilter(date, time, lots, permissions)
    return lots


app = Flask(__name__)
CORS(app)  # This will allow ALL origins (localhost, 127.0.0.1, etc.)
api = Api(app)

class GetItems(Resource):
    def get(self):
        date = request.args.get('date')
        time = request.args.get('time')
        permissions = request.args.getlist('permissions')  
        
        date = pd.to_datetime(date)
      
        filtered_lots = filter(date, time, lots, permissions)
        
        return {'Lots': filtered_lots}

api.add_resource(GetItems, '/')

if __name__ == '__main__':
    app.run(debug=True)