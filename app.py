import os
from flask import Flask
from models.user import User
from dotenv import load_dotenv
from database import db

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

db.init_app(app)

@app.route("/ola")
def hello_world():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)