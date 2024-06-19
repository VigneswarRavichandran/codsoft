import random
options=("rock","paper","scissors")
program=True
while program:
    #player's choice
    pchoice=input("Enter any one of the choices(rock,paper,scissors):").lower()
    if pchoice not in(options):
            pchoice=input("Enter any one of the choices(rock,paper,scissors):").lower()
    #computer's choice
    cchoice=random.choice(options)
    print("player's choice:"+pchoice)
    print("Computer's choice:"+cchoice)
    if pchoice==cchoice:
        print("It's a tie")
    elif pchoice=='rock' and cchoice=='paper':
        print("Computer wins!")
    elif pchoice=='rock' and cchoice=='scissors':
        print("Player wins!")
    elif pchoice=='paper' and cchoice=='rock':
        print("Player wins!")
    elif pchoice=='paper' and cchoice=='scissors':
        print("Computer wins!")
    elif pchoice=='scissors' and cchoice=='rock':
        print("Computer wins!")
    else:
        print("Player wins!")
    #asking the user if they want to continue the game
    play_again=input("Do you want to play again(yes/no):").lower()
    choices=("yes","no")
    if play_again not in(choices):
        play_again=input("Do you want to play again(yes/no):").lower()
    if play_again=='no':
        program=False        
print("Thank you for playing") 
