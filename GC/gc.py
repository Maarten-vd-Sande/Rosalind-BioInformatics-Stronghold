"""
Solution to: http://rosalind.info/problems/gc/
"""
def gc_content(sequence: str) -> float:
    """
    :returns the ratio GC content in a sequence.
    """
    return (sequence.count('G') + sequence.count('C')) / len(sequence) * 100


fasta = {}
with open("rosalind_gc.txt", 'r') as f:
    for line in f.read().splitlines():
        if line.startswith('>'):
            header = line[1:]
        else:
            fasta[header] = fasta.get(header, '') + line


fasta_gc = {key: gc_content(value) for key, value in fasta.items()}
highest = max(fasta_gc, key=fasta_gc.get)
print(f"{highest}\n{fasta_gc[highest]:0.5f}")
