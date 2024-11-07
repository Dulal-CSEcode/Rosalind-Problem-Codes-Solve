# Sample DNA string
dna_sequence = "GCGGTTGCACCGTTGGGAGCACCCGTATAGGAAGCAAATGATCGGGGTCAATAACTGCATAATTCATGGAGTCCCTGAGAAATTAGAATTCCGGCTTATGGGGGTAGTTCCGGGTTTCCTGCCCACTGATGGGAAACCGTTCTTGAACTTGAGATGTTCCTGGTTAGGGATGTGCTTGTAGAAACCATATTCAACGGTTCTGGGTCCATGGTGGGAGTAAATGGTTCACTACGAATCTACACTATGGTTAATGGGACAAAACGAATGACGGGCGTCCTACCCGTCGGATGACTCGGTGTGACTGAATGATCTACTTATTGCCGCTTTACGGATTGCATCAGCGGCGACGGGGCAATCCCTACTGTCCACGCTCGGTCGATTTAGAAGGACATCATGGTGGTGTTATAAACAACAGAGGTTGCGATGTTTACAACCACGGGACGCCAGATCAGTGGGCAGAAAGTAATGTAGATCTCGTGCACCCACGACCTAACCTCCTCGCGGGGATTATTATTACTGGCTGATAGTCTCCTTGGGACGTTAAAGGGGGATGAGGCCCGTTTCCTTTCGAGTTTTGTTACTGGGACTGGCATCAAGGTGTGGCTAGCAACCATTGTTAAGCAGTGAAGACGCTTGGGTAGACTACACGCGTTGATGTGTGGATGCATCCACTCCCCAGCGGCCAACCACGAACGGCTTTGCCGGTAATAATTGTGGGGCGAATTAAAGGTGAGCTGTAGTAGGCGTTGAGGGGAGCCGAGTTATCTCTGTCAATAACAAAGAAAGATTGGCTGTCCTGGTCCTGGTGCGATTATACGATTCCGCGCGAGAAGATTAGAAACCGTACCACGATGTGGGAAACACCATTAACCACGCTCCTAGCAAGCTCCGACAGTATC"

# Count occurrences of each nucleotide
count_A = dna_sequence.count('A')
count_C = dna_sequence.count('C')
count_G = dna_sequence.count('G')
count_T = dna_sequence.count('T')

# Print the counts as space-separated integers
print(count_A, count_C, count_G, count_T)
