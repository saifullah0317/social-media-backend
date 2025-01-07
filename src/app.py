from flask import Flask
from config.base import Config
from database import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
