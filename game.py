from random import randint

rps = ('rock', 'paper', 'scissors')

def user_input():
    a = 0

    while a < 5:
        user = input("What will you play? (Paper, Rock, or Scissors):  ").lower()
        if user in rps:
            return rps.index(user)
        else:
            print("Invalid input")
            a += 1

    print("Exiting")
    exit()

def comp_input():
    num = randint(0,2)
    return num


def decide_winner(user, comp):
    res = user - comp
    if res == -1 or res == 2:
        return 'lose'
    elif res == -2 or res == 1:
        return 'win'
    return 'draw'

rounds = int(input("How many rounds would you like to play? "))
print()

r_counter, comp_score, user_score = 1, 0, 0

while r_counter <= rounds:
    print("Round " + str(r_counter))
    user = user_input()
    comp = comp_input()
    game_res = decide_winner(user, comp)

    print("You played " + rps[user] + " : Computer plays " + rps[comp])
    
    if game_res == 'win':
        user_score += 1
    elif game_res == 'lose':
        comp_score += 1
    elif game_res == 'draw':
        r_counter -= 1
    
    print("You " + game_res + " the round")
    print("You " + str(user_score) + " : Computer " + str(comp_score))
    print()
    
    if rounds % 2 != 0:
        if comp_score >= rounds / 2 or user_score >= rounds / 2:
            print("We have a winner!")
            r_counter = rounds + 1
    else:
        if comp_score > rounds / 2 or user_score > rounds / 2:
            print("We have a winner!")
            r_counter = rounds + 1
    r_counter += 1
print("Final Score: You " + str(user_score) + " : Computer " + str(comp_score))