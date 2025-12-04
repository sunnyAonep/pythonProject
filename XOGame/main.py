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
for i in range(9):
    try:
        if counter % 2 == 0:
            player = 'O'
        else:
            player = 'X'
        print(f"{table[1]}\n{table[2]}\n{table[3]}")
        last_choice = 0
        print(last_choice)
        player_choice = int(input(f"{player}, choose your block (1-9): "))
        if avoid_same_move(choice=player_choice, last_choice=last_choice) == True:
            continue
        last_choice = player_choice
        counter += 1
        if 1 <= player_choice <= 3:
            table[1][player_choice-1] = player
        elif 4 <= player_choice <= 6:
            table[2][player_choice-4] = player
        else:
            table[3][player_choice-7] = player
        if check_winner(table, player):
            finish = True
            print(f"{table[1]}\n{table[2]}\n{table[3]}")
            break
    except Exception as e:
        print("Please enter a number between 1 - 9: ")
        counter -= 1
        continue
    
if finish == False: 
    print("Draw")
