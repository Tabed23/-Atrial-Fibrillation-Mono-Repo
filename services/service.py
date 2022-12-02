## /// buiness logic 

## data processing

##get data from databaase
## return the predicted data

from db.db import *
from services.validate_scheema import BaseSchema
from marshmallow import ValidationError

class AtrialFibrillationServiceLayer:
    def __init__(self):
        self.col = DB['AtrialFibrillationCollection']
    
    def Create_Schema(self, patient_schema):
        schema = BaseSchema()
        try:
            result = schema.load(patient_schema)
        except ValidationError as err:
             return json.dumps(err.messages)
         
        try:
            res = self.col.insert_one(patient_schema)
            return res.inserted_id
        except ValidationError as err:
            return "cannot insert patient schema"