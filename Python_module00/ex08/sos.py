# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rertzer <rertzer@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/14 13:08:04 by rertzer           #+#    #+#              #
#    Updated: 2023/05/14 14:10:55 by rertzer          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/",
        }

if len(sys.argv) == 1:
    print("Error: an argument is required")
    sys.exit(1)

text = ''
for i in range(1, len(sys.argv)):
    text = text + sys.argv[i] + ' '
text = text[:-1];

if not text[1].replace(' ', '').isalnum():
        print("Error: the argument string must have only space or alphanumeric characters")
        sys.exit(1)

text = text.upper()
new_text = ''
for c in text:
    new_text = new_text + morse[c] + ' '
new_text = new_text[:-1]
print ("{}".format(new_text))
