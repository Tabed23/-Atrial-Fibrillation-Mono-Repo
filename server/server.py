#/// API calling function
from flask_restful import Resource, Api
from flask import jsonify, request
from db.db import *
from bson import json_util, ObjectId
import json
from services.service import AtrialFibrillationServiceLayer
from flask_apispec import marshal_with
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields

# Swagger Response Schema in UI
class IsAliveResponseSchema(Schema):
    message = fields.Bool(default=True)

# API Health Check
class ApiIsAlive(MethodResource, Resource):
    @marshal_with(IsAliveResponseSchema)   
    def get(self):
        return jsonify({'alive' : True})



# AFIB API
class AtrialFibrillationApi(Resource):
    
    
    def post(self):
        
        patient_data  = request.get_json() ## get the json data
        
        srv = AtrialFibrillationServiceLayer() # initialization the service layer
        
        res = srv.Create_Schema(patient_data) # create the schema
        
        patient_req = json.loads(json_util.dumps(patient_data)) #Serialize the schema
        
        return jsonify({"schema": patient_req, "status": 200})
    
    def get(self):
        ecg = []
        col = DB['EcgCollection']
        count = 0
        for e in col.find({}):
            ecg.append(e)
            count += 1
            if count == 50:
                break
        ecg_data = json.loads(json_util.dumps(ecg))
        return jsonify(ecg_data)