from random import randint

#ALL VARIABLES USED IN THE PROGRAM
roll = []               #you start with an empty list for rolls.
dice_number = 5         #you start each turn with 5 dice.
mud_pit = 0             #and no dice in the mud pit.
player_score = []       #and an empty score that will accumulate with each round.
computer_score = []     #separately, an opposites score.
round_count = 1         #this will go up with each round and reset for opponent.
turn = 0                #0 = computer, 1 = player because i'm clever liek thaT???
user_response = False
running = True

def dice_roll(player):
    global mud_pit, dice_number         #Missing key to get global variable recognized in this loop.
    for i in range(1, dice_number+1):   #This will generate a randint each time + add it to the roll list..
        roll.append(randint(1, 6))
    player.extend(roll)                 #add the roll to the score list to be summed up.
    for i in roll:
        if i == 2:
            mud_pit += 1
            dice_number -= 1
        elif i == 5:
            mud_pit += 1
            dice_number -= 1
    return roll, mud_pit

# Returns True when the player or computer wins
def doDiceRolls(score):
    global mud_pit, dice_number, user_response, turn, round_count
    while dice_number > 0 and sum(score) < 200:
        while not user_response:
            user_response = input("Type anything to proceed with the next round: ")

        if turn == 1:
            print("-----------------\n", "Round", round_count, "for the player.")
        else:
            print("-----------------\n", "Round", round_count, "for the computer.")
        dice_roll(score)
        print("Your current score is: ", sum(score), "\n",
        "Your roll was: ", roll, "\n",
        "Dice in the mud pit: ", mud_pit, "\n",
        "Number of dice to re-roll: ", dice_number)
        round_count += 1        #after each round, this number goes up.
        roll.clear()            #clear so it doesn't up all roles from past rounds together.
        user_response = False   #and return False so it keeps asking for input before next round
    if sum(score) >= 200:
        if turn == 1:
            print("You've won!")
        else:
            print("The computer won.")
        return True # Indicates the game is over
    if dice_number == 0:
        mud_pit, dice_number, round_count = 0, 5, 1 # end turn by resetting mudpit for next turn + dice_number.
        if turn == 1:
            turn = 0 # switch to computer
        else:
            turn = 1 # switch to player

while running:

    print("Welcome to mud pit. The rules of the game are simple. \n"
            "Roll 5 x 6 sided dice and add up their value. The first to get a score of 200 wins. \n"
            "Rolling a 5 or a 2 will send the die to the mud pit and eliminate it from a re-roll. \n"
            "You re-roll any dice remaining and follow the same rules -- add up the rolled value & 2 or 5 = mud pit. \n"
            "Your turn ends when you have no more dice to roll. Then the turns switch. \n")

    choice = input("Choose who will go first: player/computer?").lower()
    if choice == "player":
        turn = 1
    elif choice == "computer":
        turn = 0

    while sum(player_score) < 200 or sum(computer_score) < 200:
        if turn == 1:
            endGame = doDiceRolls(player_score)
        if turn == 0:
            endGame = doDiceRolls(computer_score)
        if endGame:
            break

    play_again = input("Play again? Y/N: ").upper()
    if play_again != "Y":
        print("Thanks for playing! Goodbye.")
        running = False
    else:
        # Reset the game before playing again
        player_score = [] # Restart player score
        computer_score = [] # Restart computer score
        mud_pit, dice_number, round_count = 0, 5, 1 # Reset the mudpit
