from fastapi import FastAPI, HTTPException

app = FastAPI()

# Initialize the Tic-Tac-Toe board and current player
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

def print_board(board):
    """
    Create a formatted string representation of the Tic-Tac-Toe board.

    Args:
        board (List[List[str]]): The Tic-Tac-Toe board as a 2D list.

    Returns:
        str: Formatted string representation of the board.
    """
    return "\n".join([" | ".join(row) + "\n" + "-" * 9 for row in board])

def check_win(board, player):
    """
    Check if a player has won the game.

    Args:
        board (List[List[str]]): The Tic-Tac-Toe board as a 2D list.
        player (str): The player ("X" or "O") to check for a win.

    Returns:
        bool: True if the player has won, False otherwise.
    """
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

@app.get("/")
def read_root():
    """
    Root endpoint that returns a welcome message.

    Returns:
        dict: Welcome message.
    """
    return {"message": "Welcome to Tic-Tac-Toe!"}

@app.post("/move/{row}/{col}")
def make_move(row: int, col: int):
    """
    Make a move on the Tic-Tac-Toe board.

    Args:
        row (int): The row index (0-2) for the move.
        col (int): The column index (0-2) for the move.

    Returns:
        dict: Message indicating the result of the move.
    """
    global current_player

    if not (0 <= row < 3 and 0 <= col < 3):
        raise HTTPException(status_code=400, detail="Invalid row or column.")

    if board[row][col] != " ":
        raise HTTPException(status_code=400, detail="Cell is already taken.")

    board[row][col] = current_player
    result = print_board(board)

    if check_win(board, current_player):
        return {"message": f"Player {current_player} wins!\n{result}"}

    current_player = "O" if current_player == "X" else "X"

    if all(cell != " " for row in board for cell in row):
        return {"message": f"It's a draw!\n{result}"}

    return {"message": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
