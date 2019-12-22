from models import todo
from quart import request, jsonify

todos = todo.Todo()


async def get_all():
    todo = await todos.find({})
    return jsonify(todo)


async def add_todo():
    req = await request.json
    title = req['title']
    body = req['body']
    await todos.create({'title': title, 'body': body})
    return jsonify(dict(message='Successfully Created.'), 201)

async def update_todo(id):
    req = await request.json
    title = req['title']
    body = req['body']
    await todos.update(id,{'title': title, 'body': body})
    return jsonify(dict(message='Updated Created.'), 201)


async def get_one(id):
    todo = await todos.find_by_id(id)
    return jsonify(todo)


async def delete(id):
    req = await request.json
    await todos.delete(id)
    return jsonify(dict(message='Successfully Deleted.'), 204)
