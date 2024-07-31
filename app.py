from flask import Flask
import os
from routes import pages
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    client=MongoClient(os.environ.get('MONGODB_URI'))
    app.db=client.habittracker
    app.register_blueprint(pages)

    return app