def total_rabbit_pairs(n, k):
    # Initialize base cases
    if n == 1 or n == 2:
        return 1
    
    # Create a list to store the number of pairs at each month
    rabbits = [0] * (n + 1)
    rabbits[1], rabbits[2] = 1, 1  # F1 = F2 = 1
    
    # Build up the solution using the recurrence relation
    for i in range(3, n + 1):
        rabbits[i] = rabbits[i - 1] + k * rabbits[i - 2]
    
    # The nth term is the solution
    return rabbits[n]

# Example usage
n = 33  # number of months
k = 2  # number of rabbit pairs produced by each reproduction-age pair
print(total_rabbit_pairs(n, k))  # Output: 
