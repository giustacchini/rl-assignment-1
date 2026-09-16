from value_iterator import (
    ACTIONS,
    STATES,
    DISCOUNT_FACTOR,
    get_transitions,
    extract_policy,
    value_iterator,
)

def test_policy_contains_all_states():
    values = value_iterator()
    policy = extract_policy(values)

    assert set(policy) == set(STATES)

def test_policy_actions_are_valid():
    values = value_iterator()
    policy = extract_policy(values)

    assert all(action in ACTIONS for action in policy.values())

def test_policy_selects_best_action():
    values = value_iterator()
    policy = extract_policy(values)

    for state in STATES:
        action_values = {}

        for action in ACTIONS:
            action_values[action] = sum(
                probability * (
                    reward + DISCOUNT_FACTOR * values[next_state]
                )
                for probability, next_state, reward
                in get_transitions(state, action)
            )

        assert policy[state] == max(
            action_values,
            key=action_values.get
        )