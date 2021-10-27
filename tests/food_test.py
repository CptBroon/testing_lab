import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    
    def setUp(self):
        self.food1 = Food("Lasagna", 7, 5)
    
    def test_food_has_name(self):
        self.assertEqual("Lasagna", self.food1.name)
        
    def test_food_has_price(self):
        self.assertEqual(7, self.food1.price)
        
    def test_food_has_rejuvenation_level(self):
        self.assertEqual(5, self.food1.rejuvenation_level)