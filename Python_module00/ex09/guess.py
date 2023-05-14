# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rertzer <rertzer@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/14 14:15:18 by rertzer           #+#    #+#              #
#    Updated: 2023/05/14 14:40:10 by rertzer          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
import sys
import string

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.\n Good luck!")

attempt = 0
found = False
nb = random.randint(1, 99)

while not found:
    guess = str(input("What's your guess between 1 and 99? "))
    attempt = attempt + 1
    if guess == 'exit':
        print("Goodbye!")
        exit()
    if guess.isnumeric():
        gnb = int(guess)
        if gnb == nb:
            found = True
        elif gnb > nb:
            print("Too high!")
        else:
            print("Too low!")
if nb == 42:
    print("42 is the ultimate answer to, well, everything, etc.")
if attempt == 0:
    print("Congratulations! You got it on your first try!")
else:
    print("Congratulations, you've got it!")
    print("You won in {} attempts".format(attempt))
