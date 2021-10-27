from src.customer import *
from src.drink import *

class Pub:
    
    def __init__(self, name, till, drinks_list):
        self.name = name
        self.till = till
        self.drinks_list = drinks_list
        
    def can_customer_afford_drink(self, customer, drink):
        if customer.wallet >= drink.price:
            return True
        
    def add_amount_to_till(self, amount):
        self.till += amount
        
    def sell_drink(self, customer, drink):
        if self.can_customer_afford_drink(customer, drink) == True:
            self.add_amount_to_till(drink.price)
            customer.remove_amount(drink.price)