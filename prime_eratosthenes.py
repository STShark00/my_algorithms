'''Sieve of Erathosthenes'''
'''
    1. List all int from 2 to n
    2. Find the minimum number i that has not been processed
    3. Remove multiples of i (excluding i itself)
    4. Repeat step 2-3 until not possible
'''

import math

n = 1000 # Can determine all prime from 2~n
array = [True for i in range(n+1)] # Initialize every number as prime

for i in range(2, int(math.sqrt(n+1))):
    if array[i] == True:
        j = 2 # We don't want to remove i itself
        while i*j <= n:
            array[i*j] = False
            j += 1

for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')