# Coin Flip Streaks

# For this exercise, we’ll try doing an experiment. If you flip a coin 100 times and write down an H for each heads and a T for each tails, you’ll create a list that looks like T T T T H H H H T T. If you ask a human to make up 100 random coin flips, you’ll probably end up with alternating heads-tails results like H T H T H H T H T T—which looks random (to humans), but isn’t mathematically random. A human will almost never write down a streak of six heads or six tails in a row, even though it is highly likely to happen in truly random coin flips. Humans are predictably bad at being random.

# Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of 100 heads and tails. Your program should break up the experiment into two parts: the first part generates a list of 100 randomly selected 'H' and 'T' values, and the second part checks if there is a streak in it. Put all of this code in a loop that repeats the experiment 10,000 times so that you can find out what percentage of the coin flips contains a streak of six heads or six tails in a row. As a hint, the function call random.randint(0, 1) will return a 0 value 50 percent of the time and a 1 value the other 50 percent of the time.


import random
number_of_streaks = 0
for experiment_number in range(10000): # Run 10000 experiments total
    # Code that creates a list of 100 'heads' and 'tails' value:
    store1 = []
    for chances in range(100):
        purpose = random.randint(0,1)
        if purpose == 1:
            store1.append('Heads')
        else:
            store1.append('Tails')
    
    # Code that checks if a there is a streak of 6 heads or tails in a row:(TOOK THE HELP OF AI)
    
    streak_count = 1
    has_streak = False # second check with Boolean, especially for the 6 streak of Heads or Tails
    for item in range(0, len(store1)-1):
        if store1[item] == store1[item-1]:
            streak_count += 1
        else:
            streak_count = 1 # reset the streak count to 1, to charge the streak from 1 to the goal of 6, and so on..
        if streak_count == 6:
            has_streak = True
            break
        
    if has_streak:
        number_of_streaks += 1

result = (number_of_streaks/100)
print(str(result) + '%')