from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from pathlib import Path
from models.base import TestClass

load_dotenv(verbose=True)
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
api = Api(app)

api.add_resource(TestClass, '/')

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port='8000',
        debug=os.getenv("DEBUG"))