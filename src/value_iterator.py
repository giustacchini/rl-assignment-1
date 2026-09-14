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

def main():
    value = value_iterator()

if __name__ == "__main__":
    main()