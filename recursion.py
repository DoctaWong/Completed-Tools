def gcdRecur(a, b):
    '''
    Takes two integers.
    Returns their greatest common denominator using recursion.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)