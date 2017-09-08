#!/usr/bin/env python3

from flask import Flask, request, render_template
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)


@app.route('/', methods=('POST', 'GET'))
def home():
    return render_template('index.html')


class Clicks(Resource):
    clicks = {
        "rel": "self",
        "link": "http://localhost:5002/api/v1/clicks",
        "amount": 0
    }

    def get(self):
        print("Sending clicks")
        return self.__class__.clicks , 200

    def post(self):
        print("Adding click")
        self.__class__.clicks['amount'] += 1
        return self.__class__.clicks, 201

    def delete(self):
        print("Deleting click")
        self.__class__.clicks['amount'] -= 1
        return self.__class__.clicks


class Users(Resource):
    user = {
        "name": "",
        "clicks": Clicks().clicks,
        "rel": "self",
        "link": "http://localhost:5002/api/v1/users",
    }

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name')

    def get(self):
        return self.__class__.user

    def post(self):
        args = self.parser.parse_args()
        self.__class__.user['name'] = args['name']
        return self.__class__.user

api.add_resource(Clicks, '/api/v1/clicks')
api.add_resource(Users, '/api/v1/users')

if __name__ == '__main__':
    app.run(port="5002")