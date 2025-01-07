from flask import Flask
from config.base import Config

app = Flask(__name__)
app.config.from_object(Config)

if __name__ == '__main__':
    app.run(debug=True)
