def reverse_complement(dna):
    # Define the complement for each nucleotide
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    # Generate the reverse complement of the given DNA string
    return ''.join(complement[base] for base in reversed(dna))

def find_reverse_palindromes(dna):
    # List to store the positions and lengths of reverse palindromes
    palindromes = []

    # Loop through all possible lengths between 4 and 12
    for length in range(4, 13):
        # Check every substring of the given length
        for i in range(len(dna) - length + 1):
            # Get the substring
            substring = dna[i:i+length]
            # Check if it's a reverse palindrome
            if substring == reverse_complement(substring):
                # Append the position (1-based) and length of the palindrome
                palindromes.append((i + 1, length))

    return palindromes

# Read the input sequence (assumed to be in FASTA format)
def parse_fasta(fasta_string):
    lines = fasta_string.strip().split("\n")
    # Join all lines after the first one (which is the header) to form the DNA string
    return ''.join(lines[1:])

# Sample input in FASTA format
fasta_input = """>Rosalind_6712
ATATGCAGCGCACTTCATTGCTAGCAGTAACAAAATCTTAATACCTCCGCCCTCGCCTAT
CCATTGCTAATATGTAGGCTACCAGCGATTCTGCTGCGTTGTCTGTAGCAGGGTTGAGAA
TGCTAACTGAAACGCTTGACCAAGCAAGGAAGTGTTTTGCTTATTTCAGATGTCACTCGG
CGGCATGGTACGAGGCTACGCTTTCCTGCGGCTCCTTGGTTATAACTCTGCGATCACGAC
TTTTTCTAATGGATAGCGTGCAGTAGTGTCCACATCTCGCGTGTTGCCGTGCCTACCGGC
GACGCTACTTCTGACGTGTTGTTACCTTTAGTGCCCGTTGATATGTTTATAAATACGCCA
GGTTTGACCAACGACAAGGACTGATACGTTGATAATGTACCACAGATCAGCGTCGCTAGG
GCGGAATAAGTGATCACATTTCCCCGTCCGGGAGCTTCTTGAACCACTCCCAGTCCGCGG
ACTAAGATAAGAGTAAGCGAGTTTGACAGGAAACTGGAGGCCTAGGTAAACGACTGAAAA
GTGTACTTTCCGTCTAGCCTCGTTGTAAAACACACCGCTCAACTTCATAGAACGCGCGAT
CCTTTGCGGGGTTCGATGGAAACGTTTGCCCCCCCATCGTCCAAGCACCATTACCAACTC
CCTGAATACAGGTCATAGGAGTATTTTCGGAGCTAGAAGAGTTAGCCATTAATCGCAATC
GTTCGTGCACCCTGCAAGTAAAAGGCCAACAGCTGGATTCATCCTTTAGAAACAAGCGCG
AACCCATATTTCTAGCCTAGAGCTCACATGTAGCACTGGATCTCCGCAGGTATCAGGGAG
CTACTTAGCTCAGATCACAATACCCCACAGCGCATTCCTTGGGTTGTGCTTGCTAGGCCA
TAGGCGTAAGGTCATACAGGGCCGGTCACTACGTGATGCCCGGTGTTAACATAT"""

# Parse the FASTA string to extract the DNA sequence
dna_sequence = parse_fasta(fasta_input)

# Find reverse palindromes
palindromes = find_reverse_palindromes(dna_sequence)

# Print the result
for position, length in palindromes:
    print(position, length)