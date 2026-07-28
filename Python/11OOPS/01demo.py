    
# p1 = Product() 
# print(p1.quantity)

# p1, p2 -> product object or instances of the class "Product".

class Product:
    quantity = 200 # class attribute
    
    def __init__(self, name, price): 
        # constructor decl
        # self is the ref. to the obj we're working with.
        self.name = name # instance attribute
        self.price = price # instance attribute

p1 = Product("phone", "300")
print(p1.name)
print(p1.price)

p2 = Product("laptop", "900")
print(p2.name)
print(p2.price)