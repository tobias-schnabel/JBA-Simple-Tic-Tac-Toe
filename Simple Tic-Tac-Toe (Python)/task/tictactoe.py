def print_grid(grid):
    print("---------")
    for row in grid:
        print("|", " ".join(row), "|")
    print("---------")

def is_valid_move(grid, move):
    if not all(coord.isdigit() for coord in move):
        print("You should enter numbers!")
        return False
    x, y = map(int, move)
    if not all(1 <= coord <= 3 for coord in (x, y)):
        print("Coordinates should be from 1 to 3!")
        return False
    if grid[x - 1][y - 1] != '_':
        print("This cell is occupied! Choose another one!")
        return False
    return True

def make_move(grid, move, player):
    x, y = map(int, move)
    grid[x - 1][y - 1] = player

def check_win(player, grid):
    # Check rows and columns
    for i in range(3):
        if all(grid[i][j] == player for j in range(3)) or all(grid[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] == player or grid[0][2] == grid[1][1] == grid[2][0] == player:
        return True

    return False


def check_game_state(grid):
    if check_win('X', grid):
        return "X wins"
    if check_win('O', grid):
        return "O wins"
    if all(cell != '_' for row in grid for cell in row):
        return "Draw"
    return "Game not finished"

# Main Program
grid = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
current_player = 'X'
print_grid(grid)

while True:
    move = input("Enter the coordinates: ").split()
    if is_valid_move(grid, move):
        make_move(grid, move, current_player)
        print_grid(grid)
        state = check_game_state(grid)
        if state != "Game not finished":
            print(state)
            break
        current_player = 'O' if current_player == 'X' else 'X'
