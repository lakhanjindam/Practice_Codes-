#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    total_cost = 0
    total_cost = meal_cost + float(meal_cost*(tip_percent/100)) + float(meal_cost*(tax_percent/100))
    print(round(total_cost))


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = (int(input()))

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)


i = 4
d = 4.0
s = 'HackerRank '
a=int(input())
b=float(input())    
c=input()

print(i+a)
    
print((d+b))

print((s+c))    