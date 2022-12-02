#/// API calling function
 
from flask_restful import Resource, Api
from flask import jsonify

class ApiIsAlive(Resource):
    def get(self):
        return jsonify({'alive' : True})
    
    
class AtrialFibrillationApi(Resource):
    
    def post(self):
        pass
        