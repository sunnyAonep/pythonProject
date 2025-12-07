import random

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

def random_choice(last_choice, table):
    can_get_out = False
    player = 'O'
    while not can_get_out:
        pc_choice = random.randint(1,9)
        
        if 1 <= pc_choice <= 3:
            row, col = 1, pc_choice - 1
        elif 4 <= pc_choice <= 6:
            row, col = 2, pc_choice - 4
        else:
            row, col = 3, pc_choice - 7

        if is_valid_move(table, row, col):
            print(f"The pc choose {pc_choice}")
            table[row][col] = player
            can_get_out = True
            return pc_choice
        
    return None
    
#main game loop:
table = {1: [" ", " ", " "], 2: [" ", " ", " "], 3: [" ", " ", " "]}
finish = False
player = 'X'
counter = 0
last_choice = None
play_pc = input("Do you want to play versus the pc (y,n): ")
if play_pc.lower() == 'y':
    print("You play against the PC\nThis is how to choose a spot:")
    table_look = {1: [1,2,3], 2: [4,5,6], 3: [7,8,9]}
    print(f"{table_look[1]}\n{table_look[2]}\n{table_look[3]}")
    while counter < 9 and not finish:
        try:
            print(f"{table[1]}\n{table[2]}\n{table[3]}")
            print("Last choice:", last_choice)

            player_choice = int(input(f"{player}, choose your block (1-9): "))

            if 1 <= player_choice <= 3:
                row, col = 1, player_choice - 1
            elif 4 <= player_choice <= 6:
                row, col = 2, player_choice - 4
            else:
                row, col = 3, player_choice - 7

            if not is_valid_move(table, row, col):
                print("This spot is already taken, choose another.")
                continue 

            if avoid_same_move(choice=player_choice, last_choice=last_choice):
                print("You already chose this spot last turn, choose another.")
                continue

            last_choice = player_choice
            counter += 1 
            table[row][col] = player

            if check_winner(table, player):
                finish = True
                print(f"{table[1]}\n{table[2]}\n{table[3]}")
                break

            if counter < 9:
                pc_last_choice = random_choice(last_choice, table) 
                
                if pc_last_choice is not None:
                    last_choice = pc_last_choice
                    counter += 1
                
                    if check_winner(table, 'O'):
                        finish = True
                        break

        except ValueError:
            print("Please enter a number between 1 - 9: ")
            continue
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            continue

    if not finish:
        print("Draw")
else:
    print("You play against another player\nThis is how to choose a spot:")
    table_look = {1: [1,2,3], 2: [4,5,6], 3: [7,8,9]}
    print(f"{table_look[1]}\n{table_look[2]}\n{table_look[3]}")
    while counter < 9 and not finish:
        try:
            if counter % 2 == 0:
                player = 'X'
            else:
                player = 'O'

            print(f"{table[1]}\n{table[2]}\n{table[3]}")
            print("Last choice:", last_choice)

            player_choice = int(input(f"{player}, choose your block (1-9): "))
            
            if 1 <= player_choice <= 3:
                row, col = 1, player_choice - 1
            elif 4 <= player_choice <= 6:
                row, col = 2, player_choice - 4
            else:
                row, col = 3, player_choice - 7

            if not is_valid_move(table, row, col):
                print("This spot is already taken, choose another.")
                continue 

            if avoid_same_move(choice=player_choice, last_choice=last_choice):
                print("You already chose this spot last turn, choose another.")
                continue

            last_choice = player_choice
            counter += 1 
            table[row][col] = player

            if check_winner(table, player):
                finish = True
                print(f"{table[1]}\n{table[2]}\n{table[3]}")
                break

        except ValueError:
            print("Please enter a number between 1 - 9: ")
            continue

    if not finish: 
        print("Draw")