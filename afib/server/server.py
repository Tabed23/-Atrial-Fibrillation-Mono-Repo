#/// API calling function
 
from flask_restful import Resource, Api
from flask import jsonify, request
from db.db import *
from bson import json_util, ObjectId
import json
from marshmallow import Schema, fields, ValidationError


class BaseSchema(Schema):
    age = fields.Integer(required=True)
    sex = fields.String(required=True)
    height = fields.Float(required=True)
    weight = fields.Float(required=True)
    ritmi =  fields.Integer(required=True)
    I = fields.Float(required=True)
    II = fields.Float(required=True)
    III = fields.Float(required=True)
    aVF =  fields.Float(required=True)
    aVR = fields.Float(required=True)
    aVL = fields.Float(required=True)
    V1 = fields.Float(required=True)
    V2 = fields.Float(required=True)
    V3 = fields.Float(required=True)
    V4 =  fields.Float(required=True)
    V5 =  fields.Float(required=True)
    V6  =  fields.Float(required=True)
    cp = fields.Integer(required=True)
    trtbps = fields.Integer(required=True)
    chol = fields.Integer(required=True)
    fbs = fields.Integer(required=True)
    restecg  = fields.Integer(required=True)
    thalachh  = fields.Integer(required=True)
    exng  = fields.Integer(required=True)
    oldpeak =  fields.Float(required=True)
    slp  = fields.Integer(required=True)
    caa  = fields.Integer(required=True)
    thall  = fields.Integer(required=True)

class ApiIsAlive(Resource):
    def get(self):
        return jsonify({'alive' : True})
    
    
class AtrialFibrillationApi(Resource):
    
    def post(self):
        patient_data  = request.get_json()
        schema = BaseSchema()
        try:
            result = schema.load(patient_data)
        except ValidationError as err:
             return jsonify(err.messages), 400
        
        return jsonify(result)
    
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