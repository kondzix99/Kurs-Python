import random

def random_with_sum(number_of_values, asserted_sum):

    trial = 0
    numbers = list(range(number_of_values))

    while True:

        trial += 1

        for i in range(number_of_values):
            numbers[i] = random.randint(1,101)

        if sum(numbers) == asserted_sum:
            record = (trial, numbers)
            yield record
            trial = 0

for i in range(10):
    (number_of_trials, numbers)  = next(random_with_sum(3,100))
    print("Wylosowane liczby w probie {} to {}".format(number_of_trials, numbers))









