from quart import Quart 
from config import config
from quart_cors import cors
from controllers.todoController import add_todo
app = Quart(__name__)
app =cors(app,allow_origin="*")

app.add_url_rule('/add', add_todo(),methods=['POST'])


app.run(config["host"])