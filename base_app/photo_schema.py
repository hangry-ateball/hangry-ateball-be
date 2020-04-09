from marshmallow_jsonapi import Schema, fields

class PhotoSchema(Schema):
    id = fields.Str()
    metadata = fields.ResourceMeta()
    photos = fields.List(fields.Str)

    class Meta:
        type_ = 'photos'
