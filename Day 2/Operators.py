#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    totalCost = meal_cost + tip + tax
    # after round() the number look like float, so need use int() to converted to integer.
    # Strings cannot combine integers, so need use str() to converted to string
    print('The total meal cost is ' + str(int(round(totalCost))) + ' dollars.')
if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    solve(meal_cost, tip_percent, tax_percent)
        
        
