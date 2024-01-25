# Inside app/__init__.py
from flask import Flask
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Import routes and services
from .routes import auth, game, user
from .services import auth_service, game_service
