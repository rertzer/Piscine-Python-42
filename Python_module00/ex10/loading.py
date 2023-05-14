# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rertzer <rertzer@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/14 14:59:28 by rertzer           #+#    #+#              #
#    Updated: 2023/05/14 15:55:42 by rertzer          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
import math
from time import sleep

def ft_progress(lst):
    maxi = len(lst)
    start = time.perf_counter()
    i = 0
    for item in lst:
        i += 1
        elapsed = time.perf_counter() - start
        progress = i / maxi * 100
        if i != 0:
            eta = elapsed * maxi / i
        else:
            eta = float('nan')
        bar = ''
        barsize = int(progress / 5)
        for x in range(barsize):
            bar += '='
        bar += '>'
        print("ETA: {:.2f}s [{:>3d}%][{:<21}] {}/{} | elapsed time {:.2f}s".format(eta, int(progress), bar, i, maxi, elapsed), end='\r')
        yield item


if __name__ == '__main__':
    listy = range(1000)
    ret = 0

    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)
