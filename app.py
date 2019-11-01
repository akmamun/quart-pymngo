from quart import Quart 
from config import config
app = Quart(__name__)

@app.route('/')
async def hello():
    return 'hello'

app.run(config["host"])