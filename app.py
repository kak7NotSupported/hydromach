import subprocess
from flask import Flask
from flask_pymongo import PyMongo

# Запуск MongoDB
mongod_process = subprocess.Popen(["mongodb/bin/mongod.exe", "--dbpath", "mongodb`/data"])

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

if __name__ == "__main__":
    try:
        app.run()
    finally:
        mongod_process.terminate()
