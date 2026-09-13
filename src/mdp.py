GRID_ROWS = 5
GRID_COLS = 5

START_STATE = (4,0)
GOAL_STATE = (0,4)

GOAL_REWARD = 5
OBSTACLE_REWARD = -5
STEP_REWARD = -1

OBSTACLES = {
    (1,1),
    (2,3),
    (3,1), 
    (3,2),
    (4,4)
}

# all states in the grid
STATES = [
    (row, col) 
    for row in range(GRID_ROWS) 
    for col in range(GRID_COLS)
    if (row, col) not in OBSTACLES
]

ACTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

TRANSITION_PROBS = {
    "up": {
        "up": 0.7,
        "down": 0.1,
        "left": 0.1,
        "right": 0.1
    },

    "down": {
        "down": 0.7,
        "up": 0.1,
        "left": 0.1,
        "right": 0.1
    },

    "left": {
        "left": 0.7,
        "right": 0.1,
        "up": 0.1,
        "down": 0.1
    },

    "right": {
        "right": 0.7,
        "left": 0.1,
        "up": 0.1,
        "down": 0.1
    }
}

def move(state, action):
    row, col = state
 
    dr, dc = ACTIONS[action]
    next_state = (row + dr, col + dc)

    # If outside the grid, stay in the same state
    if (
        next_state[0] < 0
        or next_state[0] >= GRID_ROWS
        or next_state[1] < 0
        or next_state[1] >= GRID_COLS
    ):
        return state

    # If the next cell is an obstacle, stay in the same state
    if next_state in OBSTACLES:
        return state

    return next_state

def get_reward(state, action):
    row, col = state
    dr, dc = ACTIONS[action]

    attempted_state = (row + dr, col + dc)

    # Outside grid
    if (
        attempted_state[0] < 0
        or attempted_state[0] >= GRID_ROWS
        or attempted_state[1] < 0
        or attempted_state[1] >= GRID_COLS
    ):
        return STEP_REWARD   # -1
    
    if attempted_state in OBSTACLES:
        return OBSTACLE_REWARD # -5

    if attempted_state == GOAL_STATE:
        return GOAL_REWARD # +5

    return STEP_REWARD # -1

# Possible transitions
def get_transitions(state, action):
    transitions = []

    # possible actual movements and their probabilities
    for actual_action, probability in TRANSITION_PROBS[action].items():

        next_state = move(state, actual_action)
        reward = get_reward(state, actual_action)

        transitions.append(
            (probability, next_state, reward)
        )

    return transitions


if __name__ == "__main__":
    transitions = get_transitions((2, 2), "up")

    print("[")
    for transition in transitions:
        print(" ", transition, ",")
    print("]")