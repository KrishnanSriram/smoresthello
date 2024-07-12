from flask import Flask
from flask_smorest import Api
import logging
import sys
from api.products.routes import blp as products_blp
from config import Config
from flask_sqlalchemy import SQLAlchemy
from db import db
# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Define the log format
    handlers=[
        logging.StreamHandler(sys.stdout)  # Redirect logs to standard output
    ]
)


app = Flask(__name__)
app.config.from_object(Config)
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

# Initialize extensions
db.init_app(app)
with app.app_context():
    db.create_all()

api = Api(app)
api.register_blueprint(products_blp)

app.run(debug=True, port=5000, host="127.0.0.1")