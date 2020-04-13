import json

class Restaurant:
    def __init__(self, id, name, categories, location, phone, display_phone, rating, price, is_closed, photos):
        self.id = id
        self.cuisine = categories
        self.name = name
        self.location = ', '.join(location['display_address'])
        self.phone = phone
        self.display_phone = display_phone
        self.rating = rating
        self.price = price
        self.is_closed = is_closed
        self.photos = photos

    @classmethod
    def from_json(cls, json_string):
        info = json.loads(json_string)
        categories = []
        for i in info['categories']:
            categories.append(i['title'])
        return cls(
            info['id'],
            info['name'],
            categories,
            info['location'],
            info['phone'],
            info['display_phone'],
            info['rating'],
            info['price'],
            info['is_closed'],
            info['photos'])
