from mdp import (
    GRID_ROWS,
    GRID_COLS,
    START_STATE,
    GOAL_STATE,
    OBSTACLES,
    move,
)

from value_iterator import value_iterator, extract_policy

import pygame

ORDINARY_CELL_COLOR = (77, 76, 69)
START_CELL_COLOR = (23, 217, 12)
GOAL_CELL_COLOR = (199, 0, 0)
OBSTACLE_CELL_COLOR = (255, 255, 255)

GAME_WIDTH = 500
GAME_HEIGHT = 500
CELL_WIDTH = 100
CELL_HEIGHT = 100

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

def main():
    pygame.init()

    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    arial_font = pygame.font.SysFont("DejaVu Sans", 25)

    value = value_iterator()
    policy = extract_policy(value)
    policy_sign = {}
    for state, action in policy.items():
        if action == "up":
            policy_sign[state] = "↑"
        elif action == "down":
            policy_sign[state] = "↓"
        elif action == "left":
            policy_sign[state] = "←"
        else:
            policy_sign[state] = "→"

    v_min = min(value.values())
    v_max = max(value.values())
    value_norm = {}
    for state, val in value.items():
        value_norm[state] = (val - v_min) / (v_max - v_min)


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                state = (row, col)
                if state == START_STATE:
                    pygame.draw.rect(screen, START_CELL_COLOR, (state[1] * CELL_WIDTH, state[0] * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))
                    state_surface = arial_font.render("S", True, "white")
                    text_surface = arial_font.render(str(round(value[state], 2)), True, "white")
                    policy_surface = arial_font.render(policy_sign[state], True, "white")
                    state_rect = state_surface.get_rect(center=(state[1] * CELL_WIDTH + CELL_WIDTH / 2, state[0] * CELL_HEIGHT + CELL_HEIGHT / 2))
                    text_rect = text_surface.get_rect(center=(state[1] * CELL_WIDTH + CELL_WIDTH / 2, state[0] * CELL_HEIGHT + CELL_HEIGHT / 2 + 25))
                    policy_rect = policy_surface.get_rect(center=(state[1] * CELL_WIDTH + CELL_WIDTH / 2, state[0] * CELL_HEIGHT + CELL_HEIGHT / 2 - 25))
                    screen.blit(state_surface, state_rect)
                    screen.blit(text_surface, text_rect)
                    screen.blit(policy_surface, policy_rect)
                elif state == GOAL_STATE:
                    pygame.draw.rect(screen, GOAL_CELL_COLOR, (state[1] * CELL_WIDTH, state[0] * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))
                    state_surface = arial_font.render("G", True, "white")
                    state_rect = state_surface.get_rect(center=(state[1] * CELL_WIDTH + CELL_WIDTH / 2, state[0] * CELL_HEIGHT + CELL_HEIGHT / 2))
                    screen.blit(state_surface, state_rect)
                elif state in OBSTACLES:
                    pygame.draw.rect(screen, OBSTACLE_CELL_COLOR, (state[1] * CELL_WIDTH, state[0] * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))
                    state_surface = arial_font.render("X", True, "black")
                    text_rect = state_surface.get_rect(center=(state[1] * CELL_WIDTH + CELL_WIDTH / 2, state[0] * CELL_HEIGHT + CELL_HEIGHT / 2))
                    screen.blit(state_surface, text_rect)
                else:
                    v = value_norm[state]
                    pygame.draw.rect(screen, (int(40), int(40), int(255 * v)), (state[1] * CELL_WIDTH, state[0] * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))
                    text_surface = arial_font.render(str(round(value[state], 2)), True, "white")
                    policy_surface = arial_font.render(policy_sign[state], True, "white")
                    text_rect = text_surface.get_rect(center=(state[1] * CELL_WIDTH + CELL_WIDTH / 2, state[0] * CELL_HEIGHT + CELL_HEIGHT / 2 + 25))
                    policy_rect = policy_surface.get_rect(center=(state[1] * CELL_WIDTH + CELL_WIDTH / 2, state[0] * CELL_HEIGHT + CELL_HEIGHT / 2 - 25))
                    screen.blit(text_surface, text_rect)
                    screen.blit(policy_surface, policy_rect)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    # agent_state = START_STATE

    # print("Before:")
    # print_grid(agent_state)

    # agent_state = move(agent_state, "up")

    # print("\nAfter action: up")
    # print_grid(agent_state)

    main()