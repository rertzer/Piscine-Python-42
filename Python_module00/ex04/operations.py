# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rertzer <rertzer@student.42.fr             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/05 13:47:18 by rertzer           #+#    #+#              #
#    Updated: 2023/05/14 10:23:29 by rertzer          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) != 3:
    print("Error: two arguments required")
    sys.exit(1)
if ((not sys.argv[1].isnumeric()) or (not sys.argv[2].isnumeric())):
    print("Error: non numeric value")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[2])

print("Sum:\t\t", a + b)
print("Difference:\t", a - b)
print("Product:\t", a * b)
if (b == 0):
    print("Quotient:\tERROR (div by zero)\nRemainder:\tERROR (modulo by zero)")
else:
    print("Quotient:\t", a / b)
    print("Remainder:\t", a % b)
