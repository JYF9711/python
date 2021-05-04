from sanic import Sanic
from sanic.response import json
app=Sanic(__name__)
@app.route("/")
async def test(request):
    return json({"Hello":"world"})
app.run(host="192.168.1.9",port=8000)