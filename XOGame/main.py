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

def identify_X_or_O(xo):
   if(xo=='X' or xo=='O'):
        return True
   else:
       return False

def who_starts_first(player1, player2):
    if(player1=='X' and player2=='O'):
        return player1
    elif(player1=='O' and player2=='X'):
        return player2
    else:
        return None
    
def is_valid_move(table, row, col):
    if row in table and 0 <= col < len(table[row]):
        if table[row][col] == " ":
            return True
    else:
        return False
    
def make_move(table, row, col, player):
    table[row][col] = player

#main game loop:

while finish == False:
    player= 'X'

    for i in range(9):
        if i % 2 == 0:
            player = 'O'
        else:
            player = 'X'
        print(f"{table[1]}\n{table[2]}\n{table[3]}")
        player_choice = int(input(f"{player}, choose your block (1-9): "))
        if 1 <= player_choice <= 3:
            table[1][player_choice-1] = player
        elif 4 <= player_choice <= 6:
            table[2][player_choice-4] = player
        else:
            table[3][player_choice-7] = player
        if check_winner(table, player):
            finish = True
            break


    if finish == False: 
        print("Draw")
    break
