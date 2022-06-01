from flask_sqlalchemy import SQLAlchemy
from app import app, environ

DB_CONNECTION = str(environ.get('DB_CONNECTION'))
DB_HOST = str(environ.get("DB_HOST"))
DB_PORT = str(environ.get("DB_PORT"))
DB_CONNECT_ARGS_HOST = str(environ.get("DB_CONNECT_ARGS_HOST"))
DB_CONNECT_ARGS_PORT = str(environ.get("DB_CONNECT_ARGS_PORT"))
DB_DATABASE = str(environ.get("DB_DATABASE"))
DB_USERNAME = str(environ.get("DB_USERNAME"))
DB_PASSWORD = str(environ.get("DB_PASSWORD"))

# SQLAlchemy database configuration with MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONNECTION + "://" + DB_USERNAME + ":" + DB_PASSWORD + "@" + DB_HOST + "/" + DB_DATABASE

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

model = db.Model