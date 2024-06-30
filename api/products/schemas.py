from marshmallow import Schema, fields

# Define the schemas
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    price = fields.Float(required=True)

class ProductQuerySchema(Schema):
    name = fields.Str()