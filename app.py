from flask import Flask
from flask_session import Session
from flask_login import LoginManager
from app.routes_home import home_bp
from app.routes_login import login_bp

def create_app():
    app = Flask(__name__, template_folder="app/templates")

    app.config["SECRET_KEY"] = "dev"
    app.config["SESSION_TYPE"] = "filesystem"

    Session(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    app.register_blueprint(home_bp)
    app.register_blueprint(login_bp)

    return app
