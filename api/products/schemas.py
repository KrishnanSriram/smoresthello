from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.product import Product
# Define the schemas
# class ProductSchema(Schema):
#     id = fields.Int(dump_only=True)
#     name = fields.Str(required=True)
#     description = fields.Str()
#     price = fields.Float(required=True)

class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True

class ProductQuerySchema(Schema):
    # products = List(Nested(Product))
    product = fields.Nested(ProductSchema)
    status = fields.String()


class ProductListSchema(Schema):
    # products = List(Nested(Product))
    products = fields.List(fields.Nested(ProductSchema))
    status = fields.String()
    count = fields.Integer()