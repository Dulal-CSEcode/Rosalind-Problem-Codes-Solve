from collections import defaultdict

def parse_fasta(fasta_strings):
    """Parse the FASTA formatted strings into a dictionary."""
    sequences = {}
    label = ""
    for line in fasta_strings.strip().splitlines():
        if line.startswith(">"):
            label = line[1:]
            sequences[label] = ""
        else:
            sequences[label] += line.strip()
    return list(sequences.values())

def build_profile_matrix(dna_strings):
    """Builds the profile matrix and consensus string from the given DNA strings."""
    # Initialize profile matrix with counts for 'A', 'C', 'G', 'T'
    n = len(dna_strings[0])
    profile = {'A': [0] * n, 'C': [0] * n, 'G': [0] * n, 'T': [0] * n}
    
    # Fill in the profile matrix with counts
    for dna in dna_strings:
        for i, nucleotide in enumerate(dna):
            profile[nucleotide][i] += 1
    
    # Create the consensus string
    consensus = ""
    for i in range(n):
        # Find the nucleotide with the highest count at each position
        max_count = 0
        max_nucleotide = ""
        for nucleotide in "ACGT":
            if profile[nucleotide][i] > max_count:
                max_count = profile[nucleotide][i]
                max_nucleotide = nucleotide
        consensus += max_nucleotide
    
    return consensus, profile

def format_profile_matrix(profile):
    """Formats the profile matrix for output."""
    formatted_output = []
    for nucleotide in "ACGT":
        formatted_output.append(f"{nucleotide}: " + " ".join(map(str, profile[nucleotide])))
    return "\n".join(formatted_output)

