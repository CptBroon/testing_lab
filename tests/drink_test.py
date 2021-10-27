import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    
    def test_drink_has_name(self):
        drink = Drink("Sex on the beach", 15)
        self.assertEqual("Sex on the beach", drink.name)
        
    def test_drink_has_price(self):
        drink = Drink("Sex on the beach", 15)
        self.assertEqual(15, drink.price)