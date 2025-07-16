# run.py

from src.sweet_shop import SweetShop
from src.sweet import Sweet

shop = SweetShop()
shop.add_sweet(Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20))
shop.add_sweet(Sweet(1002, "Gajar Halwa", "Vegetable-Based", 30, 15))

print("Available Sweets:")
for sweet in shop.view_sweets():
    print(vars(sweet))
