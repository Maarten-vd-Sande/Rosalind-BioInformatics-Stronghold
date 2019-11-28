"""
Solution to: http://rosalind.info/problems/subs/
"""
with open("rosalind_subs.txt", 'r') as f:
    S, T = f.read().splitlines()

positions = [str(pos + 1) for pos in range(len(S)) if S[pos:pos + len(T)] == T]
print(' '.join(positions))
