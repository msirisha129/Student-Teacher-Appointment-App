from flask import Flask
from config import Config
from models import db
from routes.auth import auth
from routes.student import student
from routes.teacher import teacher
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
CORS(app)

app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(student, url_prefix="/student")
app.register_blueprint(teacher, url_prefix="/teacher")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)