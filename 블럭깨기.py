#블럭깨기
import random
import time

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def initialize_board(rows, cols):
    return [["O" for _ in range(cols)] for _ in range(rows)]

def place_blocks(board, num_blocks):
    for _ in range(num_blocks):
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - 1)
        board[row][col] = "X"

def break_block(board, row, col):
    if board[row][col] == "X":
        board[row][col] = "O"
        print("Block broken!")
    else:
        print("No block to break.")

def play_game(rows, cols, num_blocks, fps):
    board = initialize_board(rows, cols)
    place_blocks(board, num_blocks)

    while True:
        print_board(board)
        print("Enter row and column to break block (e.g., 1 2), or 'q' to quit:")
        user_input = input()

        if user_input.lower() == 'q':
            print("Quitting the game. Bye!")
            break

        try:
            row, col = map(int, user_input.split())
            break_block(board, row, col)
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as space-separated integers.")

        time.sleep(1 / fps)  # 입력 대기 시간을 조절하여 FPS 조절

if __name__ == "__main__":
    rows = 5
    cols = 5
    num_blocks = 5
    fps = 1  # 1초에 한 번 반응하도록 설정

    play_game(rows, cols, num_blocks, fps)
