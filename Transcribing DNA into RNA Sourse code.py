# Sample DNA string
dna_string = "CTCCTCATAAATGAACACTTAAGGGAGGAGAGTTTCTGAGAGTCCTCTGTTGTTCCAGAGTCAAGGTATTTCAAGACGCGCACGGATGCCAGGTATCACTAGGGCGACTTAGCTGACCAGGCATCTCGGCACGGGCGGCTTAGTTCGCGCCGTTTGATGGAAACACAGCAGAGATTGACACGATGGTTAAGGACCACGGTCTTACGATCACCTGGGCGTTTCAGGACTAAGCCAGGGGCGGTCATACGACGTATGGTCAGACATGGCGGACAACATGTATGTTTGCTTTTTCGGTGCGGCTAGGGGACAACTACGGGAAGAAGTCCGAATCCAGGAATTCGCTGTTACATACATCGTGGTAAGGCGGGAAACCCTGGATACACATCACGTTAATGTAACTATCCGCGCGGGTCCGCCCGTGTCCACACTGTGATTGGAATTTCCTTGTCTATTGCGAAATGCCCCAATGTTTCTGTTCCCAAATCGTCGTCTCATATGGACCCCGTCGGCGCCCTGTAACCAAGGCCCCAAAAGTTAATATCCTCTCGCTACTACGAATTCAGACTAGGTTCGTAACTGTCAATTGCGGACCTGCTGCGCCAGTGAAGGCGCGTCACGCGGGGCGGGACATAGTAACGCGCCTGCGGTCGATCTGAGCTGGGATAAAGAGGGGTGTGCCTGGGGCCTGGTCGGTACGAATACAATACGATGAGGGTAACAATGACGCTTGCGGTCGACAGTAAGGCTGGCATTTGAGCCCAGCAAGGGAATGGGTTGGGTTTGCAGCTGCGCACAAACTGTAAAGCTAGGTTGACATCTACGAGTAGGGGTGGACAAGAGTATCGGCTCACAGAGCAACGGGATAGTATTCGGGGGTAGGCGAGGGGCATCAACCCCAATATCTAGCGGTGATCAATACAGAACA"

# Transcribe DNA to RNA by replacing 'T' with 'U'
rna_string = dna_string.replace('T', 'U')

# Output the transcribed RNA string
print(rna_string)
