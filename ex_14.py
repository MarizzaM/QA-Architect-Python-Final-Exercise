import random

random_number = random.randint(1, 10)
guess_number = int(input('Please enter number from 1 to 10: '))

if random_number == guess_number:
    print('Very good')
else:
    print('Wrong')
