import random
name = input("Welcome to the Guessing Game! What's your name: ")

         
def start_game():
    guess= print(f"Hello, {name}. You have 4 chances to guess it. Let's go!")
    x= random.randint(1,10)  
    attempt= 0
    attempt_limit = 4
    while guess != x:
        try:
            attempt += 1
            attempt_limit -= 1 
            guess= int(input("Try to guess a number from 1 to 10: "))            
        except ValueError:
            print("Sorry, you have to try a number")
            continue
        if guess > 10 or guess < 1:
            print("sorry, it have to be from 1 to 10")            
            continue
        if attempt_limit == 0 and guess != x:
            print("Game over")
            break         
        if guess > x: 
            print("its lower")            
            continue
        if guess < x:
            print("it's higher")
            continue   
        else:
            print(f"congratulations, {name}. You guessed it after {attempt} attempt(s)")   
            break
        
            
start_game()
#add a next chance













