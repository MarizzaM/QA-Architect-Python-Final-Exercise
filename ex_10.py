numbers_list = []
number = 0
while number != -1:
    number = int(input("Please enter the number (HINT: for exit enter '-1'): "))
    numbers_list.append(number)

s = 1
for x in numbers_list:
    s += x

print(f'The sum of entered numbers is {s}')
