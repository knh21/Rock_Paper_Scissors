import random
# a function for the users input
def play():
    user = input("What do you chose?\n 'r' for rock, 'p' for paper, 's' for scissors\n")
    # computer randomly chooses one of these three choices
    computer = random.choice(['r', 'p', 's']) 

    if user == computer:
        return 'It is a tie'

    if is_win(user, computer):
        return 'You won!'

#  only reaches this return if none of the above is true
    return "You lost!"

    

# function to check who won and will return true if player wins
def is_win(player, opponent):

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())