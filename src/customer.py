class Customer:
    
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        
    def remove_amount(self, amount):
        self.wallet -= amount