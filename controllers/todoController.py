from models import todo
from quart import request


todos = todo.Todo()

async def add_todo():
    data =  request.get_json()
    
    title = data['title']
    body  = data['body']
    print(title, body)
    await todos.create({'title': title, 'body':body})
    return "Created"



