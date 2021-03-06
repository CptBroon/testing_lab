import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Sex on the beach", 15, 3)
    
    def test_drink_has_name(self):
        self.assertEqual("Sex on the beach", self.drink.name)
        
    def test_drink_has_price(self):
        self.assertEqual(15, self.drink.price)
        
    def test_drink_has_alcohol_level(self):
        self.assertEqual(3, self.drink.alcohol_level)