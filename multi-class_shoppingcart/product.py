# create class for products 
# can be imported into shopping cart 

class Product: 

    def __init__(self, name, base_price, tax_rate): 
        self.name = name
        self.base_price = base_price
        self.tax_rate = tax_rate

    def calculate_tax(self, base_price, tax_rate):
        tax =  self.base_price * self.tax_rate   
        return tax 
    
    def price_after_tax(self): 
        price = self.base_price + self.tax
        return price 
    

apples = Product('apples', 1, 0.08)
chips = Product('chips', 4, 0.08)
cheese = Product('cheese', 6, 0.08)
salsa = Product('salsa', 5, 0.08)
soda = Product('soda', 3, 0.08)


