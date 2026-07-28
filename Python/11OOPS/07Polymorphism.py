# Method Overriding:

class Food:
    def type(self):
        print("food")
        
class Fruit(Food):
    def type(self):
        print("fruit")
        

apple = Fruit()
print(apple.type())
# The 'type' method in Fruit Class overrides the 'type' method in Food Class, Hence "fruit" is printed.