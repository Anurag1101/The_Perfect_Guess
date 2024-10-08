import random

def game():
    num =random.randint(1,100)
    guesses=1
    
    while guesses!=0:
        guess=int(input("Guess the number: "))
        if guess==num:
            print(f"You Guessed the right number {guess} in {guesses} times")
            break
        elif guess>num:
            print("Lower number please ")
        elif guess<num:
            print("Higher number please ")
        guesses+=1
    play_again = input("Do you want to play again yes/no: ")
    if play_again.lower() == 'yes':
        game()
    else:
        print("Thank you for playing the game")
    
game()






         

