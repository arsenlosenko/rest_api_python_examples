#!/usr/bin/env python3

from flask import Flask, request, render_template
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1' : {"task": 'build an API'},
    'todo2' : {"task": '???'},
    'todo3' : {"task": 'Profit!'},
}

users = []


def abort_if_todo_exists(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')
parser.add_argument('user')


@app.route('/', methods=('POST', 'GET'))
def home():
    return render_template('index.html')


class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_exists(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_exists(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


class TodoList(Resource):
    def get(self):
        return  TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201


class Users(Resource):
    def post(self):
        args = parser.parse_args()
        users.append(args['user'])
        print()
        return users, 201

    def get(self):
        args = parser.parse_args()
        return args['user']

api.add_resource(TodoList, '/api/todos')
api.add_resource(Todo, '/api/todos/<todo_id>')
api.add_resource(Users, '/api/users')


if __name__ == '__main__':
    app.run(port="5002")