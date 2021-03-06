import unittest

from src.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Keith", 50, 49)
    
    def test_customer_has_name(self):
        self.assertEqual("Keith", self.customer.name)
        
    def test_customer_has_wallet(self):
        self.assertEqual(50, self.customer.wallet)
        
    def test_customer_has_age(self):
        self.assertEqual(49, self.customer.age)
        
    def test_customer_remove_amount(self):
        self.customer.remove_amount(10)
        self.assertEqual(40, self.customer.wallet)
        
    def test_increase_drunkenness(self):
        self.customer.increase_drunkenness(4)
        self.assertEqual(4, self.customer.drunkenness_level)