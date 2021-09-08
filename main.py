import requests
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
CORS(app)
api = Api(app)

db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    price = db.Column(db.Integer)
    quanity = db.Column(db.Integer)
    discount_price = db.Column(db.Integer)
    image = db.Column(db.String(200))
    
    # UniqueConstraint('discount_price', 'title', name='user_product_unique')


class Index(Resource):
    def get(self):
        data = [
            {"Name": "Bozlur Rosid Sagor"},
            {"Profession": "Software Engineer"},
            {"Company": "Circle Fintech"},
        ]
        return data


api.add_resource(Index, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
