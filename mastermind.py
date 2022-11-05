import random
num = random.randrange(1000, 10000)
print(num)
chances = 5
guess = int(input(f'Guess a 4 digit number, you have {chances} chances left:  '))
if guess == num:
    print('Great you won, now you are a mastermind')
else:
    tries = 0
    while guess != num and chances > 0:
        tries += 1
        chances -= 1
        rightDigits = 0
        guess = str(guess)
        num = str(num)
        correct = ['X'] * 4

        for i in range(0, 4):
            if guess[i] == num[i]:
                rightDigits += 1
                correct[i] = num[i]
        if rightDigits < 4 and rightDigits > 0 and chances:
            print('Not the right guess, but you guessd', rightDigits, 'numbers right')
            print('Current status is:')
            for char in correct:
                print(char, end='  ')
            print('\n')
            print('\n')
            guess = int(input(f'Guess a 4 digit number, you have {chances} chances left:  '))
        elif rightDigits == 0 and chances:
            print('None of the digits you guessed is right')
            guess = int(input(f'Guess a 4 digit number, you have {chances} chances left:  '))
    if guess == num:
        print('Great you won in', tries, 'guesses, now you are a mastermind')
    if chances == 0: 
        print('sorry you lost as you ran out of chances')
        print('Number is', num)