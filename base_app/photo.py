import json

class Photo:
    def __init__(self, id, photos):
        self.id = id
        self.photos = photos

    @classmethod
    def from_json(cls, json_string):
        attributes = json.loads(json_string)
        photo_list = Photo(attributes['id'], attributes['photos'])

        return photo_list
