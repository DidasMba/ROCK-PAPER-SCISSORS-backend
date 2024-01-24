# Importing necessary modules from the Flask framework

from flask import Flask
from flask_sqlalchemy import SQLAlchemy  

from flask_migrate import Migrate



# Creating a Flask web application instance
app = Flask(__name__)

# Configuring the SQLAlchemy database connection for the Flask app
# 'sqlite:///site.db' specifies the SQLite database file named 'site.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Disabling Flask-SQLAlchemy modification tracking feature for better performance
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Creating a SQLAlchemy database instance and associating it with the Flask app
db = SQLAlchemy(app)
migrate = Migrate(app, db)
erwre
