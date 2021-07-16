import random

random_list = [random.randint(-100, 100) for x in range(10)]
for x in random_list:
    if x < 0:
        print(f'Number {x} is negative')
    else:
        print(f'Number {x} is positive')
