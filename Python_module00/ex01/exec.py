# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rertzer <rertzer@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/14 09:49:35 by rertzer           #+#    #+#              #
#    Updated: 2023/05/14 09:51:06 by rertzer          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

n = len(sys.argv)

string = ""
for i in range(1, n):
    string = string + " " + sys.argv[i]
if n > 1:
    tmp = string [::-1]
    tmp = tmp.swapcase()
    print(tmp)
