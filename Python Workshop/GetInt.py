min = 10
max = 40

cornum = 25
maxguess = 3
guesses = 0

for num in range(3):
    guess= int(input("Place guess here: "))
    guesses += 1
    if guess == cornum:
        print("Well done! You got it correct!")
        print("Game over!")
        break
    print(f"you have done {guesses} guesses")
else:
    print("You lost! Sorry...")
    print("Game over!") 