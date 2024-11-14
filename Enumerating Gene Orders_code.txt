from itertools import permutations

def generate_permutations(n):
    # Check if n is within a reasonable range
    if n > 7:
        print("Warning: For large n (> 7), generating all permutations may be computationally expensive.")

    # Calculate all permutations of length n using itertools.permutations
    perms = list(permutations(range(1, n + 1)))
    # Total number of permutations
    total_permutations = len(perms)
    return total_permutations, perms

if __name__ == "__main__":
    n = int(input("Enter a value for n (≤ 100): "))  # User input for n
    if n <= 100:
        total_permutations, perms = generate_permutations(n)

        # Print total number of permutations
        print(total_permutations)

        # Print each permutation
        for perm in perms:
            print(" ".join(map(str, perm)))
    else:
        print("Please enter a value of n that is less than or equal to 100.")