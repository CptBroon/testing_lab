import unittest
from src.pub import *
from src.drink import *

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Keith", 50, 49)
        self.drink1 = Drink("Sex on the beach", 15)
        self.drink2 = Drink("Tennets", 4)
        self.drink3 = Drink("White wine", 6)
        drinks_list = [self.drink1, self.drink2, self.drink3]
        self.pub = Pub("The Winchester", 1000, drinks_list)
        
    def test_pub_has_name(self):
        self.assertEqual("The Winchester", self.pub.name)
        
    def test_pub_has_till(self):
        self.assertEqual(1000, self.pub.till)
        
    def test_pub_has_drinks_list(self):
        self.assertNotEqual(0, len(self.pub.drinks_list))
        
    def test_can_customer_afford_drink(self):
        self.assertEqual(True, self.pub.can_customer_afford_drink(self.customer, self.drink1))

    def test_add_amount_to_till(self):
        self.pub.add_amount_to_till(10)
        self.assertEqual(1010, self.pub.till)
        
    def test_sell_drink(self):
        self.pub.can_customer_afford_drink(self.customer, self.drink1)
        self.assertEqual(True, self.pub.can_customer_afford_drink(self.customer, self.drink1))
        
        self.customer.remove_amount(self.drink1.price)
        self.pub.add_amount_to_till(self.drink1.price)
        
        self.assertEqual(35, self.customer.wallet)
        self.assertEqual(1015, self.pub.till)
        
    def test_check_customer_over_18(self):
        self.assertEqual(True, self.pub.check_customer_over_18(self.customer))