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


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['API_TITLE'] = 'Flask-Smorest API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.0.3'
app.config['OPENAPI_URL_PREFIX'] = '/docs'
app.config['OPENAPI_SWAGGER_UI_PATH'] = '/'
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

api = Api(app)
api.register_blueprint(products_blp)
init_products()

app.run(debug=True, port=5000, host="127.0.0.1")