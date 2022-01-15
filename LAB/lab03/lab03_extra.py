""" Optional problems for Lab 3 """

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return False
    helper = lambda i: True if i == n else False if n % i == 0 else helper(i + 1)
    return helper(2)
    

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if a > b:
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)
    elif a < b:
        if b % a == 0:
            return a
        else:
            return gcd(a, b % a)
    else:
        return a

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    def count_number(n, pair, cnt):
        if n == 0:
            return cnt
        elif n % 10 == pair:
            return count_number(n // 10, pair, cnt + 1)
        else:
            return count_number(n // 10, pair, cnt)
    def count_n(n, cnt):
        if n == 0:
            return cnt
        else:
            return count_n(n // 10, cnt + count_number(n // 10, 10 - n % 10, 0))
    return count_n(n, 0)