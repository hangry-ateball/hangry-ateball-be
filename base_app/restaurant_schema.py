from marshmallow_jsonapi import Schema, fields

class RestaurantSchema(Schema):
    id = fields.Str()
    metadata = fields.ResourceMeta()
    cuisine = fields.List(fields.Str)
    name = fields.Str()
    location = fields.Str()
    phone = fields.Str()
    display_phone = fields.Str()
    rating = fields.Float()
    price = fields.Str()
    is_closed = fields.Bool()

    class Meta:
        type_ = 'restaurants'
