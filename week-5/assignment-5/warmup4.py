
for row in range (1,31):
    if row % 3 ==0 and row %5==0:
        print('FizzBuzz')
    elif row % 5==0:
        print('Buzz')
    elif row % 3==0:
        print(f'Fizz')
    else:
        print(row)

