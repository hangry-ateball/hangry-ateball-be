from marshmallow_jsonapi import Schema, fields
from collections import OrderedDict
from restaurant import Restaurant

class RestaurantSchema(Schema):
    id = fields.Str()
    metadata = fields.ResourceMeta()
    name = fields.Str()
    cuisine = fields.List(fields.Str)
    price = fields.Str()
    rating = fields.Float()
    location = fields.Str()
    display_phone = fields.Str()
    phone = fields.Str()

    class Meta:
        type_ = "restaurants"
        fields = ("id", "name", "cuisine", "price", "rating", "location", "display_phone", "phone")
        ordered = True


