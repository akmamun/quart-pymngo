import asyncio
from config import config

from quart import Quart
from quart_cors import cors

from controllers.todoController import add_todo, delete, get_all,get_one,update_todo

app = Quart(__name__)
app = cors(app, allow_origin="*")


app.add_url_rule('/add', view_func=add_todo, methods=['POST'])
app.add_url_rule('/', view_func=get_all)
app.add_url_rule('/todo/<id>', view_func=get_one)
app.add_url_rule('/todo/<id>', view_func=update_todo,methods=['PUT'])

app.add_url_rule('/delete/<id>', view_func=delete, methods=['DELETE'])


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app.run(config["host"], loop=loop)
