# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rertzer <rertzer@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/14 09:56:52 by rertzer           #+#    #+#              #
#    Updated: 2023/05/14 10:14:49 by rertzer          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string
import sys

def text_analyzer(text = None):
    """
    Take a string as argument. If none, read it on stdin.
    Return statistics on letters in the provided string.
    """
    if not text:
       text = str(input("Enter a string: "))
    if not isinstance(text, str):
        print("ERROR (argument is not a string)")
        sys.exit(1)
    print("The text contains ", len(text), " characters:")
    up = 0
    lw = 0
    pu = 0
    sp = 0
    for x in text:
        if x.isupper():
            up += 1
        elif x.islower():
            lw += 1
        elif x.isspace():
            sp += 1
        elif x in string.punctuation:
            pu += 1
    print(up, " upper letter(s)")
    print(lw, " lower letter(s)")
    print(pu, " punctuation mark(s)")
    print(sp, " space(s)")
    

if __name__ == '__main__':
    if len(sys.argv) > 2:
        print("Error: to many arguments")
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()
