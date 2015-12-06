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
        print("It is a draw")
    elif user == 'paper' and comp == 'rock':
        print("User wins")
    elif user == 'paper' and comp == 'scissors':
        print("Computer wins")
    elif user == 'rock' and comp == 'scissors':
        print("User wins")
    elif user == 'rock' and comp == 'paper':
        print("Computer wins")
    elif user == 'scissors' and comp == 'paper':
        print("User wins")
    elif user == 'scissors' and comp == 'rock':
        print("Computer wins")
    return

user = user_input()
comp = comp_input()

print("User plays " + user)
print("Computer plays " + comp)

decide_winner(user, comp)