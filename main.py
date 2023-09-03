from flask import Flask
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
    quantity = db.Column(db.Integer)
    discount_price = db.Column(db.Integer)
    image = db.Column(db.String(200))

    UniqueConstraint('discount_price', 'title', name='user_product_unique')


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Book(Base):
   __tablename__ = 'books'
   id = Column(Integer, primary_key=True)
   title = Column(String)
   author = Column(String)
   engine = create_engine('sqlite:///books.db')
   Session = sessionmaker(bind=engine)
   session = Session()

# Create a new book
new_book = Book(title="Django Unleashed", author="Andrew Pinkham")
session.add(new_book)
session.commit()



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
