from src.mdp import (
    GRID_ROWS,
    GRID_COLS,
    START_STATE,
    GOAL_STATE,
    OBSTACLES,
    move,
)

def print_grid(agent_state):
    """Display the GridWorld with the agent's current position."""
    
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            state = (row, col)

            if state == agent_state:
                symbol = "A"
            elif state == START_STATE:
                symbol = "S"
            elif state == GOAL_STATE:
                symbol = "G"
            elif state in OBSTACLES:
                symbol = "X"
            else:
                symbol = "."

            print(symbol, end="  ")

        print()

if __name__ == "__main__":
    agent_state = START_STATE

    print("Before:")
    print_grid(agent_state)

    agent_state = move(agent_state, "up")

    print("\nAfter action: up")
    print_grid(agent_state)