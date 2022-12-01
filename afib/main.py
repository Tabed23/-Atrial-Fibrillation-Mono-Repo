from model.afib import Afib
from flask import Flask, request, Response, jsonify
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

app = Flask(__name__)

# swagger API

a = Afib()
a.formate_data()