# create class for products 
# can be imported into shopping cart 

class Product: 

    def __init__(self, name, base_price, tax_rate): 
        self.name = name
        self.base_price = base_price
        self.tax_rate = tax_rate

    def __str__(self):
        return f'{self.name} costs ${self.base_price} plus tax: ${self.tax_rate}.'

    def calculate_tax(self):
        tax =  self.base_price * self.tax_rate   
        return tax 
    
    def price_after_tax(self): 
        price = self.base_price + self.calculate_tax()
        return price 
    



