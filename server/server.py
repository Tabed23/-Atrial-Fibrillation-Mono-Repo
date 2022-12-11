#/// API calling function
from flask_restful import Resource, Api
from flask import jsonify, request
from db.db import *
from bson import json_util, ObjectId
import json
from ast import literal_eval
from services.service import AtrialFibrillationServiceLayer
from flask_apispec import marshal_with, use_kwargs, doc
from flask_apispec.views import MethodResource
from ast import literal_eval
from schema.swagger_schema import IsAliveResponseSchema, AtrialFibrillationRequestSchema, AtrialFibrillationResponseSchema, AtrialFibrillationRequestPutSchema, AtrialFibrillationResponsePutSchema
# API Health Check
class ApiIsAlive(MethodResource, Resource):

    @doc(description='Atrial Fibrillation API.', tags=['Health Check'])
    @marshal_with(IsAliveResponseSchema)
    def get(self):
        return jsonify({'alive' : True})

# Atrial Fibrillation API implementation
class AtrialFibrillationPredictApi(MethodResource,Resource):
    def __init__(self):
        self.srv = AtrialFibrillationServiceLayer() # initialization the service layer

    @doc(description='Atrial Fibrillation API.', tags=['AFIB Prediction Request'])
    @use_kwargs(AtrialFibrillationRequestSchema)
    @marshal_with(AtrialFibrillationResponseSchema)
    def post(self, **kwargs):
        data = request.data
        patient_data = literal_eval(data.decode('utf-8'))

        res = self.srv.Create_Schema(patient_data) # create the schema
        patient_req = json.loads(json_util.dumps(patient_data)) #Serialize the schema

        # get prediction result
        out_dict = self.srv.Get_Prediction(patient_req)
        return jsonify({'prediction': out_dict, "status": "success" , "status_code":200 , "status_message":res})



class AtrialFibrillationPutApi(MethodResource,Resource):
     def __init__(self):
        self.srv = AtrialFibrillationServiceLayer() # initialization the service layer

     @doc(description='Atrial Fibrillation API.', tags=['AFIB  Update Record'])
     @use_kwargs(AtrialFibrillationRequestPutSchema)
     @marshal_with(AtrialFibrillationResponsePutSchema)
     def put(self, **kwargs):
        data = request.data
        patient_data = literal_eval(data.decode('utf-8'))
        patient_req = json.loads(json_util.dumps(patient_data)) #Serialize the schema
        res = self.srv.Update_Record(patient_schema)

class AtrialFibrillationDeleteApi(MethodResource,Resource):
     def __init__(self):
        self.srv = AtrialFibrillationServiceLayer() # initialization the service layer

     @doc(description='Atrial Fibrillation API.', tags=['AFIB  Delete Record'])
     def delete(self, **kwargs):
        pass
