from main import app
import requests

app.app_context().push()

url = "http://127.0.0.1:5000/index"


def test_request():
    r = requests.get('http://127.0.0.1:5000/index')
    assert r.status_code == 200
    assert r.text == 'ok'
