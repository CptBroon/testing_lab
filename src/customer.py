class Customer:
    
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        
    def remove_amount(self, amount):
        self.wallet -= amount