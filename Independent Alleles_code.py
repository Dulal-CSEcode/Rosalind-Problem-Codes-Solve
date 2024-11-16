import math

def binomial_prob(n, x, p):
    """Calculate the probability of having exactly x Aa Bb individuals in a population of size n with probability p for each."""
    return math.comb(n, x) * (p ** x) * ((1 - p) ** (n - x))

def mendel_probability(k, N):
    # Number of individuals in the k-th generation
    n = 2 ** k
    # Probability of a single individual being Aa Bb
    p = 1 / 4
    
    # Calculate the probability of having at least N Aa Bb individuals
    prob = 0
    for x in range(N, n + 1):
        prob += binomial_prob(n, x, p)
    
    return prob

# Example usage:
k, N = 5, 8
result = mendel_probability(k, N)
print(f"{result:.3f}")