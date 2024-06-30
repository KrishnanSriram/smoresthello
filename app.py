from flask import Flask
from flask_smorest import Api
import logging
import sys
from api.products.routes import blp as products_blp, init_products

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Define the log format
    handlers=[
        logging.StreamHandler(sys.stdout)  # Redirect logs to standard output
    ]
)
class Main:
    def __init__(self):
        self.app = Flask(__name__)
        logging.info("Created app")
        self.init_app()
        self.api = Api(self.app)

    def init_app(self):
        self.app.config['PROPAGATE_EXCEPTIONS'] = True
        self.app.config['API_TITLE'] = 'Flask-Smorest API'
        self.app.config['API_VERSION'] = 'v1'
        self.app.config['OPENAPI_VERSION'] = '3.0.3'
        self.app.config['OPENAPI_URL_PREFIX'] = '/docs'
        self.app.config['OPENAPI_SWAGGER_UI_PATH'] = '/'
        self.app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
        logging.info("Initialized app")

    def add_blueprint(self, bp):
        self.api.register_blueprint(bp)
        logging.info("Added BP")

    def run(self):
        logging.info("Running app.....")
        self.app.run(debug=True, port=5000, host="127.0.0.1")
        logging.info("App Stoppped!!")

# if __name__ == "__main__":
# MAIN SECTION
main = Main()
main.add_blueprint(products_blp)
init_products()
main.run()