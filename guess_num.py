import random
r = random.randint(1,100)

while True:
    num = input('Please enter a num[1-100]: ')
    num = int(num)
    if r == num:
        print('Bingo!! the answer is ' + str(r))
        break
    elif num > r:
        print('the answer is smaller than ' + str(num))
    elif num < r:
        print('the answer is bigger than ' + str(num))
