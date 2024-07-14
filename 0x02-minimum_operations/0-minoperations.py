#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0
    operations = 0
    pasteValue = 0
    total = 1
    while total < n:
        # copy all and paste
        if pasteValue == 0:
            pasteValue = total
            operations += 2
            total += pasteValue
        elif n - total > 0 and (n - total) % total == 0:
            # copy all and paste
            pasteValue = total
            total += pasteValue
            operations += 2
        else:
            # paste only
            operations += 1
            total += pasteValue
    return operations
