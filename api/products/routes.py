from flask.views import MethodView
from flask_smorest import Blueprint
from api.products.schemas import ProductSchema, ProductQuerySchema, ProductListSchema
import logging
from models.product import Product, db
# Create the Blueprint
blp = Blueprint('products', __name__, url_prefix='/api/products', description='Product ops')


@blp.route('/')
class ProductDefaultOps(MethodView):

    @blp.response(200, ProductListSchema, description="List all products. Pagination is not supported in this version")
    def get(self):
        logging.info("List all products")
        """List all items"""
        products = Product.query.all()
        logging.info("Found {} products".format(len(products)))
        # return products
        return { 'status': 'success', 'products': products, 'count': len(products)}, 200

    @blp.arguments(ProductSchema)
    @blp.response(201, ProductSchema, description="Add a new product")
    def post(self, new_product):
        logging.info("Add a new product")
        logging.info(new_product)
        """Create a new item"""
        product = Product(name = new_product["name"], description = new_product["description"], price=new_product["price"])
        db.session.add(product)
        db.session.commit()
        return product, 201


@blp.route('/<int:product_id>')
class ProductIDOps(MethodView):
    @blp.response(200, ProductQuerySchema, description="Query products by ID")
    # @blp.response(404, description="Unidentified product ID")
    def get(self, product_id):
        """List all items"""
        logging.info("Find a product with ID - {}".format(product_id))
        product = Product.query.get(product_id)
        logging.info(product)
        if product is None: 
            return { 'status': 'failed', 'product': None}, 404
        return { 'status': 'success', 'product': product}, 200

    @blp.response(204, description="Product deleted successfully")
    @blp.response(404, description="Unidentified product ID or deletetion issues")
    def delete(self, product_id):
        logging.info("Delete product with ID - {}".format(product_id))
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return '', 204

