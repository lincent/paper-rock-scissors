from random import randint

def user_input():
    a = 0

    while a < 5:
        user = input("What will you play? (Paper, Rock, or Scissors):  ").lower()
        if user in ('rock', 'paper', 'scissors'):
            return user
        else:
            print("Invalid input")
            a += 1

    print("Exiting")
    exit()

def comp_input():
    num = randint(1,3)
    if num == 1:
        return 'rock'
    elif num == 2:
        return 'paper'
    return 'scissors'
    
def decide_winner(user, comp):
    if user == comp:
        return 'draw'
    elif user == 'paper' and comp == 'rock':
        return 'win'
    elif user == 'paper' and comp == 'scissors':
        return 'lose'
    elif user == 'rock' and comp == 'scissors':
        return 'win'
    elif user == 'rock' and comp == 'paper':
        return 'lose'
    elif user == 'scissors' and comp == 'paper':
        return 'win'
    elif user == 'scissors' and comp == 'rock':
        return 'lose'


rounds = int(input("How many rounds would you like to play? "))
print()

a = 1
comp_score = 0
user_score = 0

while a <= rounds:
    print("Round " + str(a))
    user = user_input()
    comp = comp_input()

    print("You played " + user + " : Computer plays " + comp)

    game_res = decide_winner(user, comp)
    
    if game_res == 'win':
        user_score += 1
    elif game_res == 'lose':
        comp_score += 1
    elif game_res == 'draw':
        a -= 1
    
    print("You " + game_res)
    print("You " + str(user_score) + " : Computer " + str(comp_score))
    print()    
    
    a += 1
print("Final Score: You " + str(user_score) + " : Computer " + str(comp_score))