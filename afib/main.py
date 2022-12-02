from flask import Flask, request, Response, jsonify
from flask_restful import Api
from db.db import *
from server.server import ApiIsAlive, AtrialFibrillationApi

app = Flask(__name__)
api = Api(app)


api.add_resource(ApiIsAlive, '/api/v1/health')
api.add_resource(AtrialFibrillationApi, '/api/v1/ecg_data')
if __name__ == '__main__':
    InitDB()
    app.run(debug=True)