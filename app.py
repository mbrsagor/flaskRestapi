from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}


class HelloWorld(Resource):
    def get(self):
        return {"hello": "World"}


class SimpleTodo(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


class Todo1(Resource):
    def get(self):
        # Default to 200 OK
        return {'task': 'Hello world'}


class Todo2(Resource):
    def get(self):
        # Set the response code to 201
        return {'task': 'Hello world'}, 201


class Todo3(Resource):
    def get(self):
        # Set the response code to 201 and return custom headers
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run()
