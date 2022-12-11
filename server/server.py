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
class AtrialFibrillationApi(MethodResource,Resource):

    @doc(description='Atrial Fibrillation API.', tags=['AFIB Detection Request'])
    @use_kwargs(AtrialFibrillationRequestSchema)
    @marshal_with(AtrialFibrillationResponseSchema)
    def post(self, **kwargs):
        data = request.data
        patient_data = literal_eval(data.decode('utf-8'))
        srv = AtrialFibrillationServiceLayer() # initialization the service layer
        res = srv.Create_Schema(patient_data) # create the schema
        patient_req = json.loads(json_util.dumps(patient_data)) #Serialize the schema

        # get prediction result
        out_dict = srv.Get_Prediction(patient_req)
        return jsonify({'prediction': out_dict, "status": "success" , "status_code":200})
    @doc(description='Atrial Fibrillation API.', tags=['AFIB Detection Request'])
    def delete(self, **kwargs):
        pass

    @doc(description='Atrial Fibrillation API.', tags=['AFIB Detection Request'])
    @use_kwargs(AtrialFibrillationRequestPutSchema)
    @marshal_with(AtrialFibrillationResponsePutSchema)
    def put(self, **kwargs):
        pass
