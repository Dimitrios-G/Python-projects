# SOS Game in Python

This is a simple two-player SOS game implemented in Python. Players take turns placing 'S' or 'O' on a 10x10 board, trying to create the sequence "SOS" horizontally, vertically, or diagonally.

## How to Play

1.  **Clone the repository** (if you have one) or save the Python code (`.py` file) to your local machine.
2.  **Run the script** from your terminal using the Python interpreter:
    ```bash
    python your_script_name.py
    ```
    (Replace `your_script_name.py` with the actual name of your Python file).
3.  The game will prompt Player 1 to enter their name and choose a letter ('S' or 'O').
4.  Player 2's letter will be the opposite of Player 1's choice. Player 2 will then enter their name.
5.  The initial game board will be displayed with 'S' in the four corners and "SOS" in the center.
6.  Players will take turns entering the row and column number (separated by a space) where they want to place their letter. Rows and columns are numbered starting from 0.
7.  After each move, the board is updated and displayed.
8.  If a player creates one or more "SOS" sequences with their move, they score a point.
9.  The game continues until the board is full.
10. The player with the most "SOS" sequences at the end of the game is declared the winner, and a trophy and heart graphic will be displayed.

## Features

* Two-player gameplay.
* Clear display of the game board with row and column numbers.
* Input validation for player names and moves.
* Automatic assignment of the second player's letter.
* Detection of "SOS" sequences (horizontal, vertical, and diagonal).
* Score tracking for each player.
* Game end detection when the board is full.
* Display of a winner and loser with simple ASCII art.
* Pre-filled board with 'S' in the corners and "SOS" in the center for a slightly different starting configuration.

## How to Contribute

If you'd like to contribute to this project, feel free to:

* Fork the repository.
* Create a new branch with your improvements.
* Submit a pull request.

## License

[You can add a license here if you have one, e.g., MIT License]

## Acknowledgements

[You can add any acknowledgements here, e.g., if you used any libraries or resources]
