# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rertzer <rertzer@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/14 09:52:35 by rertzer           #+#    #+#              #
#    Updated: 2023/05/14 09:53:59 by rertzer          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) != 2:
    print("Error: please give one argument, neither less nor more")
    sys.exit()
if not sys.argv[1].isnumeric():
    print("Error: non numeric value")
    sys.exit()
number = int(sys.argv[1])
if number == 0:
    print("I'm Zero")
elif (number % 2) == 0:
    print("I'm Even")
else:
    print("I'm Odd")
