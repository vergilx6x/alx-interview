#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n 'H' characters.
    '''
    if not isinstance(n, int) or n <= 1:
        return 0

    ops_count = 0
    divisor = 2  # Start checking from the smallest possible divisor

    while n > 1:
        # While n is divisible by the current divisor, keep reducing n
        while n % divisor == 0:
            ops_count += divisor
            n //= divisor
        divisor += 1  # Move to the next divisor

    return ops_count
