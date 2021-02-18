import random
r = random.randint(1,100)
count = 0
while True:
    count = count + 1
    num = input('Please enter a num[1-100]: ')
    num = int(num)
    if r == num:
        print('Bingo!! the answer is ' , r)
        break
    elif num > r:
        print('the answer is smaller than ', num)
    elif num < r:
        print('the answer is bigger than ', num)
    print('You have guessed' , count , 'times!')