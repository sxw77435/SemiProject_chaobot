from flask import Flask 
from flask_sqlalchemy import SQLAlchemy #pip install flask_sqlalchemy
from config import Config

app = Flask(__name__, static_folder='static', template_folder='templates')

app.config.from_object(Config)
db = SQLAlchemy(app)

from app.suspend import routes as suspend_routes
app.register_blueprint(suspend_routes.suspend_bp)

from app.update import routes as update_routes
app.register_blueprint(update_routes.update_bp)

from app.test import routes as test_routes
app.register_blueprint(test_routes.test_bp)

from app.acception import routes as acception_routes
app.register_blueprint(acception_routes.acception_bp)

from app.modeling import modeling as modeling_routes
app.register_blueprint(modeling_routes.modeling_bp)


