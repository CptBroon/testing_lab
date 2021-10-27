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
        
    def can_customer_afford_food(self, customer, food):
        if customer.wallet >= food.price:
            return True
        
    def add_amount_to_till(self, amount):
        self.till += amount
        
    def sell_drink(self, customer, drink):
        if customer.drunkenness_level < 10:
            if self.check_customer_over_18(customer.age) == True:
                if self.can_customer_afford_drink(customer, drink) == True:
                    self.add_amount_to_till(drink.price)
                    customer.remove_amount(drink.price)
                    customer.increase_drunkenness(drink.alcohol_level)
                    
    def sell_food(self, customer, food):
        if self.can_customer_afford_food(customer, food) == True:
            self.add_amount_to_till(food.price)
            customer.remove_amount(food.price)
            customer.decrease_drunkenness(food.rejuvenation_level)
                        
    def check_customer_over_18(self, customer):
        if customer.age >= 18:
            return True