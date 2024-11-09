def dominant_phenotype_probability(k, m, n):
    # Total number of organisms
    total = k + m + n
    
    # Probability of each mating combination
    # P(dominant | k-k) = 1
    kk = (k / total) * ((k - 1) / (total - 1))
    # P(dominant | k-m) = 1
    km = (k / total) * (m / (total - 1)) + (m / total) * (k / (total - 1))
    # P(dominant | k-n) = 1
    kn = (k / total) * (n / (total - 1)) + (n / total) * (k / (total - 1))
    # P(dominant | m-m) = 3/4
    mm = (m / total) * ((m - 1) / (total - 1)) * 0.75
    # P(dominant | m-n) = 1/2
    mn = (m / total) * (n / (total - 1)) * 0.5 + (n / total) * (m / (total - 1)) * 0.5
    
    # Total probability of dominant phenotype
    probability = kk + km + kn + mm + mn
    
    return probability

# Sample Dataset
k, m, n = 27, 26, 18

# Calculate and print the probability
result = dominant_phenotype_probability(k, m, n)
print(f"{result:.5f}")
