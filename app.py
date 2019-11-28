from flask import Flask
from database import db
from user.blueprint import user_blueprint

from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

db.init_app(app)


app.register_blueprint(user_blueprint)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090, debug=True)
