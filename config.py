import os

class AppConfig:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://krishnan:krishnan@localhost/homeworkdb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    API_TITLE = 'Flask-Smorest API'
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.3'
    OPENAPI_URL_PREFIX = '/docs'
    OPENAPI_SWAGGER_UI_PATH = '/'
    OPENAPI_SWAGGER_UI_URL = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist'