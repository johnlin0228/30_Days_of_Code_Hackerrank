#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    count = 0
    maximum = 0

while n > 0:
    if n % 2 == 1:
        count += 1
        if count > maximum:
            maximum = count
    else:
        count = 0

    # Floor Division(//)
    # Divides and returns the integer value of the quotient. 
    # It dumps the digits after the decimal.
    n //= 2

print(maximum)
