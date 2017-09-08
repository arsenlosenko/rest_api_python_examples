#!/usr/bin/env python3

from flask import Flask, request, render_template
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)


@app.route('/', methods=('POST', 'GET'))
def home():
    return render_template('index.html')


class Clicks(Resource):
    clicks = 0

    def get(self):
        print("Sending clicks")
        return {"clicks": self.clicks}, 200

    def post(self):
        print("Adding click")
        self.__class__.clicks += 1
        return 201

    def delete(self):
        print("Deleting click")
        self.__class__.clicks -= 1
        return 200

api.add_resource(Clicks, '/api/v1/clicks')

if __name__ == '__main__':
    app.run(port="5002")