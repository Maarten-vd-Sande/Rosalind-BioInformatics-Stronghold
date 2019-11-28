"""
Solution to: http://rosalind.info/problems/fibd/
"""

with open("rosalind_fib.txt", 'r') as f:
    N, M = f.readline().split(' ')
N, M = int(N), int(M)


def mortal_fibonacci(n: int, m: int) -> int:
    """
    The total number of rabbit pairs that will be present after n months, if we begin with 1 pair
    and in each generation, every pair of reproduction-age rabbits produces another rabbit pair and
    pairs die after m months.

    :param n: number of months
    :param m: max age of rabbits
    :return:  total number of rabbits
    """
    if n in [0, 1]:
        return n
    return mortal_fibonacci(n - 1, m) + mortal_fibonacci(n - 2, m)


print(mortal_fibonacci(N, M))
