# Tic-Tac-Toe
Tic-Tac-Toe: Create a two-player Tic-Tac-Toe game where players take turns marking spaces on a 3x3 grid.

# FastAPI Tic-Tac-Toe Game

Welcome to the FastAPI Tic-Tac-Toe game! This project demonstrates a simple implementation of the classic Tic-Tac-Toe game using the FastAPI framework.

## How to Run

1. Clone this repository to your local machine.

2. Install the required dependencies using the following command:

pip install -r requirements.txt
3. Run the FastAPI application using Uvicorn:

uvicorn main:app --reload

4. Open a web browser and navigate to `http://localhost:8000` to access the Tic-Tac-Toe game.

## Usage

1. Access the game's welcome message by visiting the root URL: `http://localhost:8000/`.

2. Make moves in the game by making POST requests to the move endpoint: `http://localhost:8000/move/{row}/{col}`.
- Replace `{row}` and `{col}` with the desired row and column indices (0-2) for your move.

3. The game will respond with messages indicating the result of the move, including win or draw conditions.

4. Continue making moves until the game ends.

## Dependencies

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast, web framework for building APIs with Python.
- [Uvicorn](https://www.uvicorn.org/): An ASGI server that serves FastAPI applications.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to customize and extend the game as you like. Have fun playing and coding!



