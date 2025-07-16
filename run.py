from src.sweet import Sweet
from src.sweet_shop import SweetShop

shop = SweetShop()
shop.add_sweet(Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20))
shop.add_sweet(Sweet(1002, "Gajar Halwa", "Vegetable-Based", 30, 15))
shop.add_sweet(Sweet(1003, "Gulab Jamun", "Milk-Based", 10, 50))

print("🎉 Available Sweets in Shop:")
for sweet in shop.view_sweets():
    print(sweet)
