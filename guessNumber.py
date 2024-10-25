import random
def guess_number(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_num:
            print("Sorry! Try again, Your guess was too low :((")
        elif guess > random_num:
            print("Sorry! Try again, your guess was too high :((")
    print(f"Yayy, congrats. Your guess {random_num} is correct!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high: #randint throws an error if both high & low are equal
            guess = random.randint(low, high)
        else:
            guess = low #could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay! The computer has guessed your number {guess}, correctly!')

computer_guess(1000)
guess_number(25)