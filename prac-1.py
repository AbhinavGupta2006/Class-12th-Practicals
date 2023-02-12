import random
while True:
    print('Guess the number between 1 and 50')
    n=random.randint(1,50)
    while True:
        guess=int(input())
        if guess<n:
            print('The number is larger than',guess)
        elif guess>n:
            print('The number is smaller than',guess)
        else:
            print('Correct! The number is',guess,'\n')
            break