# Sample Input
fasta_input = """>Rosalind_8713
CACACCGTGTCCGTTAATTCAGCAAAAGTGATCGTAGTGAGTGGGGTTTGGGGGAGTCAA
AGGACGGGGAAAAAAGGGCAAATAGAGCCATCGTGCCCTAGCCCATCTGACAATGGATTT
CTTAATCGCTCGCTGTATAGCCCTGATCGGGTCCACAAGCGGGATTTCGCACGTAGGAAT
GTAAGAACTTGCAGGGAACTCGGATAATCTGTTGTAACCACACGCCTGTCTAAGTAGCGG
CCCTCACGCGAAATGATCCTGAACAACGATATACCAGTGAATCCGTCATTCCACGATCAC
TCAAAAAAAAGATTTACAGGTGTGGCTGCGCCTGAACCAAGCAGGTTAGGGGTGGTGGAC
CCTAACTACTGATTAGAATGACAAGATTGGTGCGCAGCTATCATCCCATTGGACCTGGGC
CGTGCATGTCACGGAGAATCACGAGGGTTACGTACTACTGTTCACTGTTCACCCCCGGAG
ACTAGATTTGATGATGACATCTAGCTTCGGCCTGGTCTGCCGGGAGCATGCAACGCTCGG
GCGGACAAACATTGGCAGCTACACGGAGTGTCTTTGGACATTCAACGTAGTGACTCTAGA
GAATTAACGAGCAAGCCTTGCTGGCTGTTCAATTCGAGATTCCTACTCGTGTTACTCTAG
CCATCTATTGGTACGCTTTCAGCGTTCTTCCGTTCTGCCACCTCGCGTTACTGGGATTTT
GGAGCCCCCGCGAATTAGAGAGGATAAAGACTCCGGAGGCACCTTACCCACCCTAATAGC
TCACGCTCGGAATTCCACAGGTAACCAATTCTGTTCATGCCCGATGTTCCTCACGACGAT
CTCGTGTCACGTTCGACGTTTGACGTACGTGGTATCTCTTGTCTGTCCACTCAGTATCCA
TGGTCGCGCAACTGATAGAC
>Rosalind_6417
CGTACATTCTCCCAAAGTCTAGACGACAGATTCTACGCGCATTACAGTCAACAACTTACG
CTGACCTTTCTCAGTTTCTTTTAGTGTGGCAGTCGAGTTCTGGTGGGGTGTTCTACAACA
TCGATGAATGAACGGCACAAGCACGGTGACCCTGATTTGCGAACACAAGCATAGGGCTCC
AACTTGCCCATACACATAAAAGCCACACGTACAGCATGATTGTCGTCTATCGGGCGACGC
AGTATCTTGCATGAACGAATGAAATTTGCGCTTCCCTCAAGTTATTCGTCACTAAAAGAC
TTCATCAGCCCATTGGCTTTGGTAGTTACCCTAAGCGCGTCCCTATACGTTGAGGATCAA
TAGATCGCCAGACTATTTGACAGGATTCTCCCTGTCTACTTGATCTCAAGTCCCCCGGCG
TTAGCAAACATAACGTCGTAGGAGTACATCGTTTAATCAACTGAAACGGCCTAAGTTACT
TATCCCTTCTCAACGGGCACCGGATCGCGATCCTCGGCCAGCCGGGGTCTTTTAGCTGTA
CTTCAGGTACACTTCCCTAGCCGGCCCTCACTGTGCCGGAGCGATGACCGTAACGAGAAA
TGCTCCCGTTTAGGTATTCTGGTGATTGATCGGTATCATTGGTAGCCGGACGTATGACGC
GTCCGCCCAAAGCCACGGGGCCACCGTTTAGGGTAGGAAGCCTAAACTGGCATACCGGCT
CGGGGCCGCTCTAGCTCCTGGCTCCCCAGAGTCGGTGGAAATCTATACTGTAGAGATCAA
ATGATATCACGCGCGCAGCTCAGCACTACCTCTGATAGCGATTAACGTATAGTTATAGGT
GTGTCAACTGGCTCTAACGGTCCAATCCGATCTTGGTGCAGTCCCCCTACCGCTGAAGTT
AGGGCTCGCGCGTACAAGCC
>Rosalind_3086
AATGCGACATTACATACGTTTACTCCACACTGTCTCTCACTCGCACTTTACCTCTCTTTT
TCCGTATCAAGGTGGCGCACCTTAATCCAGAGTTGTAGGAGCCTTCTGCTTAATGCTATG
GTACAACCTATCCGAGGACTACCTTGAGACGTTGAGCCGTTTGGTCGTTATTTAGCGTTT
GATCCGAATAGGCCGCCAGCTCTGGTTGTTAGTGCGTCTGGTCTGAGCTGTGTCCGGTCC
CCGCGGCTAGCGGCTAGCTACTCGGGCAAGATCGCCTCGTAACAACGCTCACATCAGCGT
CAGCGTGTTACTCAATCTTACTACAGATGAGATTCCGCTAACCCCGGAAAGCTCATTTAC
CTCAAAGTGGTGGTACTTGTCACGGAGGGCGCTAGCGTCGAGTGAGAGTATTACTGCTAA
GTAGACAGGAGCGAATTTTGGGACTACGCCGTTCTGATGATTCGAGATGTAGATGTCTGC
TCTACCAATTGGCCACCGCACCTAGTCACATTGATTTGCCTTAGTGGTACGGTACCAATC
TGCACAGGCGGTGCCCAACGTACGGCTAACATCGGACTGGTAATCTCACAAAAGTGCAGT
AGTCCTAATTAGCGCGAGTTACCCCGCGATAGACAACGGAGTACTTGAAGGGGTCTCTAC
TCTACACATTTAGCCAACATTTGAGCTGTCTTCACGATCATTCGTAACAGCCCGGAGATG
GTACATTAGACTCCCTGCTGGAATTTCTTCTCTAACCAGACCCAAGTCTAGTACAATTAT
CCCCGCCGAAAATCTAATGATACAAATCACGAGAGGTGAATCGCAAGTTGGACCGGCCCG
TAAAGATTAAAGCTAAAGCGCTGGTAGGGAGCGTGATTCAGAAGGACAGCTCATACTCAA
GAGGCCGACTATCTCTTATT
>Rosalind_0525
CACATCCACTTAGTTTAATACGCTGGCCTAAGATCCGCAGCCTCGTGCCTGACCGTGGAG
TCAGAATCTAGGCCCATTCTCCTCCGTTCCACTCGGCATTTAGAGTATTACAGTGGCTGT
CCCCAGGATGACGACAGTTGTAACTAAAGAGGAGTCGGAGGAAGAGAACTATTAATCCCC
GAGGTGGAGGTGGTCCCATCTGCACTATAGCCTCAATCACCACAAATTGGCCTTACAGCC
GGTCTGTGCATCTGTGTGGCAACAGGTTTAGATTGCCATAGTTAGCATACAATCTTCTTC
GGGTGGCTATGACTCCACCCGAACTACACCTATTTTCAACTAGTGAAGTTAACCAGCCAG
GCTAAACGGATTTTAGTCTGTCTCTCCTGAGCTTCCCCCTTGGGGAATAAGTGAATGGAC
GCATCCACCAGGGAACTGCTAGGAGCCGTGGCGTGCGCTTAGCATCGCCGGGCCCGGATA
TCGACCCAAAGTACTCCCAATGATTAATCGCGGACTGAGACACAGCTGTTTCTATATAGG
GTTCCTGCCCTAGTCCGGATCGTTTAACTGAATGATGTAGACACGCGTTAAAAGGCATCG
TACCACACATGGGTTAAGGCCGACGTGTGGCCGCCTCAGACCTTCTTTGTATTATTTAGT
TAGTGCTAGGAGTGTACCTTTTGTGACTGCATCCATGGTTGATAAGATCCTCAACTGGTC
GCAACCAATGGCATACGCATGCCACACTGCCCTACGAGAAATTATATCACTAATGACTAA
CTAAGTCTCTTGGCTTGAGTCTGACAGAGACCACATCTAACATTTATGCTCTGGGGTCTG
TCTTGTGGAAACCTAACGAAACGAAAATTCCCGCTGCTACTCCGACCTCGCAGGCGCCGA
CGGTTCGATGCTTTGCATCT
>Rosalind_5277
TGGATCCATCTTGAATGCTGTCAACCGATTACGCCGTTTCCGGGGGTCAGTAGAATCCTC
TTAAGATGCTTCGATTCAGGTTACAAGCAACAACCCCTGCGTACCAGTTCCGGAGTGATA
GATTCTAAGAGTAACTTCCCGGTATTCAGCGATTAGGAATCCAGATTTAACTTCCTAGCC
AGCATAAGTCCGACGTGTGAACTCTCCACATACGGGCCTTCCACACTAGAAAGTGGAGGT
ATCCGCACTCCGAGTCACTACTAGAACGAATTTGGCGTTCATGCGGTAGGAGGGCAATAC
AGAAACATGAGGCCATGAGAGCCGATGGCACGGTGGCATTTATGAGCCCTAAATCTGATG
ACTAAAGGTCATGAATGTCCTAAACCATCTACGTAGCGCGTCCCGCCTGACCTGTGAATT
TTACTGTATGGCGATGCTGCGCATGATCCTGCGATTTAGTCGAATATCTAAATGCTATTC
AAATGGCTTCGTGTCGACTCTACTTTCCTGAAACGTGGTGTGTGTTCCCAGAGAATGAAT
AGGACACCCGATATACTCATGAAAAGGCGCCATTCATGATATCAGCATGAACAGGCCTAT
ACGGGGTTCACAGGTTAGAATGTACTTCCTAGCTTACTGTTTATATGAATAGCGCCACTC
CACCTCACCACGCAGGCAGTGGGCCGTTCATGCACAGAAGTCCCCAAAATTCGTCACCAC
GGATATTTTACGGGAACGACGCAGGGTCAGGACAGTTGTAGTAATATGAACCTAACACTC
CGACACCGGTGCTCAATCTGTTCATTGCGGCACCTACCTAAGCAAAGGCCGGGAAGCAAG
AGTTATATCTTCGCGAAAGTAATGAATGGACTCCGTAGCCCCCCTATACCTTCCCTAAAT
TCATGCGGGTGTTCGCGTTA
>Rosalind_0983
ACGAATGTGACGTCAGTGTCGCGTTAGGAGAGAACCTCTCTAAGGGTGCCTGTTTCGGGG
GGATAGGTACGATAAGCATTATGCATCATCTGCACTCCACATGCTTTAACCTCGAGTACC
GGACAACGTCTACGGGCTGCGCCGCGGGTGTGCAAAATTGGAAAGCTATCTTAGCGATGG
ACAGATGTCAAATCTGTATGTGGGGATGGACGGCTACCACGGGTTTGTCACGGTAAGATG
AACGCCGTGATAGCGCACCAACGGTTCTACCCTATCCCACGCAGGGGTAAATCTGCATCC
CGCCAGTCACTTGTAGGGCTTCTTGATACTCTCATGGGTGACCGAGGAAGGGGGGCACGC
CGTGACTGAACAGGTGGAACAAGCGGAAAGCATACCGATCTCTTAACAAACCAGTTTACC
CGGCGCTAGCGTAAACTTTCTCAGTGTTTGTGTGTCACTTCCGTAAGTCGCGACTAAGTG
AATTAGGACCGTTGGTCTGAGCCCGTAGGAGCGATATTTTAACCCACCTGTTCAATATGT
TTTGAAATCCGGGGGGTGAAGATTCGCATCATGCTGTTAGTTGCCAAATTGTGTCGCACC
TGGGCAACTGACGTTCCCCGACGCATGTCACCGTGACCTCAAACTTAGGGTACGGACATG
GGGTCAGCCTCAGGGCGAGCAAGGTACTGTCGTGGCCGGCTATGGTACTATTTAAGGCGT
CATGGTTAGTCTAATTCTAACGGCGTACAATACCTTCTCCTAGATAGACGCTTGAAGTTT
ATTTGAAGAAGGAAAGGTAAAGGTACCGAACTCTGCATTACGTTACTGGAGGCTCAAGCT
AGCTGAGACAGAAACATTGATAGGCGAGTTATAGTGACCTAATGTATGCCATAAAACCCG
TTTCCTCAGCTTTTTATACG
>Rosalind_4093
TACCCGGCCCAGTTCGTTCTATCGTGCGCACCGCCTTGGCTATCCCCATGGATAACCCGT
ATAGTGCGTTGCTGCCAAGTCAACCGACATTTAGCGTTGACAAACGTTACCTTCAATGTC
TTCTATCTAATGACTCAATTTAACCATCCATTTTACACTTTTATCATTTGCTACACACTT
TGACGAACCAACTATTGAGGAATAGCATGACTATGGACCTGTTTGGTGCGTAGGCAGTCC
TTTGAATTTTCATATGGTAGCTTCGCGGTGACCGCATATTTATGTCCGAAGGAAAACGTT
CACTGGTCCCACGTGCTCTTGTTCAAGATACGTATGAGCATCACATGGGGATCCAACATC
AATTTGAGGTTTATTAGAGTGGCTCTTATACGTCTTGTGGACCTCACAAGCAACTGGGAA
ACGAGACTCGCAACGATTAGATGGCCTTGCGGAATATGGGCGTTGGAGCTTTACAATGCC
TGACGATGGTTGTTCACTTTATCAGGGGCCCCCAATTTACTTCCCTACGGAGTCTGGTAG
AAGAGCGCGTCCACAATATTTAGATTACAATCTCTCTCAGAGGACCCAAAAATGATCCGG
TTGTGTGACCTCGTCTCAGGTACAGTCGTTGTCAGACAACGTCGAAAGTCGCACCCAAGG
TCTGACCCATCCCGGGCGGTTCAAACCGTATGTCAATGCCTACGGATTCGCTCGCGTTCG
TGTCAGGCATATCATTGTTCGACCCTGCTGTCGGCCGTTCTATAGATCGGTCTGGTGCCC
GTAAAGGTTAGGCTAAGTATTGATTGGATGTATACTCCCTGGTGTCCAGTAATACAGTTT
GCCAACGGCAAGCTCGTCGAGTGTCTGATCAACTGTCGCCCGTCGTAACGACACGCGATC
CTCTCGCTTCATAACTCCGT
>Rosalind_5012
GATTTCCCATTGGGAGGCAAATATTTTCGACCCTCCTTTCAAGCACCCACGAACTGAGCG
GTGAATGTGGTCTTAATCCAGTCCGTGTTCTAGGTGAAGGTCTCAAGGAAGTTGCACTAC
AAAGGGACGCACTCCCGCCAGTGTTTGTTTCATGATTAACGATGTGTTTTGAACTTAAAG
CCGTCTTTTTGGGCATTTTGTGGCGCTGCTGGTCTGTATGATGGCACCGGCTGGTCCTGA
TGGGATTGGCCAGCAGGGTGGCGCATCCGGGAGTCTCCTCTAAGTTAGGGAGGCTAACTA
GATGTTGTTTATAACTCGGTACGGGGATCTGCGTATACCAGATGCAAATGCTACCGGAGC
TTTACGAAGGCAAAGGTGGGTCTAAAGAAATGGCCGAGTTGTTCACGCCTTCCATTCACC
AAGTCGAAGGGGTGACTATGTGATATGGATGCCTTGCTACGATAGTCTTTCACCTCTCCC
TCCGTAACGCGGCACTTTCTCTGTATGGCAGCTCTTTTGGTTTGGGGGCTTCTCTGTGAT
ACGGGCGTTAGCACCATCAATAAACGCGCAGGTGAATAAACCAAATGGACTGAATCCAAA
CCTGTTGTGTGGATCGACCGTATTCGTGAGGTTTCAAGGTATTACTTCCTATCGCCCAAA
GTACGCTTACGGGAGCAGCGAGTTGGCGTGGCAAGACATGACAATAATTTACGCGTACTC
TCTTTTAAACTATTGGGTGCACGAAATCTATACAATGGCTCCCTGGTTTGTCCAAGAGTC
TTCCGCCTATTTAAACAGCAACAGGTGTGAACCGGACTAATATGCTTGGACGTACCTCAT
CTATCCGAGGGCGCCGTGTTACATTAGGTGCTTTAACCAATGAGTGAGCTGGTAGTTTGT
ATTTAACAACTTGGCCCGAG
>Rosalind_4828
AACAAAATCTAAGGCGCCATGCACGTCCACTACTCACAAACTAAAGATGCGATAGTTCTG
GTATTGAGCTAATCCCCAACCGCCGGCTAGAGGGTGCGACCCCCATAGCTGAGATCAAGC
GGCGTAGAACCCTTTTGCCGCCTACTATATACGAAGGTGTGCCGCACCTAATCAGTTCTC
TGTCCCGGTCCACCACACAAACGGGTTTACGTAGTGTGGGCTAATAGAACTTATTTGCGT
ACGCACTTAAGTCAGTTTGCCCTAGGTGCACCGTTGTCGCCGATCTTGACTATTAGTCTA
AGAAGTGTGACCACCTGACGACTCCAATCCATCCCAAAGCTATTCGAGCTGTATCGGTCT
AGCTAATTCCCTTCCCCACTCTGGTGTTACTATATTGGGGACATCTGGCCGCCATGTCGT
TAACACCTGCCATTGCTGTCAACGCACGAGAGATGGCCAACAAAACAAATTCCGTCACCC
ATGATGTTAAGCCTAACAAGTGCCTTTGTGTAGTCTCTCTATAACTAACTAAGACACGTA
TCCGCGTTCAACCGAGTCGGCTGGGATTCAGAACGTGCCTGATTTGACCCGGCGTATCTG
GAATCAACCAAGGTGACGCTGATCGTGGTTGGAGTTAGCCCCCAAGGTGTTCGAAGAACG
CATCAAGATTTAAGTAAACCTTGGCGATTTAACCTCTTGGGGTGGATAATTGGTGACCAG
GAGTGCTCCCCGTGCGGTTTCATTAAAGCACTATGAACATCTTTGCAGTGCGGACGGCAA
GACGACGCCGCCCTACTACGCTTACGCACTGTGGTGTACGTCACCTCTTCAGTAATGGAG
TCAGGAAGTGCTTATCGTAGGCCTGTCACAGTCATGTATCGTCGTTGCTACAGAGTCACA
TATGAGACGAGGGATTAATG
>Rosalind_9450
AGGGGGCCGTCTGGATTGACATTTTACTAGGTATTAGCTGGTCGGCGGGGGTGAGACTGG
ATCTGTCGGGTTAGTTCATTTCTAGCAGGCTATGTGCGCAACTTGACGCTGACAGTGTAC
AAGTGGAATGAGTCCATAGCTAGAGGTCTTTCATCGTGTATGCTCGGTTTCGTCAGCTTC
GCGCGTCCATTTGTAGACTAAACACTCCTATAATTACTGCCCTCCATTTCTCCCTCATCT
GCTTAGCAACTTCTGCTAGTAAGTTGGTCGTTGTGCGTAGTATGGTTGGAAATGGCATTA
CCATGTCGCCAGTTGAGCGCTTGGGTCGTTACATGTGGGTTGGAGTCCATATGGAATAGC
CTGTCTCTTGCGATGATCGTCCGACCCGGTTCCGTCGGCCCTCCTTAGTGTGAGACACAT
CTTGCGACGCTTGGCAGCGCCCGTATGTCTGATCAAGACAATGCTCATTCACGAAGGAAG
CCGAGCTCCTAACAACGCCCCGTACACGTCATACTAAATGGCGCCTCTTCGTACACGCGG
CAAAACGATGGAGCGAGATCCTAGTGTCTTTACAGATTAGTGTAGCCTCCGCATTAGTAA
GCCCTGTTCGGATTTGGTAAGCCTGTGCGCCGTTAGCCTACCCTGTTGCGGCGAAGCTGA
CCCTGCACGGTCGGGATATGTGAACTCATAAGTTGTAGTGGAAAATCTAAGCAGTCGCGT
GTCTTCATCATGAACTTCCGGCCATCTTGGAGCTTTTGGTGCGCCAGGTCGATTAGCTTA
AACCTTAGGCAATCTTCCTATGCACTTACGAAACTATCCCGTACTCACACATTGGACGAT
GCTCACTAAGGCTATCTAGGCTGCGTTCCGCATTGCGCGCGATCTAACTACTAACGCAAA
GAGGTACGGCGCCCGACGGC"""

# Parsing the FASTA input
dna_strings = parse_fasta(fasta_input)

# Building the profile matrix and consensus string
consensus, profile = build_profile_matrix(dna_strings)

# Formatting the output
print(consensus)
print(format_profile_matrix(profile))