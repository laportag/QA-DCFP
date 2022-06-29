from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
# app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI") 
# "mysql+pymysql://root:root@34.163.156.75:3306/crud-garden"
# "sqlite:///data.db"
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")


db = SQLAlchemy(app)


from application import routes