#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    # https://docs.python.org/3/library/stdtypes.html#range
    for i in range(1,11):
        print(str(n) + " x " + str(i) + " = " + str(n * i))