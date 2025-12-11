import random

def check_row(table):
    for r in range(1, 4):
        if table[r][0] == table[r][1] == table[r][2] != "___":
            return True
    return False


def check_col(table):
    for c in range(3):
        if table[1][c] == table[2][c] == table[3][c] != "___":
            return True
    return False


def check_dig(table):
    if table[1][0] == table[2][1] == table[3][2] != "___":
        return True
    if table[1][2] == table[2][1] == table[3][0] != "___":
        return True
    return False

def check_winner(table, player):
    if check_row(table) or check_col(table) or check_dig(table):
        print(f"Player {player} wins!")
        return True
    return False
    
def is_valid_move(table, row, col):
    if row in table and 0 <= col < len(table[row]):
        if table[row][col] == "___":
            return True
    return False

def avoid_same_move(choice, last_choice):
    if choice == last_choice:
        return True
    return False

def choice_to_position(choice):
    if 1 <= choice <= 3:
        return 1, choice - 1
    elif 4 <= choice <= 6:
        return 2, choice - 4
    else:
        return 3, choice - 7

def display_board(table):
    print(f"{table[1]}\n{table[2]}\n{table[3]}")

def display_instructions():
    table_look = {1: [1,2,3], 2: [4,5,6], 3: [7,8,9]}
    print(f"{table_look[1]}\n\n{table_look[2]}\n\n{table_look[3]}")

def get_player_input(player):
    while True:
        try:
            choice = int(input(f"{player}, choose your block (1-9): "))
            if 1 <= choice <= 9:
                return choice
            else:
                print("Please enter a number between 1 - 9: ")
        except ValueError:
            print("Please enter a number between 1 - 9: ")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def make_move(table, choice, player, last_choice):
    row, col = choice_to_position(choice)
    
    if not is_valid_move(table, row, col):
        print("This spot is already taken, choose another.")
        return False
    
    if avoid_same_move(choice, last_choice):
        print("You already chose this spot last turn, choose another.")
        return False
    
    table[row][col] = player
    return True

def get_current_player(counter, vs_pc):
    if vs_pc:
        return ' X '
    else:
        return ' X ' if counter % 2 == 0 else ' O '

def random_choice(table):
    player = ' O '
    attempts = 0
    max_attempts = 100
    
    while attempts < max_attempts:
        pc_choice = random.randint(1, 9)
        row, col = choice_to_position(pc_choice)
        
        if is_valid_move(table, row, col):
            print(f"The pc choose {pc_choice}")
            table[row][col] = player
            return pc_choice
        
        attempts += 1
    
    return None

def initialize_game():
    table = {1: ["___", "___", "___"], 2: ["___", "___", "___"], 3: ["___", "___", "___"]}
    return table

def main_game_loop(vs_pc):
    table = initialize_game()
    finish = False
    counter = 0
    last_choice = None
    
    if vs_pc:
        print("You play against the PC\nThis is how to choose a spot:")
    else:
        print("You play against another player\nThis is how to choose a spot:")
    display_instructions()
    
    while counter < 9 and not finish:
        player = get_current_player(counter, vs_pc)
        
        display_board(table)
        print("Last choice:", last_choice)
        
        player_choice = get_player_input(player)
        
        if not make_move(table, player_choice, player, last_choice):
            continue
        
        last_choice = player_choice
        counter += 1
        
        if check_winner(table, player):
            finish = True
            display_board(table)
            break
        
        if vs_pc and counter < 9 and not finish:
            pc_choice = random_choice(table)
            
            if pc_choice is not None:
                last_choice = pc_choice
                counter += 1
                
                if check_winner(table, ' O '):
                    finish = True
                    display_board(table)
                    break
    
    if not finish:
        print("Draw")
        display_board(table)

if __name__ == "__main__":
    play_pc = input("Do you want to play versus the pc (y,n): ")
    vs_pc = play_pc.lower() == 'y'
    main_game_loop(vs_pc)
