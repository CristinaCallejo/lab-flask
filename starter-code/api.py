from pymongo import MongoClientimport requests
from flask import Flask, request



app = Flask(__name__)

client = MongoClient()
db = client.get.database()
db = db.companies 

@app.route("/")
def test ():
    hola = "hola"
    return hola

@app.route ("/receta/salmorejo")
def hacer_salmorejo ():
    ingredientes

def loquesea():
    db.find({})
    return

app.run("0.0.0.0" , 98 debug=True) #