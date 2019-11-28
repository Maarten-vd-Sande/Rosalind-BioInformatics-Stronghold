"""
Solution to: http://rosalind.info/problems/hamm/
"""
with open("rosalind_hamm.txt", 'r') as f:
    S, T = f.read().splitlines()

distance = 0
for nuc_s, nuc_t in zip(S, T):
    if nuc_s != nuc_t:
        distance += 1

print(distance)
