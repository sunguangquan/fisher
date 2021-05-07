from flask import Flask
from config import DEBUG, HOST, PORT
app = Flask(__name__)


# app.add_url_rule('/', view_func=hello)
@app.route('/hello')
def hello():
    return 'Hello Flask!'


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
