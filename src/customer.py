class Customer:
    
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness_level = 0
        
    def remove_amount(self, amount):
        self.wallet -= amount
        
    def increase_drunkenness(self, alcohol_level):
        self.drunkenness_level += alcohol_level
        
    def reduce_drunkenness(self, rejuvenation_level):
        if self.drunkenness_level > rejuvenation_level:
            self.drunkenness_level -= rejuvenation_level
        else:
            self.drunkenness_level = 0