def decorator(func):
    def wrapper():
        print("Wrapper upside")
        func()
        print("Wrapper downside")
    return wrapper

@decorator
def chocolate():
    print("Chocolate")
    
@decorator
def cake():
    print("Cake")
    
    
    
chocolate()
cake()