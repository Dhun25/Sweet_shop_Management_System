from Sweet import Sweet
from SweetShop import SweetShop
import os

TEST_DATA_FILE = 'test_sweets.json'
if os.path.exists(TEST_DATA_FILE):
    os.remove(TEST_DATA_FILE)

shop = SweetShop(data_file=TEST_DATA_FILE)

# Add
sweet = Sweet("1", "Ladoo", "Traditional", 10, 20)
shop.add_sweet(sweet)
assert len(shop.get_sweets()) == 1

# Purchase
assert shop.purchase_sweet("1", 5)
assert shop.find_sweet_by_id("1").quantity == 15

# Restock
assert shop.restock_sweet("1", 10)
assert shop.find_sweet_by_id("1").quantity == 25

# Delete
assert shop.delete_sweet("1")
assert shop.find_sweet_by_id("1") is None

print("✅ All tests passed!")
