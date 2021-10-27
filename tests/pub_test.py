import unittest
from src.pub import *
from src.drink import *

class TestPub(unittest.TestCase):
    
    def setUp(self):
        drink1 = Drink("Sex on the beach", 15)
        drink2 = Drink("Tennets", 4)
        drink3 = Drink("White wine", 6)
        drinks_list = [drink1, drink2, drink3]
        self.pub = Pub("The Winchester", 1000, drinks_list)
        
    def test_pub_has_name(self):
        self.assertEqual("The Winchester", self.pub.name)
        
    def test_pub_has_till(self):
        self.assertEqual(1000, self.pub.till)
        
    def test_pub_has_drinks_list(self):
        self.assertNotEqual(0, len(self.pub.drinks_list))