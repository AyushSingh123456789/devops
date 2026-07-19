message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {}

for character in message: # Iterate through every single character in the 'message' string, one by one
    count.setdefault(character, 0) # # If 'character' is NOT in the dict, add it as a key with a value of 0. If it is already there, do nothing. 
    count[character] = count[character] + 1 # Increment the stored value (the count) for this character key by 1.
    # This repeats for every character, ensuring each unique character's count is accurately totaled.
print(count)


# Imp Note: How setdefault actually works: This method only sets the value to 0 if the key does not already exist in the dictionary. If the key already exists (for example, when the loop encounters the second 'I' or 't'), setdefault does absolutely nothing and simply returns the existing value. Without this check, you'd constantly overwrite your hard work and reset existing counts back to 0