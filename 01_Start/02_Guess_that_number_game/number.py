import random

print('----------------------------')
print('       NUMBER GAME')
print('----------------------------')

guess = -1
number = random.randint(0, 100)

name = input('What is your name? ')

while guess != number:
    guess = int(input('Guess a number between 0 and 100: '))
    if guess < number:
        print(f'Sorry {name}, your guess {guess} too LOW')
    elif guess > number:
        print(f'Sorry {name}, your guess {guess} too HIGH')
    else:
        print(f'{name} you won! Your guess {guess}')

print('Done!')