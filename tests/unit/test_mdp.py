import pytest 
from mdp import move, get_reward, get_transitions

def test_move_normal_state():
    #Arrange 
    state = (2, 2)
    action = "up"

    #Act 
    result = move(state, action)

    #Assert
    assert result == (1, 2)

def test_move_outside_grid_stays_same():
    state = (0, 0)
    action = "left"

    result = move(state, action)

    assert result == (0, 0)

def test_move_into_obstacle_stays_same():
    state = (1, 0)
    action = "right"

    result = move(state, action)

    assert result == (1, 0)


def test_step_reward_is_minus_one():
    state = (2, 2)
    action = "up"

    result = get_reward(state, action)

    assert result == -1


def test_obstacle_reward_is_minus_five():
    state = (2, 2)
    action = "right"  

    result = get_reward(state, action)

    assert result == -5


def test_goal_reward_is_five():
    state = (0, 3)
    action = "right"

    result = get_reward(state, action)

    assert result == 5


def test_outside_grid_reward_is_minus_one():
    state = (0, 0)
    action = "up"

    result = get_reward(state, action)

    assert result == -1

def test_get_transitions_returns_four_transitions():
    # Arrange
    state = (2, 2)
    action = "up"

    # Act
    transitions = get_transitions(state, action)

    # Assert
    assert len(transitions) == 4


def test_transition_probabilities_sum_to_one():
    # Arrange
    state = (2, 2)
    action = "up"

    # Act
    transitions = get_transitions(state, action)
    total_probability = sum(
        probability for probability, next_state, reward in transitions
    )

    # Assert
    assert total_probability == pytest.approx(1.0)
