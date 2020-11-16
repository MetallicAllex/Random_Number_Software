import random
"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""

my_randoms = list()
for i in range(67):
    my_randoms.append(random.randrange(1, 67))

# Generate a list of numbers 1..67
numbers_1_to_67 = range(1, 67)

# Iterate from 1 to 67
for number in numbers_1_to_67:
    the_numbers_match = False

    # Iterate your random number list here
    for random_number in my_randoms:
    # Does my_randoms contain number? Change the boolean.
        if number == random_number: 
            the_numbers_match = True
            print(f'{number} is in the random list')