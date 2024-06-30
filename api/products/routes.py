from flask.views import MethodView
from flask_smorest import Blueprint
from api.products.schemas import ProductSchema
import logging

# Create the Blueprint
blp = Blueprint('products', __name__, url_prefix='/api/products', description='Product ops')

# In-memory storage for items
products = []

def init_products():
    logging.info("Initialize products...")
    products.append({"id": 1, "name": "Product 1", "price": 10.01, "description": "Description 1"})
    products.append({"id": 2, "name": "Product 2", "price": 20.01, "description": "Description 2"})
    products.append({"id": 3, "name": "Product 3", "price": 30.01, "description": "Description 3"})

@blp.route('/')
class ProductDefaultOps(MethodView):

    @blp.response(200, ProductSchema(many=True), description="List all products. Pagination is not supported in this version")
    def get(self):
        logging.info("List all products")
        """List all items"""
        return products

    @blp.arguments(ProductSchema)
    @blp.response(201, ProductSchema, description="Add a new product")
    def post(self, new_product):
        logging.info("Add a new product")
        logging.info(new_product)
        """Create a new item"""
        new_product['id'] = len(products) + 1
        products.append(new_product)
        return new_product, 201


@blp.route('/<int:product_id>')
class ProductIDOps(MethodView):
    @blp.response(200, ProductSchema(many=False), description="Query products by ID")
    @blp.response(400, description="Unidentified product ID")
    def get(self, product_id):
        """List all items"""
        logging.info("Find a product with ID - {}".format(product_id))
        for product in products:
            if product["id"] == product_id:
                logging.info(product)
                return product, 200
        logging.info("Product was NOT found")
        return {"message": "Unidentified product ID"}, 400

    @blp.response(200, description="Delete product by ID")
    @blp.response(400, description="Unidentified product ID")
    def delete(self, product_id):
        logging.info("Delete product with ID - {}".format(product_id))
        for product in products:
            if product["id"] == product_id:
                products.pop(product_id -1)
                return product, 200

        logging.info("Product with ID - {} was not found".format(product_id))
        return {"message": "Unidentified product ID"}, 400

