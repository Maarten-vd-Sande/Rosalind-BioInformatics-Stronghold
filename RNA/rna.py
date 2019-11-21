"""
Solution to: http://rosalind.info/problems/rna/
"""

with open("rosalind_rna.txt", 'r') as f:
    DNA = ''.join(f.readlines())

print(DNA.replace('T', 'U'))
