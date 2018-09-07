#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    # https://www.tutorialspoint.com/python/string_rstrip.htm
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    max_sum = -63
    temp_sum = 0
    for i in range(4):
        for j in range(4):
            temp_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if temp_sum > max_sum:
                max_sum = temp_sum
    print(max_sum)
