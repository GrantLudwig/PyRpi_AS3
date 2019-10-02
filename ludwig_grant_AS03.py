# File Name: ludwig_grant_AS03.py
# File Path: /home/ludwigg/Python/PyRpi_AS3/ludwig_grant_AS03.py
# Run Command: sudo python3 /home/ludwigg/Python/PyRpi_AS3/ludwig_grant_AS03.py

# Grant Ludwig
# 10/04/2019
# AS.03
# Magic 8-Ball

import random

choices = ["It is certain",
           "It is decidedly so",
           "Without a doubt",
           "Yes definitely",
           "You may rely on it",
           "As I see it, yes",
           "Most likely",
           "Outlook good",
           "Yes",
           "Signs point to yes",
           "Reply hazy try again",
           "Ask again later",
           "Better not tell you now",
           "Cannot predict now",
           "Concentrate and ask again",
           "Don't count on it",
           "My reply is no",
           "My sources say no",
           "Outlook not so good",
           "Very doubtful"]

input("What do you ask the Magic 8-Ball? ")
print(random.choice(choices))