import json

class Restaurant:
    def __init__(self, id, name, categories, location, phone, display_phone, price, rating):
        self.id = id
        self.name = name
        self.cuisine = categories
        self.price = price
        self.rating = rating
        self.location = ' '.join(location['display_address'])
        self.display_phone = display_phone
        self.phone = phone

    @classmethod
    def from_json(cls, json_string):
        dict = json.loads(json_string)
        restaurant_list = []
        for u in dict['businesses']:
            categories = []
            for dic in u['categories']:
                categories.append(dic['title'])
            if u.get("price") != None:
                restaurant_list.append(Restaurant(u['id'], u['name'], categories, u['location'], u['phone'], u['display_phone'], u['price'], u['rating']))
            else:
                continue
        return restaurant_list
