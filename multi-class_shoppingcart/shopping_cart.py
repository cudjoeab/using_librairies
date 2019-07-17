from product import Product

class Shopping_cart:
    def __init__(self, name):
        self.name = name
        self.cart = []
    
    def __str__(self):
        return f"{self.name}'s cart: {self.cart}"
    
    def add_to_cart(self, product):
        self.cart.append(Product) 
        return f'{product.name} added to cart. Your cart: {self.cart}.'

    def remove_from_cart(self, product):
        self.cart.pop(product)
        return f'{product.name} removed from cart. Your cart: {self.cart}.' 
    
    def total_before_tax(self):
        subtotal = 0
        for product in self.cart:
            subtotal += product.base_price
        return f'Subtotal: {subtotal}'
    
    def total_after_tax(self):
        total = 0
        for product in self.cart:
            total += product.price_after_tax
        return f'Your total is ${total}.'


        
#The shopping carts 

abigail = Shopping_cart('Abigail')
ekua = Shopping_cart('Ekua')
dustin = Shopping_cart('Dustin')
duncan = Shopping_cart('Duncan')

#show the empty carts 
print('\nArriving at the store.\n')
print(abigail)
print(ekua)
print(dustin)
print(duncan)

#add items to carts 
print('\nFolks get the products they need:\n')
abigail.add_to_cart(Product('apples', 1, 0.08)) #not sure why products are not adding to the list via variable names 
abigail.add_to_cart(Product('cheese', 6, 0.08))
print(abigail)  

ekua.add_to_cart(Product('chips', 4, 0.08))
ekua.add_to_cart(Product('salsa', 5, 0.08))
print(ekua)

dustin.add_to_cart(Product('soda', 3, 0.08))
print(dustin)

duncan.add_to_cart(Product('apples', 1, 0.08))
duncan.add_to_cart(Product('chips', 4, 0.08))
duncan.add_to_cart(Product('cheese', 6, 0.08))
duncan.add_to_cart(Product('salsa', 5, 0.08))
duncan.add_to_cart(Product('soda', 3, 0.08))
print(duncan)

#calculate subtotal and total 
print('\nPayment at the till\n')

#for abigail
print(abigail.total_after_tax())
