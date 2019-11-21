"""
Solution to: http://rosalind.info/problems/fib/
"""

with open("rosalind_fib.txt", 'r') as f:
    N, K = f.readline().split(' ')
N, K = int(N), int(K)


def fibonacci(n: int, k: int) -> int:
    """
    The total number of rabbit pairs that will be present after n months, if we begin with 1 pair
    and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit
    pairs

    :param n: number of months
    :param k: reproduction rate
    :return:  total number of rabbits
    """
    if n in [0, 1]:
        return n
    return fibonacci(n - 1, k) + fibonacci(n - 2, k) * k


print(fibonacci(N, K))
