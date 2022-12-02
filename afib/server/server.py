#/// API calling function
 
from flask_restful import Resource, Api
from flask import jsonify
from db.db import *

class ApiIsAlive(Resource):
    def get(self):
        return jsonify({'alive' : True})
    
    
class AtrialFibrillationApi(Resource):
    
    def post(self):
        pass
    
    def get(self):
        ecg = []
        col = DB['ecg']
        for e in col.find_one({}):
            ecg.append(e)
        return jsonify({'ecg' : ecg})