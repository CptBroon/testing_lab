import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Sex on the beach", 15)
    
    def test_drink_has_name(self):
        self.assertEqual("Sex on the beach", self.drink.name)
        
    def test_drink_has_price(self):
        self.assertEqual(15, self.drink.price)