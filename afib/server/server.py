#/// API calling function
 
from flask_restful import Resource, Api
from flask import jsonify, request
from db.db import *
from bson import json_util, ObjectId
import json

class ApiIsAlive(Resource):
    def get(self):
        return jsonify({'alive' : True})
    
    
class AtrialFibrillationApi(Resource):
    
    def post(self):
        ecg_data = request.get_json()
        print(ecg_data)
    
    def get(self):
        ecg = []
        col = DB['ecg']
        count = 0
        for e in col.find({}):
            ecg.append(e)
            count += 1
            if count == 50:
                break
        ecg_data = json.loads(json_util.dumps(ecg))
        return jsonify(ecg_data)