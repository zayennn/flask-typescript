from flask import Flask
from blueprints.home.routes import home_bp
from blueprints.dashboard.routes import dashboard_bp

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(dashboard_bp)
