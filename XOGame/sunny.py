table = {1: [1,2,3], 2: [4,5,6], 3: [7,8,9]}
finish = False
player = "X"  

# Check rows
if(table[1][0] == table[1][1] == table[1][2] != " "):
    print(f"Player {player} wins!")
    finish = True
elif(table[2][0] == table[2][1] == table[2][2] != " "):
    print(f"Player {player} wins!")
    finish = True
elif(table[3][0] == table[3][1] == table[3][2] != " "):
    print(f"Player {player} wins!")
    finish = True
#columns
elif(table[1][0] == table[2][0] == table[3][0] != " "):
    print(f"Player {player} wins!")
    finish = True
elif(table[1][1] == table[2][1] == table[3][1] != " "):
    print(f"Player {player} wins!")
    finish = True
elif(table[1][2] == table[2][2] == table[3][2] != " "):
    print(f"Player {player} wins!")
    finish = True
#diagonals
elif(table[1][0] == table[2][1] == table[3][2] != " "):
    print(f"Player {player} wins!")
    finish = True
elif(table[1][2] == table[2][1] == table[3][0] != " "):
    print(f"Player {player} wins!")
    finish = True



#another version

def check_winner(table, player):
    winning_lines = [
        # rows
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        ((3, 0), (3, 1), (3, 2)),
        # columns
        ((1, 0), (2, 0), (3, 0)),
        ((1, 1), (2, 1), (3, 1)),
        ((1, 2), (2, 2), (3, 2)),
        # diagonals
        ((1, 0), (2, 1), (3, 2)),
        ((1, 2), (2, 1), (3, 0)),
    ]

    for line in winning_lines:
        (r1, c1), (r2, c2), (r3, c3) = line
        v1 = table[r1][c1]
        v2 = table[r2][c2]
        v3 = table[r3][c3]

        if v1 == v2 == v3 != " ":
            print(f"Player {player} wins!")
            return True

    return False

table = {1: ["_", "_", "_"],
         2: ["_", "_", "_"],
         3: ["_", "_", "_"]}

player = "X"
finish = False

if check_winner(table, player):
    finish = True


finish = False




for r in range(1, 4): 
    if table[r][0] == table[r][1] == table[r][2] != " ":
        print(f"Player {player} wins!")
        finish = True
        break
 
if not finish:
    for c in range(3):  
        if table[1][c] == table[2][c] == table[3][c] != " ":
            print(f"Player {player} wins!")
            finish = True
            break

if not finish:
    if table[1][0] == table[2][1] == table[3][2] != " ":
        print(f"Player {player} wins!")
        finish = True
    elif table[1][2] == table[2][1] == table[3][0] != " ":
        print(f"Player {player} wins!")
        finish = True