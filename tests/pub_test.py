import unittest
from src.food import Food
from src.pub import *
from src.drink import *

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Keith", 50, 49)
        self.drink1 = Drink("Sex on the beach", 15, 3)
        self.drink2 = Drink("Tennets", 4, 1)
        self.drink3 = Drink("White wine", 6, 2)
        drinks_list = [self.drink1, self.drink2, self.drink3]
        self.pub = Pub("The Winchester", 1000, drinks_list)
        self.food = Food("Lasagna", 7, 5)
        
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
        self.customer.increase_drunkenness(self.drink1.alcohol_level)
        
        self.assertEqual(35, self.customer.wallet)
        self.assertEqual(1015, self.pub.till)
        self.assertEqual(3, self.customer.drunkenness_level)
        
    def test_check_customer_over_18(self):
        self.assertEqual(True, self.pub.check_customer_over_18(self.customer))
        
    def test_sell_food(self):
        self.pub.can_customer_afford_food(self.customer, self.food)
        self.assertEqual(True, self.pub.can_customer_afford_food(self.customer, self.food))
        
        self.customer.remove_amount(self.food.price)
        self.pub.add_amount_to_till(self.food.price)
        self.customer.reduce_drunkenness(self.food.rejuvenation_level)
        
        self.assertEqual(43, self.customer.wallet)
        self.assertEqual(1007, self.pub.till)
        self.assertEqual(0, self.customer.drunkenness_level)