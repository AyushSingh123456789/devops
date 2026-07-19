import random
random_number = random.randint(1,6)


def get_random_dice_roll():
    # Returns a random integer from 1 to 6
    return random_number

print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())

# Why does the function call return the same number?

# So the program starts and the random_number variable stores a generated random number b/w 1 and 6, function is created, and then the function is called, so that generated number stored inside the variable 'random_number' is returned and stored inside the function in 'random number'. So, how many ever times this function is called while we run this program once, it'll print that same exact random value. But the repeated number is not guaranteed to be the exact same once when we run this program again and again.#
