import json

class Restaurant:
    def __init__(self, id, categories, name, location, phone, display_phone, rating, price):
        self.id = id
        self.cuisine = categories
        self.name = name
        self.location = ', '.join(location['display_address'])
        self.phone = phone
        self.display_phone = display_phone
        self.rating = rating
        self.price = price

    @classmethod
    def from_json(cls, json_string):
        dictionary = json.loads(json_string)
        restaurant_list = []
        for r in dictionary['businesses']:
            categories = []
            for values in r['categories']:
                categories.append(values['title'])
            if r.get('price') != None:
                restaurant_list.append(Restaurant(r['id'], r['name'], categories, r['location'], r['phone'], r['display_phone'], r['rating'], r['price']))
            else:
                continue
            return restaurant_list
