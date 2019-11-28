"""
Solution to: http://rosalind.info/problems/iprb/
"""
with open("rosalind_iprb.txt", 'r') as f:
    K, M, N = f.read().splitlines()[0].split(' ')
K, M, N = int(K), int(M), int(N)

total = sum([K, M, N])
chance = (K / total) \
       + (M / total) * (K / (total - 1)) \
       + (M / total) * ((M - 1) / (total - 1) * 0.75) \
       + (M / total) * (N / (total - 1) * 0.5) \
       + (N / total) * (M / (total - 1) * 0.5) \
       + (N / total) * (K / (total - 1))

print(f"{chance:5f}")
