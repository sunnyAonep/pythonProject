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
    return False
def make_move(table, row, col, player):
    table[row][col] = player
def 

    
