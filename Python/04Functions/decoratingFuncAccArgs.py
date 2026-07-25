def decorator(func):
    def wrapper(*args, **kwargs):
        print('Wrapper upside')
        func(*args, **kwargs)
        print('Wrapper downside')
    return wrapper

@decorator
def chocolate():
    print('Chocolate')
  
@decorator  
def cake(name):
    print("Cake" + name)
    
    
chocolate()
cake("ayush")