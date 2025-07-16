# src/sweet_shop.py

from src.sweet import Sweet

class SweetShop:
    def __init__(self):
        self.inventory = {}

    def add_sweet(self, sweet):
        if sweet.id in self.inventory:
            raise ValueError("Sweet with this ID already exists.")
        self.inventory[sweet.id] = sweet

    def delete_sweet(self, sweet_id):
        if sweet_id not in self.inventory:
            raise ValueError("Sweet not found.")
        del self.inventory[sweet_id]

    def view_sweets(self):
        return list(self.inventory.values())

    def search_sweets(self, name=None, category=None, price_range=None):
        results = self.inventory.values()
        if name:
            results = filter(lambda s: name.lower() in s.name.lower(), results)
        if category:
            results = filter(lambda s: category.lower() == s.category.lower(), results)
        if price_range:
            min_price, max_price = price_range
            results = filter(lambda s: min_price <= s.price <= max_price, results)
        return list(results)

    def purchase_sweet(self, sweet_id, quantity):
        if sweet_id not in self.inventory:
            raise ValueError("Sweet not found.")
        sweet = self.inventory[sweet_id]
        if sweet.quantity < quantity:
            raise ValueError("Not enough stock.")
        sweet.quantity -= quantity

    def restock_sweet(self, sweet_id, quantity):
        if sweet_id not in self.inventory:
            raise ValueError("Sweet not found.")
        self.inventory[sweet_id].quantity += quantity
