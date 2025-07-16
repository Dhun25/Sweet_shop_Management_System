import unittest
from src.sweet import Sweet
from src.sweet_shop import SweetShop

class TestSweetShop(unittest.TestCase):

    def setUp(self):
        self.shop = SweetShop()
        self.sweet1 = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
        self.sweet2 = Sweet(1002, "Gajar Halwa", "Vegetable-Based", 30, 15)
        self.shop.add_sweet(self.sweet1)
        self.shop.add_sweet(self.sweet2)

    def test_add_duplicate(self):
        with self.assertRaises(ValueError):
            self.shop.add_sweet(self.sweet1)

    def test_delete_sweet(self):
        self.shop.delete_sweet(1002)
        self.assertEqual(len(self.shop.inventory), 1)

    def test_view_sweets(self):
        sweets = self.shop.view_sweets()
        self.assertEqual(len(sweets), 2)

    def test_search_by_name(self):
        results = self.shop.search_sweets(name="kaju")
        self.assertEqual(len(results), 1)

    def test_search_by_category(self):
        results = self.shop.search_sweets(category="nut")
        self.assertEqual(len(results), 1)

    def test_search_by_price(self):
        results = self.shop.search_sweets(price_range=(10, 40))
        self.assertEqual(len(results), 1)

    def test_purchase_sweet(self):
        self.shop.purchase_sweet(1001, 5)
        self.assertEqual(self.shop.inventory[1001].quantity, 15)

    def test_purchase_insufficient(self):
        with self.assertRaises(ValueError):
            self.shop.purchase_sweet(1001, 100)

    def test_restock_sweet(self):
        self.shop.restock_sweet(1002, 10)
        self.assertEqual(self.shop.inventory[1002].quantity, 25)

if __name__ == "__main__":
    unittest.main()
