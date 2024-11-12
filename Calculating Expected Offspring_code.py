def expected_dominant_offspring(couples):
    # Extract the number of couples for each genotype pairing
    AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa = couples
    
    # Calculate the expected number of dominant phenotype offspring
    # For each genotype pair, we calculate 2 * (couple count * probability of dominant offspring)
    expected_offspring = (2 * (AA_AA * 1 +
                              AA_Aa * 1 +
                              AA_aa * 1 +
                              Aa_Aa * 0.75 +
                              Aa_aa * 0.5 +
                              aa_aa * 0))
    
    return expected_offspring

# Example usage:
couples = [18843, 18336, 16273, 18948, 18376, 18376]  # Input for the six genotypes
result = expected_dominant_offspring(couples)
print(f"{result:.2f}")