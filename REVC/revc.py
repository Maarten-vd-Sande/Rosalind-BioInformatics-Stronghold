"""
Solution to: http://rosalind.info/problems/revc/
"""

with open("rosalind_revc.txt", 'r') as f:
    DNA = ''.join(f.readlines())

REV_COMPLEMENT = {'A': 'T',
                  'T': 'A',
                  'C': 'G',
                  'G': 'C'}

print(''.join([REV_COMPLEMENT[nuc] for nuc in reversed(DNA)]))
