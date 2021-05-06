from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_migrate import Migrate
from flask_basicauth import BasicAuth
from app.config import Config

admin = Admin(name='bla', template_mode='bootstrap4')
migrate = Migrate()
db = SQLAlchemy()
basic_auth = BasicAuth()


def register_blueprint(app):
    from app.routes import web
    app.register_blueprint(web)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    admin.init_app(app)
    migrate.init_app(app, db)
    basic_auth.init_app(app)
    register_blueprint(app)
    return app
