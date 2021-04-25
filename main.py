from flask import Flask

app = Flask(__name__)


@app.route('/search/<key>')
def search(key):
    key_or_code = "key"
    if key.isdigit():
        key_or_code = 'code'


if __name__ == '__main__':
    print(app.url_map)
    print(app.view_functions)
    app.run(debug=True)
