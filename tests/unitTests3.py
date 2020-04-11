from http_server_mock import HttpServerMock
import requests

app = HttpServerMock(__name__, is_alive_route="/metrics")

@app.route("/", methods=["GET"])
def index():
    return "Hello world"

with app.run("localhost", 8000):
    r = requests.get("http://localhost:8000/")
