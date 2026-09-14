import pytest

from value_iterator import value_iterator, DISCOUNT_FACTOR, THETA
from mdp import get_transitions, STATES, ACTIONS

def test_all_states_appear_in_value_dict():
    value = value_iterator()
    assert set(STATES).issubset(list(value.keys()))

def test_all_values_are_numbers():
    vals = value_iterator()
    assert all(isinstance(value, float) or isinstance(value, int) for value in vals.values())

def test_value_iteration_result_converges_to_bellman():
    value = value_iterator()
    new_value = {}
    for state in STATES:
        quality = {}
        for action in ACTIONS:
            quality[action] = 0
            for transition in get_transitions(state, action):
                quality[action] += transition[0] * (transition[2] + DISCOUNT_FACTOR * value[transition[1]])
        new_value[state] = max(quality.values())

    assert value == pytest.approx(new_value, abs=THETA)