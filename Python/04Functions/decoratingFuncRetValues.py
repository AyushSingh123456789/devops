def summer_discount_decorator(func):
    def wrapper(price):
        func(price)
        return func(price/2)
    return wrapper

@summer_discount_decorator
def total(price):
    return price

result = total(100)
print(result)