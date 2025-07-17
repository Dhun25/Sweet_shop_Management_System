import json
from Sweet import Sweet

class SweetShop:
    def __init__(self, data_file='sweets.json'):
        self.data_file = data_file
        self.sweets = []
        self.load_sweets()

    def add_sweet(self, sweet):
        self.sweets.append(sweet)
        self.save_sweets()

    def get_sweets(self):
        return self.sweets

    def find_sweet_by_id(self, sweet_id):
        for sweet in self.sweets:
            if str(sweet.id) == str(sweet_id):
                return sweet
        return None

    def delete_sweet(self, sweet_id):
        sweet = self.find_sweet_by_id(sweet_id)
        if sweet:
            self.sweets.remove(sweet)
            self.save_sweets()
            return True
        return False

    def purchase_sweet(self, sweet_id, qty):
        sweet = self.find_sweet_by_id(sweet_id)
        if sweet and sweet.quantity >= qty:
            sweet.quantity -= qty
            self.save_sweets()
            return True
        return False

    def restock_sweet(self, sweet_id, qty):
        sweet = self.find_sweet_by_id(sweet_id)
        if sweet:
            sweet.quantity += qty
            self.save_sweets()
            return True
        return False

    def search_sweets(self, name="", category="", min_price=0, max_price=float("inf")):
        results = []
        for sweet in self.sweets:
            if name.lower() not in sweet.name.lower():
                continue
            if category.lower() not in sweet.category.lower():
                continue
            if sweet.price < min_price or sweet.price > max_price:
                continue
            results.append(sweet)
        return results

    def save_sweets(self):
        with open(self.data_file, 'w') as f:
            json.dump([s.to_dict() for s in self.sweets], f, indent=4)

    def load_sweets(self):
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.sweets = [Sweet.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.sweets = []
