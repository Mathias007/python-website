from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdf-asdf-asdf-asdf' # to change in production build

    return app

