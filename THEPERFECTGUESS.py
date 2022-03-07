import random

randNum=random.randint(1,100)
guesses=0
userGuess=None


while(userGuess!=randNum):
    userGuess=int(input("Enter your guess : "))
    guesses+=1
    if(userGuess==randNum):
        print("YOU MADE A RIGHT GUESS!")
    else:
        if(userGuess>randNum):
            print("YOU GUESSED IT WRONG! ENTER A SMALLER NUMBER") 
        else:
            print("YOU GUESSED IT WRONG! ENTER A LARGER NUMBER")     
      
print(f"YOU GUESSED THE NUMBER IN {guesses} GUESSES")   
with open("hiscore.txt","w") as f:
    f.write(str(guesses)) 
