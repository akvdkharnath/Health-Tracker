from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['THREADED'] = True

cors = CORS(app)

from Project import views

