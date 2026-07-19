import random

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concetrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

print('Ask a yes or no question: ')
input('>')
# The above lines are just random add ons, not necessary for logic.
print(messages[random.randint(0, len(messages)-1)])