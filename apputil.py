import numpy as np
from IPython.display import clear_output
import time
import seaborn as sns
import matplotlib.pyplot as plt


def update_board(current_board):
    # Get board dimensions
    rows, cols = current_board.shape
    updated_board = np.zeros_like(current_board)
    
    # For each cell in the board
    for i in range(rows):
        for j in range(cols):
            # Count live neighbors
            neighbor_count = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:  # Skip the cell itself
                        continue
                    ni = i + di
                    nj = j + dj
                    # Only count neighbors within board bounds (no wrapping)
                    if 0 <= ni < rows and 0 <= nj < cols:
                        neighbor_count += current_board[ni, nj]
            
            # Apply Conway's Game of Life rules
            if current_board[i, j] == 1:  # Cell is alive
                if neighbor_count in [2, 3]:
                    updated_board[i, j] = 1  # Survives
                else:
                    updated_board[i, j] = 0  # Dies
            else:  # Cell is dead
                if neighbor_count == 3:
                    updated_board[i, j] = 1  # Becomes alive
                else:
                    updated_board[i, j] = 0  # Stays dead
    
    return updated_board




def show_game(game_board, n_steps=10, pause=0.5):
    """
    Show `n_steps` of Conway's Game of Life, given the `update_board` function.

    Parameters
    ----------
    game_board : numpy.ndarray
        A binary array representing the initial starting conditions for Conway's Game of Life. In this array, ` represents a "living" cell and 0 represents a "dead" cell.
    n_steps : int, optional
        Number of game steps to run through, by default 10
    pause : float, optional
        Number of seconds to wait between steps, by default 0.5
    """
    for step in range(n_steps):
        clear_output(wait=True)

        # update board
        game_board = update_board(game_board)

        # show board
        sns.heatmap(game_board, cmap='tab20c_r', 
                    cbar=False, square=True, linewidths=1)
        plt.title(f'Board State at Step {step + 1}')
        plt.show()

        # wait for the next step
        if step + 1 < n_steps:
            time.sleep(pause)