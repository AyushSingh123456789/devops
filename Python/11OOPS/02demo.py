# Methods in OOPS: Functions declared inside a Class.

class Product:
    quantity = 400

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def summer_discount(self, discount_percent):
        self.price = self.price - (self.price * discount_percent)/100
        
p1 = Product("T-shirt", 10)
print(p1.name)
print(p1.price) # regular price
p1.summer_discount(50) # method called on the object with a 50% discount
print(p1.price) # discounted price


p2 = Product("Phone", 400)
p2.summer_discount(10) # 10% discount
print(p2.price)