from models import todo
from quart import request, jsonify

todos = todo.Todo()



async def get():
    todo = await todos.find({})
    return jsonify(todo)


async def add_todo():
    req = await request.json
    title = req['title']
    body = req['body']
    await todos.create({'title': title, 'body': body})
    return jsonify(dict(message = 'Successfully Created.'), 201) 

async def delete(id):
    req = await request.json
    await todos.delete(id)
    return jsonify(dict(message = 'Successfully Deleted.'), 204) 