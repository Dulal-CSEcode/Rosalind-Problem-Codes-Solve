def mortal_fibonacci_rabbits(n, m):
    # Initialize a list where each element represents the number of rabbit pairs of a given age
    # Since rabbits die after `m` months, we need a list of size `m` to track the age distribution.
    ages = [0] * m
    ages[0] = 1  # Initial pair of newborn rabbits in the first month

    # Simulate each month
    for month in range(1, n):
        # The number of new rabbits is the sum of all rabbits that are old enough to reproduce
        # which are the rabbits in all age groups except the newborn group (ages[1:] sum)
        new_rabbits = sum(ages[1:])

        # Shift ages: move each age group one month forward
        # The oldest group (last in the list) dies off, and others get older
        ages = [new_rabbits] + ages[:-1]

    # The total number of rabbits is the sum of rabbits in all age groups
    return sum(ages)

# Example usage:
n = 83  # Total number of months
m = 18  # Lifespan of rabbits in months
print(mortal_fibonacci_rabbits(n, m))