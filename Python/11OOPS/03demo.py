# Functional Programming way of writing Code:

# def product_data():
#     product_name = input("Enter the name of the product: ")
#     product_price= input("Enter price of the product: ")
#     print(product_name)
#     print(product_price)
    
# product_data()

# Object Oriented way of writing Code:

class Product:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    # getter method to get data from user:
    def get_data(self):
        self.name = input("Enter the name of the product: ")
        self.price = input("Enter the price of the product: ")
    
    # putter method to display the accepted data from the getter method:
    def put_data(self):
        print(self.name)
        print(self.price)
        
p1 = Product("", "")
p1.get_data()
p1.put_data()
        