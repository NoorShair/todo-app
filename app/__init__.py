from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate=Migrate(app, db)

from app.todo.views import todo_blueprint

app.register_blueprint(todo_blueprint, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True)

