# tests/test_sweet_shop.py

import unittest
from src.sweet import Sweet
from src.sweet_shop import SweetShop

class TestSweetShop(unittest.TestCase):

    def setUp(self):
        self.shop = SweetShop()
        self.kaju = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
        self.gajar = Sweet(1002, "Gajar Halwa", "Vegetable-Based", 30, 15)
        self.gulab = Sweet(1003, "Gulab Jamun", "Milk-Based", 10, 50)
        self.shop.add_sweet(self.kaju)
        self.shop.add_sweet(self.gajar)

    def test_add_duplicate_id(self):
        with self.assertRaises(ValueError):
            self.shop.add_sweet(self.kaju)

    def test_delete_sweet(self):
        self.shop.delete_sweet(1002)
        self.assertEqual(len(self.shop.inventory), 1)

    def test_view_sweets(self):
        sweets = self.shop.view_sweets()
        self.assertEqual(len(sweets), 2)

    def test_search_by_name(self):
        results = self.shop.search_sweets(name="Kaju")
        self.assertEqual(len(results), 1)

    def test_search_by_category(self):
        results = self.shop.search_sweets(category="Nut-Based")
        self.assertEqual(len(results), 1)

    def test_search_by_price_range(self):
        results = self.shop.search_sweets(price_range=(25, 55))
        self.assertEqual(len(results), 2)

    def test_purchase_sweet(self):
        self.shop.purchase_sweet(1001, 5)
        self.assertEqual(self.shop.inventory[1001].quantity, 15)

    def test_restock_sweet(self):
        self.shop.restock_sweet(1001, 10)
        self.assertEqual(self.shop.inventory[1001].quantity, 30)

    def test_purchase_with_insufficient_stock(self):
        with self.assertRaises(ValueError):
            self.shop.purchase_sweet(1001, 100)

if __name__ == '__main__':
    unittest.main()
