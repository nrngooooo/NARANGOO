from flask import Flask, redirect, url_for, abort
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>hello this is index page</h1>'
if __name__ == '__main__':
    app.run(debug=True)