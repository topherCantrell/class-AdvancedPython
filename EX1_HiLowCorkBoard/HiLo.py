import random

print("I am thinking of a number between 1 and 100")
print("You guess it!")
print("")

number = random.randint(1,101)
# print ("Number:"+str(number))
score = 0

while True:
    guess = input("What is your guess? ")
    g = int(guess)
    score = score + 1
    
    if g<number:
        print("Higher! Your guess is too low.")
        
    elif g>number:
        print("Lower! Your guess is too high.")
        
    else:
        print("You got it in "+str(score)+" guesses.")
        break