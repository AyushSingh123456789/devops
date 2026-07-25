def product(**kwargs):
    for key, value in kwargs.items():
        print(key + " : " + value)
    
    
product(name="iphone", price="700")
product(name="iphone", price="1000", descr="this is an iphone")