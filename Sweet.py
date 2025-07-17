class Sweet:
    def __init__(self, id, name, category, price, quantity):
        self.id = str(id)
        self.name = name
        self.category = category
        self.price = float(price)
        self.quantity = int(quantity)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "quantity": self.quantity
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            name=data["name"],
            category=data["category"],
            price=data["price"],
            quantity=data["quantity"]
        )
