from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.debug = True

from myapp import routes