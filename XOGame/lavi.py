# לוח המשחק
table = {1: [1,2,3], 2: [4,5,6], 3: [7,8,9]}
finish = False

while finish == False:
    player1_symbol = 'X'
    player2_symbol = 'O'
    for i in range(9):
        print(f"{table[1]}\n{table[2]}\n{table[3]}")
        player_choice = int(input("First player, choose your block (1-9): "))
        if 1 <= player_choice <= 3:
            table[1][player_choice-1] = player1_symbol
        elif 4 <= player_choice <= 6:
            table[2][player_choice-4] = player1_symbol
        else:
            table[3][player_choice-7] = player1_symbol
        print(table)
