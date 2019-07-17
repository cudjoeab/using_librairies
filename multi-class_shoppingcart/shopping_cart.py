from product import Product

class Shopping_cart:
    def __init__(self, name):
        self.name = name
        self.cart = []
    
    def __str__(self):
        return f"{self.name}'s cart: {self.cart}"
    
    def add_to_cart(self, product):
        self.cart.append(product) 
        return f'{product.name} added to cart. Your cart: {self.cart}.'

    def remove_from_cart(self, product):
        self.cart.pop(product)
        return f'{product.name} removed from cart. Your cart: {self.cart}.' 
    
    def total_before_tax(self):
        subtotal = 0
        for product in self.cart:
            subtotal += product.base_price 
        return subtotal
    
    def total_after_tax(self):
        total = 0
        for product in self.cart:
            total += product.price_after_tax
        return total 

        
        
    

    

