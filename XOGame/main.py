table = {1: [1,2,3], 2: [4,5,6], 3: [7,8,9]}
finish = False

def check_row(table):
    for r in range(1, 4):
        if table[r][0] == table[r][1] == table[r][2] != " ":
            return True
    return False


def check_col(table):
    for c in range(3):
        if table[1][c] == table[2][c] == table[3][c] != " ":
            return True
    return False


def check_dig(table):
    if table[1][0] == table[2][1] == table[3][2] != " ":
        return True
    if table[1][2] == table[2][1] == table[3][0] != " ":
        return True
    return False

def check_winner(table, player):
    if check_row(table) or check_col(table) or check_dig(table):
        print(f"Player {player} wins!")
        return True
    return False
    
def is_valid_move(table, row, col):
    if row in table and 0 <= col < len(table[row]):
        if table[row][col] == " ":
            return True
    else:
        return False

def avoid_same_move(choice, last_choice):
    print(f"Choice: {choice}, Last Choice: {last_choice}")
    if choice == last_choice:
        return True
    else:
        return False

def choice_Player(player):
    if player == 'X':
        return 'X'
    else:
        return 'O'

#main game loop:

player= 'X'
counter = 0
last_choice = None 
while counter < 9 and finish == False:
    try:
        if counter % 2 == 0:
            player = 'O'
        else:
            player = 'X'

        print(f"{table[1]}\n{table[2]}\n{table[3]}")
        print("Last choice:", last_choice)

        player_choice = int(input(f"{player}, choose your block (1-9): "))

        if avoid_same_move(choice=player_choice, last_choice=last_choice):
            print("You already chose this spot last turn, choose another.")
            continue
        last_choice = player_choice

        if 1 <= player_choice <= 3:
            row, col = 1, player_choice - 1
        elif 4 <= player_choice <= 6:
            row, col = 2, player_choice - 4
        else:
            row, col = 3, player_choice - 7

        if table[row][col] == "X" or table[row][col] == "O":
            print("This spot is already taken, choose another.")
            continue 

        counter += 1 
        table[row][col] = player

        if check_winner(table, player):
            finish = True
            print(f"{table[1]}\n{table[2]}\n{table[3]}")
            break

    except Exception:
        print("Please enter a number between 1 - 9: ")
        continue

if finish == False: 
    print("Draw")