'''4. random → Rock Paper Scissors Game
 
Use random.choice() to let the computer play Rock–Paper–Scissors against the user.
 
Sample Input:
 

 
User: Rock
 
Computer (random): Scissors
 

 
Sample Output:
 

 
You chose Rock, Computer chose Scissors
 
You Win!
 '''



import random

def rock_paper_scissors():
    options = ['Rock', 'Paper', 'Scissors']
    user_choice = input("User: ").capitalize()  
    computer_choice = random.choice(options)
    
    print("You chose", user_choice + ", Computer chose", computer_choice)
    
    if user_choice == computer_choice:
        print("It's a Tie!")
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        print("You Win!")
    else:
        print("Computer Wins!")

rock_paper_scissors()
