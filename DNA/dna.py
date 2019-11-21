"""
Solution to: http://rosalind.info/problems/dna/
"""

with open("rosalind_dna.txt", 'r') as f:
    DNA = ''.join(f.readlines())

print(DNA.count('A'), DNA.count('C'), DNA.count('G'), DNA.count('T'))
