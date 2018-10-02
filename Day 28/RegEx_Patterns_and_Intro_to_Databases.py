#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())

    name_array = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if re.search('@gmail\.com$', emailID):
            name_array.append(firstName)

    sorted_array = sorted(name_array)

    # use re method to print.
    print(*sorted_array, sep='\n')

    # use for loop to print.
    # for i in range(len(sorted_array)):
    #     print(sorted_array[i])
