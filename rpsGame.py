import random, sys

# Give the user the name of the game they are playing
print("Let's Play Rock, Paper, Scissors.")

# These are the variables to keep track of the nuber of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop
    print("%s Wins, %s Losses, %s Ties"  % (wins, losses, ties))
    while True: #The player input loop
        print("You are playing against the Computer in a Rock, Paper, Scissors game:\n Enter your move: (r)ock, (p)aper, (scissors or (q)uit")
        player_move = input("> ")
        if player_move == "q":
            sys.exit() # Quit the program.
        if player_move == "r" or player_move == "p" or player_move == "s":
            break # Break out of the player input loop.
        print("Type one of r, p, s, or q.")

    # Display what the player chose.:
    if player_move == "r":
        print("ROCK versus...")
    elif player_move == "p":
        print("PAPER versus...")
    elif player_move == "s":
        print("SCISSORS vs....")

    # Display what the computer chooses.
    move_number = random.randint(1, 3)
    if move_number == 1:
        computer_move = "r"
        print("The Computer Plays: Rock")
    elif move_number == 2:
        computer_move = "p"
        print("The Computer Plays: Paper")
    elif move_number == 3:
        computer_move = "s"
        print("The Computer Plays: Scissors")

    # Display and record the win/loss/tie:
    if player_move == computer_move:
        print("It is a tie!")
        ties = ties +1
    elif player_move == "r" and computer_move == "s":
        print("You win!")
        wins = wins + 1
    elif player_move == "p" and computer_move == "r":
        print("You win!")
        wins = wins + 1
    elif player_move== "s" and computer_move =="p":
        print("You win!")
        wins = wins + 1
    elif player_move == "r" and computer_move == "p":
        print("You lose!")
        losses = losses + 1
    elif player_move == "p" and computer_move == "s":
        print("You lose!.")
        losses = losses + 1
    elif player_move == "s" and computer_move == "r":
        print("You lose!")
        losses = losses + 1
