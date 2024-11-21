# RNA Codon Table as a dictionary
rna_codon_table = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
    "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

def translate_rna_to_protein(rna_sequence):
    # Initialize an empty protein string
    protein_string = ""
    
    # Process the RNA sequence in steps of 3 (codon length)
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]  # Get the next codon
        
        # Look up the codon in the RNA codon table
        amino_acid = rna_codon_table.get(codon, "")
        
        # Stop if we reach a stop codon
        if amino_acid == "Stop":
            break
        
        # Add the amino acid to the protein string
        protein_string += amino_acid
    
    return protein_string

# Given RNA sequence
rna_sequence = ("AUGAGUCAUGGCAGCCGUGAAACUUUUUUACCUUGUAAUUGGGGGCGGCUAGAGUCAUACAUAAUUGGGCUCUACGGCUUGAUGGGGUCCCAUGCGUGGCCCUGUUCGAUUCAUCUCCCAUUGAUACUCUUCGUCCUCUUCAAGACACGUAAACUGGUUACUAACAUUAAUCUCAAGCGAAGUUUAACUAGUGACACCCCAAUCCAGAUUCUUUUAGUCCCCGGAUUAGCUCAUAGACGCGCAGCCUGUAAUAGUAAUAUUUUGCAAUGUCCGGUCCUCCGCAUAAACAUCUACGAAGAGGGUACGCGAGUAUCUCAGUGCGCGCUGCAUCCCAGGUUUAAGCUGUCUGUUGUAGACCUAGUACGACAAGCAAAACAAUUGGGUCUGGAAAGCAAACGCGGGGUACUGACGCCGUGCAGGGCUAGCGGCGAACUUUUCACUGCGCCUAAAGUACGGGCAAUUCCCGACCAGUGCACUGUGAGCAUAAUGAUACACGUUCAUAUGCCCGAAAGAUUAAACUAUUGUUUGGGUUGUAUGCCUGCUCCACGGAGGAAAAGCCCACUAUUAAUGGAGUGCGCCCCUGAGCCAUUGGGCCUCUUGUCGACGAUAGGACUAGUGGGUCAUCCACCUUACGCUAACGAUCAGGGUAUAUUCACUAACCACGAGUUUCUGGAGAGUCCUAUGAGGCCGGAUCCUCGGCGAAGGGUCAACCAGACCGUGUCAUCAGACUACGCGGUUACUUGCGUCGAUAAGGAUCUUUCCCCCAAGGAAACAAUCGGGCGGAAACCUGGUGGGUCCCAUUCGGCGAUCGGAAGCCACGCAGACGCGCUCUCAGUGACGGCUCACUCAAACAAAGUGACAACAUACAAGAGUUUCUGCGGGCCUCCUUGGUGUUCUUUUAAUGAGAAGGCAUGGUGCAUUACAUUUGUGCCCCCUCGUAAAAAACGCGGAGGUGAUGCUGUGAUACUUAAGACUUCUAGAGUAAAAGUUAUAAGCCGAACACCUAACGCGCGCAGUUCUGUGGAGUUCGUUGAUGAACCGCGGACGGUAUUCCAUAUACGGAUUGGAAAAACGGCUUCGGUUAGUCCGCUCACUUAUAAGUGUGUUCACACAUUACGCCGGGACCUUCUCAUAAUACGUGAUCCCGAGACAGGUUUAUGCGCUUGGUCGGCCUCUGCCGCAGAAGUCCGACUCAGGUAUUGCCGCUUGACACCGAAGACAAGGGUUCGGAAACUCUGGGCAUCAAGCACCCAGGAAACCAUCAUGCCUAGAUCCCCGCACAGCCUUUCUUACACACGAGUGAAAUUGUAUGGUCAUACAGACUCCGGGACCAAGAGUGUUCGAUCCUCUUCCGCUGCUCAAUGUUUGCGGCUAGGUUUGUGUCUUACAAUUAAUCUCCGCCUGCCUGCGCUGUUCUUGUACCUACCGAGGCUGCUAUCUCCUGAAGAGUCAUACAGCGACCACCGAGCAGCCAAAGUCAGUACUCAAUUGCAGUGUUCACCCGGUCUGCUAAUAUUUAUCACAUGUGUUCUCGCAAGUCUUAAUAGGCCUGCCUCUUCACGACUCUGCCGGCAGUGCAGCGCACGCAUGGCGCACCUGGUCGCAAUAAAGCAUAUAGUAGGGUCGCUGUCACCCGGUCUUGGUGCCGGCGGCGGGAAAAUAAGAGGCAUCGAACGUAAACAGCCUACAUUCUUAACGUCUUUUCCGCAUAUUGACGUAAACACUGGUCAGCCGAGGCGUGUGGUUUCGCACCCUGAACAUCCUCAAGAGCCCCCAUCAGCUCCGCAGCCUACGUUACGUAAAAAAGUUUCGGGAGUGUCCCCCAUGCACUGGCAAAUUCAGUUCCGUCUUACCAUCCGAACGCACGGAAGCAGGUUAAUCUCAUCGGAGACGGUCGCGUAUCGUAUUUUGCAAACCGCAGAGAUGACAUCUUGCGCCAAGCUUGCCGGUCUGCCCCUAAGGCAAAUUCGGUGGAGUGUACACUUCCCACUAUGUUCGCAGAUCAGCUUAUCCUUGUACCUGACGCAAUACCGGUUUGUUGUGAUAACCGCAAGAUUACCCAAAUUACUCGUUGGCACAUCCAACGUAAUUCGUGAUGCGUAUUCUGGUCUCGCUCUUCUUGAUUGCUCUGGUACAUCAAAGAUUGCGUGCAAUGCAAAACAUGGCGCGAUUCACUUCCUGGCAAGUGUGAAGCCUUUGUCUCACACUCAAUCACAUAUCGCAUACCGUAUGGAUGCCCCCUAUGCAAGUUACAUGACGAAGUCUCACGAAGCGACCCGUGAGUUCAUCCAAGCGAGUCUUGCCUUGCGAAGACAUCAACGACAUAGGACAAGUUGGGCGGACUAUGAGCGUCUAUUGUUUCCACGCCCAUUAAGCAACGAUAUAUCACUGACGACGGACCGGCACUCACAUUGCGGACUUGCACUUAAUAUAUUACUUCUUACAACUCAAAUAGCUACGACACUUCCUUAUAGGAAGAGAUCGAUUAUUCGAGUAUUAACAGAUCAGCGUCCCCAUCCUUGUUCGAGGGGCACAUCUCGGUCCGAAGAUACUGUUCAUGCUUUCAGGUGCGUUAGCGCUCCGCCCGGUACCUCCGUUCUCGCGACCAUGCGGACUAGUUGUCGUGAGAUCUCCCGACCCCGAGCGUACUCCGCGAAUCUUGAUGUACUCACGCUGAAGAAAAUAAAUCGUGAAUCUGCUGAGCAUAAUACACCACUAGACUACUGGCUAAAUGUUACGCCUAACGGUCGCGGGGCCAAGAAAUCAGCACUAUCCGCUGCAAGCAAAACUACUUGUACGGUACUGUACGAGCGGCCUUGUGACAUGCCCCGGACGUCAGAUGGAAAGUCAAACAGGCAGAUCAGCGUAUCAGAGAUUAAUUUUAAUACGGAUUCCGACCUGCGCAUCGGGAGGAGCCGUAAGCGGCAAGUAACGGACUGGGCUGCUAGAGGGGGCUUGCCUCACUACCAUGAGUGGGGGCUUCGAGUAUCGGUCUAUCAUGACGGCCCAUCACUGACGAAAGGCAGCCCCUCUGCGCGCGGUCAGUCUCAGUCUUAUGAUGAAUUAUUUUGCAGCUAUAUCCCCCAUUGCCUCGCUAGACAGCAGACACCGCGACCGCUUCCUACGCUUAACCUUCACGUCGGAUCAUGGCCUGCCGACAAGUUGUACCCGACAGCGAUAUGCCCUAGGCAGAAGUCGUCAACGGAGGCGGCUAUCUUGCUGCCCACAUGGUGCCGGCUACGGGGAUGUAUUGGUUGGCAAAGCGCUCUAACUUCUCUCGAGUUCGAAUGCGGUUGCAUCGUCUUUAGUUCACAAGUGUGCUGGGUCUGUCCGGUCCGGUCAAUAUGUCCUAAAUAUAUUCACUCAGUCAGCGACACACCCCGACAAGUUAAAUUCUUAACUCUAACUUAUAACAUUCUCGUACACCCGAAGAACGUCGGAGCCGAUAAUGGCAGAACAUAUGUACAAGCCAUGAAUCAUUGCGUUAUAUGCCCCUCACUGAUUCAACGGUCUCUGGUUCUCGGAUGGACGGCGCAGUGCUAUGUUAUUGUCGACGAGUAUGUCACGCAAGCUGCAGUUAGAUCCGUAAAGCAGACGUUUGAAUUAAGCUGUGUCUGCUUGAGUCCGCAGGUUCGGGGGUGUUUCCAACGCUUGUGUUUGGUCGAGCACUCUUUACAGCCCCUGCGCAGUGUCUAUUCACGCACACGGGUCAGACCAUUUUCUGUCCAGAGACAUGGCUCGGUAACUUGCCUAAGUUGUGGCGGGCGCGGGUUGAGAAUGACGCCUCACUCGCAUCCCCUGGCUAACAGUCCCCAUGGCCAUUGGGUUGUAUCACUCACAUCUGUGACCGGCAGGGCACGACAUCCCAUCAUUAAUGGCGAAUCGCUACGCGUAGAUGUAUGGUUCUACAUAACAGACGGGACACUGUUUUAUUGCAUCCUCGCAAAACGGAACUAUAUUGAACCAGCUUCCAGGCGUUUGGUCACCACAAAGCAACGAGAAGUAGAUAUAAGCCCUCUCAAGAUAAUCGAAAGGCAAUCAGAACGUGAAGUCUGGGAGAAGGCAGCGGUAAUCCCUAUCAAAUUUAGUUUAGAACGAGACCGUCUCGACGUCGUGAGUCACGUGGAUUUGCGAUCUAACAACCGCGCCAUAGCUUAUCACCUAAUGUCGCUAUAUGGGUCCUCUGUGCGGACUGAGCAAGAAGGUCGAACGGAUCUAUCCUCACACUGUUCAAGGCCUCUCAAGUACAUAGGGGAUUUUUACGUCCUGCAGUAUCGAUUUAGCAUAGACAGUAUUGUAAUUAAUAAGCGUGAUCAGGUGACACAUAUUCCUCAGCGCGACACUGCGUAUGCUGGUCGUAUGUGCGGCCUGAAACUAUCGAAUGGCAGUGUCCCUAACACGGAGCAAACGUCUCGGCCCCCCCGAACUUAUUGCUGUAUUAGCUUCCCACUUCAGAGUGAAUUAGCGCCAGUGACAGCGCAUCGGUUUGGGCAGCAUCUGGUACUACAGAGAUUCAUGCGGGCUCACUUACGAAACGGUCAGUUCGGCCUACGGAGCGUUAGCAUGUUCACGUCCCUAGACUGUAAAGAGUCCUCUGGGGAGUCAUUUUUCAGAACCGGAAGGAUGGUCUACUCCCGGAGUGCGCUAUUUGCGAGCCCCGCAGUACCUGAUUGCAUCUCUCGUGAAGCUCCCAAGCCUAAUCCUAGGCGAGGCCGGAUUGUAUCACACUCAACGAUCUCCAGAAUACGCCGCGAUCAAUUCGGCGGACGACUAUCGGUGCCAAAAUACAUGACCGCUUGCAAGUACUACCAUAGCAACUUCUUAUAUCAGGGACGCCCGUCACGCGUGACAUUGUACCCGAGACGUGCCAGGUUACCGUCGAGAGGUGCGCCCCGUGAUUCCGGGGAAUCCGUCCAAGAGCUGGCACGCUUGCAUCAUCCGUGUACGGAGGGUCUUUCGAUUCGGGAAAGGACAAUUGCCGGGUCUCGACCUGAUCACUGCUGGAUCGCACGCCAGUUGUCGCACGUCCCAGUGCCCACGAGAAUCUCGUUUAAAGUGUGCGUAACUCCUAAGAGGCCGCUAUGGGAAAAACCACCUCAAGAUGUCUACCGUACCACAUGGGUCGGGUACGCUCCCGAUGAAAGAGUCUAUAACGCACUCCUUGGAACGAAAGCGUAUGUCGGGUGGGUCCACCCGACAGGAAUAUUGCUGCUCGGAGACACGCAAAUAUACCACGACUGGGCACGUAUUGCGUUGCCGCGGAUAUUACUCUAUAUGUGUCAGUUGUUGUUAAACCGGGUAAUUGCAGCGUUGCGCACAAAACUCGCUUCCGUAUUUGAAGCCCGCUAUGCGUAUGGUACCACAAGACAUGAACGCUGGAUACAGUGGGUCACGCACGUAGGCUCUUAUCGCACCCGUCUUACCCUAUUGUCUCUUUCGUAUAAUAUGGGAGUCCCUGAGACAAGACAAGAGCCAAACACUCACUUUUCAGGGAAUCCUCGACCCGCCACCGUGGCAUCGGUAAACUAUGAGGACUCAACGAUCCGGAUCCACCCGAUCCGGAUCGAUCAAAGCUGUCACAGUACCUUUAGCGGCUAUACCGCCAGAUUAGCCCGUGAACGAGACAACUCCCGGCGUGGUAACCAUCCAGUCAGUGUUAUUAUGGUCCCUAUGAUCACUUUCCGAGAUAUAAUACCUGCAAGUUGGCCAGCGUUUCCAUGUAAUUCGUCCGUAAGGCGACACGAACCUAAUGAGGAGUCUUUAGUCUGGCCGCAUACGUGUCACCAGGAAAAUUUUCUGGCGAGACGCGCUACCUCACGUGGCUCAAUAGAAGCGUGGGCGUGCUAUCGCCUCUGGGAGGUGCUGAUUCCGUGCCGGCCAUUUCAUAUUUGUCUGAUCACAGUUAAGUCUGUGCAUUCGAUCAGUCUGCUCAUGCCGUUAACCGUGAUUGAGUUCCGCAGCAGUGCGUAUCAGAUGGCGUGUACACGAUCGCUAUGGCAAAAGAGGCCCUGCUUGAUGGAAACAAUUGCCAGACAAACAGGCGCACGUGAGAAAUGUCAACUAACACCAGGAAAACUUGUUUGGUAUGACUUUGAGUACCGGACGCCUCCCUGUUUAGGGGAUAGCAAUGUGAUGGGGGGCCCGGCUGUUGACUUCUUUGCUCACCAUAGGGCCACCAGGGAGAGCUUAGCUCGUCCAGCCACAGUCUAUUACACUCUUCCUUCCAUGGGGGUCGUCAGAAUCAAAGGAUGUCUAGAUUUACCGACAGUCCUCAUACGACUCUCACCAGCAAUAGACUACAUAUGCGCAAGAUCGGGUGCCUGCAUUUCUUCGAUUGUGUUUUUCUGCGGGCCCGUAACUUUGCUGUGUUCAUACCAGCUCUCAGGGAAGGACUAUCGUCGCCUACCGUAUGCUAACGGACUACAUUCAAAUCGUAGAGCGCCAGUACAAGUCACGAACGCGGUCAAAAGGUUUAUAGAACUUUUGCGCAGUCUCAGUCUCGCGCCACAAUCAGAGGUGUUUGAUAAAUUACAAUGUUAUUUGGAAUGGCAUGGCGACUUCUGUUGUGAUCGCGAUGAGCUGUGCUAUUUAAGUACGCUUCGCAACGGAGUCUAUACUAGCGAUGUUCGCCAAUGCUCUCCUAGACCGCAUUUAUCAAAUCUCCGUAGCGGGACACCCUUGCCGAGUUUUAGCGGAAUAAUUGUUCCAACGCACUCACCACACGUUGCCGCGGUCAACGCCACAAAAACGUGUAUUGCCCGGAAAGAGUAUGGUACGUUUAGAGAAGCUGCAAGGGUCGUUGACACAGAGUAUAGGUGGGCAUCGGCGAGAGCUACCAAACCCCUAAAUAUCGCACUACACAUUGCGUUGCAAGUUAUGAACCUUAUCAUACCGCACCCGGUCGCUGCGAAAAAGACGGCCGAACGCGAGCGUUCAGCGAGCUACAGUGUCCCUGGUCUCGCUAUGGGGUACAGUCUUUUGCAUGCAGCAAUAAUCGGAACACCGCUUUCAGUCAUCCCCUACUGGCAUUACUCUCGUGCACCCCCCCGAAGAUGUCUUACAUCGCUCGUGAGACGGGGCCAGGCGUGCGCCAGAUUGUUCUCAGGUCAGUUGGUGGUCGGGAAUGGCCGCUACGUCGUUAUCCCCGCAGUCCAAAUCGAGGAUAAGACGGGGUUACUCUAUGCACCAAAAAGAUUGUCUCGGCCUUACUCCCCCGGUUCCUGCCGACCAACGAUUCACGUACUCAUAAUUAUGCGUGUCUCGGCGCAGGUCGUUAGCUGUUUAGCGUGGGGAAGUGCGUUCACAGGGUGUCACACUCGUCAAAGCUCUGGUUGGUUAGGCCAUAAGGAACGUAGAUAUCCCAACCUAUGCUGGCUCUUUGACUCGAGCAUUUAUGCUGAGCUCAAACUUUGUCAACCCAGUGUAACGCGUGCCGAAAUCACGUAUGAGGGGCCGAAGCCCGGCUGCUGUGCCGUGUAUCGCCACGACGGGUCCUAUGUGCCUACUUACAAGGAUACUCCGCUACAUCGGUACAGUCCGGUCUCAUUCGCCAAAUUCACCUUAUCUACUGAUUGUGAUACAAUGAAUCGCCACACCGGGAGUUGGAAUCUGUGGAGUCAUACCGCCGGCAAAAACACGCCAAAGAAUCGGUUGAGUCGGCCGAAGCAAUUGUGGCCACUAAAGGUGUACUCGGCCUUCAUAGUUGAGUCUGUGUGGAUCGGACGCACUCACAGUUGCGUGUGGAACCCGGUACUCCGGGUCAUUGGCGAAAUAAAUGCUAGACUCGAACAGACAGCAACCGCAGAUGAGUCCUGUAGCAAACUCGCUCUUUCAAAUAGGGCGUUGCGUUAUUGGGGCCCUCUUCUCAGAGUGACAGGGCCUCUCAGCUUACCCGACGUAGUUGAACUGUACUUCUCUACGGUAUGGCAUUAUUGCAUUGCUCUCAUAUAUGCCUGUGAAGCUGUGGAUGGACCGUAUCGUUUAGGGGUACACCCAGAAAUAAGCGCACGUGCCCAGAAACCUAUAAAAGUAAAACCAGGCAGCACUGCUAACAUACGGGAUGGCGAUCUGAUUAUAGCUUCCUACCACGGUGGCUCUCUUCCUAGAGGAAAUGCUACCAGUAAGACAUUAAGCGAGUCCCGCGUCCGGUACUCAAUCCGCUCCAUCAAUCUAGGGAAGUUCCAGUUUUUCUUCAACUACAUGGGCAGUGCCAAGUCGGAUGACAGUGGCAGAUUUGGAACCAAAAGGGACGUACGUGUCAGGUUACCACCUGUCGGUUCGACUGAGGCACCUGUGUCUCAUAGGAAUUGUCACAUCUCGACGACAGGAGUUGACUACUCGAUGUCGUCUCCGCCUACGGUCGGUCAUACACCCCUGUCUCGAGCGCUCCGCCCGUUGCCGGGCUCCGCCCCGGGAGUAAACACUCGACCGGUGGUUGUAUUGGGCGUUAUGGCCCAGAUUAGAUCCACUCCCGCGAUAACGCCUAGCAUCGCCCUCAACCGGGCGGUUAAGGAGAGUUACGCUAGGAAGAUUGCCCAGCUCCGCUUAAUCCAACCCUCAAAGUAUUUUAUACAUGUACAUUUGCCAGGGACGAGUCUCCGCGAGGUGUCCGUAUUGUCGUUAGAUACCCGGGUGUGCCCAAAAGCGCUUUGUGCAGCUAACAUUGUAAGACGUUCUUAUCGGAACUCAGAACUGCAACUGCGUGUUCGUAGUCAUCGAAGACCUAGGUGCGAAACCUUAUGGAUAACACUAGCGGAGGGCCGUACGUGCCCCGCAAGCUGCACCAUCAACCCGGCCGAGCUGCUGCACAUAAUCGAUUUACUCCCAGGGUUCAUUUCGAGCACUCCAGAGCGGCCGUCGGGUUACUGCUUAGUAGAAAGGGAGGCCAGCGAAGAUGUACGUAAGAUACAAGAGCCGCAACUUCGGAGUCCCUUGCGUUCGUCUUUGGGUGGAACGGGUGAACCGGGGCCUACUGUAGUCCAAUGUGGCGACGAAGGAUCCGCAAAUUUGGACCAGGGGACGGCAGCGCCCCACGAUGUUACGAAUUUUAAGGCAGGCGUGGAGGAAAUUGAAGGUGGUCUUCAAGCUCCCUCUGCAAUUGACCGUGCUCGUUCGCAAAGAGGAACCCAGCGUACCGACCGAGUUCCGCCAAUUUACGCCAGACAUGGGUACGCAUUCACUUCCACGCAGGACUACAUUCCUCCGAAAAUCCUGACUUCCCACUUUAGACUCGGUCCAUAUUACCUUAUCUCGUUAUCCUGGGCCUUAAGGGGUUCUACUGCCUUAGACACCGAUUUCGAUAUUCAAGACUCCUACGGCGGCGGCGUCAAACCUUCCGGUUCAGCUGCUGGAGACUCUGUGGAGUCUAUUAUGGAGGGCAGUACGAUGCUUGUGGUUCAUGAAUCCAUCCAUAACCUAGUGGCAAAGAGCUUCGUUGCGGGGUCUGGUCUAGCAGAAUGGUCUUUAUUGGUUUCUUGA")

# Translate the RNA sequence to protein string
protein_string = translate_rna_to_protein(rna_sequence)

# Output the result
print(protein_string)