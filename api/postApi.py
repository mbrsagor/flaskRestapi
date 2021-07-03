from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

posts = {
    [
        {"name": "New post", "author": "Sagor", "posted_date": "20-December-2021", "is_publish": True},
        {"name": "Another New post", "author": "Mbr sagor", "posted_date": "10-March-2021", "is_publish": False}
    ]
}


class Post(Resource):
    def get(self):
        # Set the response code to 201
        return posts, 201
