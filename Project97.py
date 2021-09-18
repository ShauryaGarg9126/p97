import random
print ("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print ("Guess A Number Between 1 and 9")
while chances<3:
    guess = int(input("Enter Your Guess :"))
    if number==guess:
        print ("Congratulations You Won")
        break 
    elif guess<number:
        print ("Guess A Higher Number")
    else :
        print ("Guess A Lower Number")
    chances +=1
if chances==3:
    print ("You Lose The Number Was ",number)           
     
