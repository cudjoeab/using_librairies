class Shopping_cart:
    def __init__(self, name):
        self.name = name
        self.cart = []
    
    def add_to_cart(self, product):
        self.cart.append(product) 
        return self.cart

    def remove_from_cart(self, product):
        self.cart.pop(product)
        return self.cart 
    
    def subtotal(self, cart):
        for product in cart:
            subtoal_sum += self.base_price 
        return subtoal_sum 
    
    def total_tax(self, cart):
        for product in cart:
            total_tax_sum += self.total_tax
        return total_tax_sum
    
    def total(self, cart):
        total = subtotal_sum + total_tax_sum 
        return 

        
        
    

    

