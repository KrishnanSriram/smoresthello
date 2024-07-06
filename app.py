from flask import Flask
from flask_smorest import Api
import logging
import sys
from api.products.routes import blp as products_blp, init_products
from config import AppConfig

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Define the log format
    handlers=[
        logging.StreamHandler(sys.stdout)  # Redirect logs to standard output
    ]
)


app = Flask(__name__)
app.config.from_object(AppConfig)

api = Api(app)
api.register_blueprint(products_blp)
init_products()

app.run(debug=True, port=5000, host="127.0.0.1")