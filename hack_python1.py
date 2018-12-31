"""
Task 
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
"""

#!/bin/python3

N = int(input())

#If n is odd, print Weird:
if N % 2 != 0:
    print("Weird")

#If n is even and in the inclusive range of 2 to 5, print Not Weird:
if N >= 2 and N <=5 and N % 2 == 0:
    print("Not Weird")

#If n is even and in the inclusive range of 6 to 20, print Weird:
if N >= 6 and N <= 20 and N % 2 == 0:
    print("Weird")

#If n is even and greater than 20, print Not Weird:
if N > 20 and N % 2 == 0:
    print("Not Weird")