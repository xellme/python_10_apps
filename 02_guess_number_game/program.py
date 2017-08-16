import random

print('---------------------------------')
print('      GUESS THAT NUMBER GAME')
print('---------------------------------')
print()

that_number = random.randint(0, 100)

while True:
    guess_text = input('Guess a number a between 0 and 100: ')
    guess = int(guess_text)

    if guess == that_number:
        print('{} is correct'.format(guess))
        break
    if guess > that_number:
        print('{} is too big'.format(guess))
    else:
        print('{} is too small'.format(guess))


