# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rertzer <rertzer@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/14 11:44:03 by rertzer           #+#    #+#              #
#    Updated: 2023/05/14 13:02:28 by rertzer          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string
import sys

if len(sys.argv) != 3:
    print("Error: two arguments required")
    sys.exit(1)

if not sys.argv[2].isnumeric():
    print("Error: second argument must be an integer")
    sys.exit(1)

words = sys.argv[1].translate(str.maketrans('', '', string.punctuation))
words = words.split()
words = [w for w in words if len(w) > int(sys.argv[2])]
print("{}".format(words))
