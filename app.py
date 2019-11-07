from quart import Quart 
from config import config
from quart_cors import cors

app = Quart(__name__)
app =cors(app,allow_origin="*"))

@app.route('/')
async def hello():
    return 'hello'

app.run(config["host"])