from mdp import get_transitions, STATES, ACTIONS

THETA = 0.001
DISCOUNT_FACTOR = 0.9

def value_iterator():
    value = {}
    for state in STATES:
        value[state] = 0
    delta = THETA
    while delta >= THETA:
        new_value = {}
        delta = 0
        for state in STATES:
            new_value[state] = 0
            v_old = value[state]
            quality = {}
            for action in ACTIONS:
                quality[action] = 0
                transitions = get_transitions(state, action)
                for transition in transitions:
                    quality[action] += transition[0] * (transition[2] + DISCOUNT_FACTOR * value[transition[1]])
            new_value[state] = max(quality.values())
            delta = max(delta, abs(new_value[state] - v_old))
        value = new_value
    return value

def extract_policy(value):
    policy = {}

    for state in STATES:
        action_values = {}

        for action in ACTIONS:
            action_value = 0

            for probability, next_state, reward in get_transitions(state, action):
                action_value += probability * (
                    reward + DISCOUNT_FACTOR * value[next_state]
                )

            action_values[action] = action_value

        # Select the action with the highest expected value.
        policy[state] = max(action_values, key=action_values.get)

    return policy

def main():
    value = value_iterator()
    policy = extract_policy(value)
    print(policy)

if __name__ == "__main__":
    main()