import math
import pygame


def init_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

# Check if moves are left
def is_moves_left(board):
    return any(" " in row for row in board)

# Minimax Algorithm
def minimax(board, depth, is_max, player, ai):
    winner = check_winner(board)
    if winner == ai:
        return 1
    if winner == player:
        return -1
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = ai
                    best = max(best, minimax(board, depth + 1, False, player, ai))
                    board[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = player
                    best = min(best, minimax(board, depth + 1, True, player, ai))
                    board[i][j] = " "
        return best

# Find best move for AI
def find_best_move(board, ai, player):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = ai
                move_val = minimax(board, 0, False, player, ai)
                board[i][j] = " "
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

# Draw game board
def draw_board(screen, board, font, size):
    screen.fill((255, 255, 255))
    for i in range(1, 3):
        pygame.draw.line(screen, (0, 0, 0), (i * size // 3, 0), (i * size // 3, size), 3)
        pygame.draw.line(screen, (0, 0, 0), (0, i * size // 3), (size, i * size // 3), 3)

    for i in range(3):
        for j in range(3):
            if board[i][j] != " ":
                text = font.render(board[i][j], True, (0, 0, 0))
                screen.blit(text, (j * size // 3 + 30, i * size // 3 + 20))
    
    pygame.display.flip()

# Main game function
def tic_tac_toe():
    pygame.init()
    size = 300
    screen = pygame.display.set_mode((size, size))
    pygame.display.set_caption("Tic-Tac-Toe")
    font = pygame.font.Font(None, 80)

    board = init_board()
    player = input("Choose X or O: ").upper()
    if player not in ["X", "O"]:
        print("Invalid choice, defaulting to X.")
        player = "X"
    ai = "O" if player == "X" else "X"
    turn = "X"

    running = True
    draw_board(screen, board, font, size)  # Ensure the board appears initially

    while running:
        # Display board
        draw_board(screen, board, font, size)

        # Check if the game has ended
        winner = check_winner(board)
        if winner or not is_moves_left(board):
            print(f"{winner} wins!" if winner else "It's a draw!")
            pygame.time.wait(2000)
            running = False
            break

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and turn == player:
                x, y = event.pos
                row, col = y // (size // 3), x // (size // 3)
                if board[row][col] == " ":
                    board[row][col] = player
                    turn = ai  # Change turn to AI
        
        # AI Move
        if turn == ai and is_moves_left(board):
            pygame.time.wait(500)  # Small delay for AI move
            ai_move = find_best_move(board, ai, player)
            board[ai_move[0]][ai_move[1]] = ai
            turn = player  # Change turn back to player

    pygame.quit()
import math
import pygame
import random

def init_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

# Check if moves are left
def is_moves_left(board):
    return any(" " in row for row in board)

# Minimax Algorithm
def minimax(board, depth, is_max, player, ai):
    winner = check_winner(board)
    if winner == ai:
        return 1
    if winner == player:
        return -1
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = ai
                    best = max(best, minimax(board, depth + 1, False, player, ai))
                    board[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = player
                    best = min(best, minimax(board, depth + 1, True, player, ai))
                    board[i][j] = " "
        return best

# Find best move for AI
def find_best_move(board, ai, player):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = ai
                move_val = minimax(board, 0, False, player, ai)
                board[i][j] = " "
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

# Draw game board
def draw_board(screen, board, font, size):
    screen.fill((255, 255, 255))
    for i in range(1, 3):
        pygame.draw.line(screen, (0, 0, 0), (i * size // 3, 0), (i * size // 3, size), 3)
        pygame.draw.line(screen, (0, 0, 0), (0, i * size // 3), (size, i * size // 3), 3)

    for i in range(3):
        for j in range(3):
            if board[i][j] != " ":
                text = font.render(board[i][j], True, (0, 0, 0))
                screen.blit(text, (j * size // 3 + 30, i * size // 3 + 20))
    
    pygame.display.flip()

# Main game function
def tic_tac_toe():
    pygame.init()
    size = 300
    screen = pygame.display.set_mode((size, size))
    pygame.display.set_caption("Tic-Tac-Toe")
    font = pygame.font.Font(None, 80)

    board = init_board()
    player = input("Choose X or O: ").upper()
    if player not in ["X", "O"]:
        print("Invalid choice, defaulting to X.")
        player = "X"
    ai = "O" if player == "X" else "X"
    turn = "X"

    running = True
    draw_board(screen, board, font, size)  # Ensure the board appears initially

    while running:
        # Display board
        draw_board(screen, board, font, size)

        # Check if the game has ended
        winner = check_winner(board)
        if winner or not is_moves_left(board):
            print(f"{winner} wins!" if winner else "It's a draw!")
            pygame.time.wait(2000)
            running = False
            break

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and turn == player:
                x, y = event.pos
                row, col = y // (size // 3), x // (size // 3)
                if board[row][col] == " ":
                    board[row][col] = player
                    turn = ai  # Change turn to AI
        
        # AI Move
        if turn == ai and is_moves_left(board):
            pygame.time.wait(500)  # Small delay for AI move
            ai_move = find_best_move(board, ai, player)
            board[ai_move[0]][ai_move[1]] = ai
            turn = player  # Change turn back to player

    pygame.quit()

def main():
    while True:
        tic_tac_toe()
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

if __name__ == "__main__":
    main()
tic_tac_toe()