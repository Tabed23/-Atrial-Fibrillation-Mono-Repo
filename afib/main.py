from model.afib import Afib
from flask import Flask, request, Response, jsonify
app = Flask(__name__)



a = Afib()
a.formate_data()