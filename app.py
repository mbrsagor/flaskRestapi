from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

#
# @app.route('/')
# def hello_world():
#     return render_template('index.html')


class HelloWorld(Resource):
    def get(self):
        return {"hello": "World"}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run()
