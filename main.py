import pandas as pd


def value_iteration(states: list[str],
                    transition_probabilities: dict[str, dict],
                    gamma: float,
                    iterations: int) -> tuple[dict, dict]:
    """
    Perform value iteration for a given set of states and transition probabilities.

    :param states: list of states in the MDP
    :param transition_probabilities: nested dictionary representing transition probabilities and rewards.
    :param gamma: discount factor.
    :param iterations: number of iterations to perform.
    :return: a tuple containing the value history for each state-action pair and state, and the optimal policy.
    """
    value_function = [{"S1": 0, "S2": 0, "S3": 0} for _ in range(iterations + 1)]
    value_history = {("S1", "a1"): [0],
                     ("S1", "a2"): [0],
                     ("S2", "a3"): [0],
                     "S3": [0]}
    optimal_policy = {}

    for i in range(1, iterations + 1):
        for state in transition_probabilities:
            state_values = []

            for action in transition_probabilities[state]:
                action_value = 0

                for next_state, probability, reward in transition_probabilities[state][action]:
                    action_value += probability * (reward + gamma * value_function[i - 1][next_state])

                state_values.append((action_value, action))
                value_history[(state, action)].append(action_value)

            max_value, best_action = max(state_values, key=lambda x: x[0])

            value_function[i][state] = max_value
            optimal_policy[state] = best_action

        for state in states:
            if state not in transition_probabilities:
                value_history[state].append(0)

            elif state not in value_history:
                for action in transition_probabilities[state]:
                    if (state, action) not in value_history:
                        value_history[(state, action)] = [0] * (i + 1)

    return value_history, optimal_policy


def display_value_history(value_history: dict[str | tuple, list[float]],
                          title: str) -> None:
    """
    Print the value history in a tabular format using pandas.

    :param value_history: dictionary containing the value history for each state-action pair and state.
    :param title: title for the table.
    :return: None
    """
    df = pd.DataFrame(value_history)
    df.index.name = "i"
    df.columns = [f'{key[0]} {key[1]}' if isinstance(key, tuple) else key for key in df.columns]

    print(f"\n{title}")
    print(df.T)


def display_optimal_policy(optimal_policy: dict[str, str], title: str) -> None:
    """
    Print the optimal policy.

    :param optimal_policy: dictionary containing the optimal action for each state.
    :param title: title for the policy.
    :return: None
    """
    print(f"\n{title}")
    for state, action in optimal_policy.items():
        print(f"Optimal action for state {state}: {action}")


if __name__ == "__main__":
    iterations = 4
    states = ["S1", "S2", "S3"]

    transition_probs = {"S1": {"a1": [("S1", 0.001, 100), ("S3", 0.999, 100)],
                               "a2": [("S1", 0.001, 90), ("S2", 0.999, 90)]},
                        "S2": {"a3": [("S3", 0.999, 11), ("S1", 0.001, 11)]}}

    val_his_no_dis, optimal_policy_no_dis = value_iteration(states=states,
                                                            transition_probabilities=transition_probs,
                                                            gamma=1,
                                                            iterations=iterations)

    val_his_with_dis, optimal_policy_dis = value_iteration(states=states,
                                                           transition_probabilities=transition_probs,
                                                           gamma=0.9,
                                                           iterations=iterations)

    display_value_history(value_history=val_his_no_dis,
                          title="\033[1;34m" + "Without Discount Factor: " + "\033[0m")

    display_optimal_policy(optimal_policy=optimal_policy_no_dis,
                           title="\033[1;32m" + "Optimal Policy: " + "\033[0m")

    print("\n" + "\033[1;31m" + 50 * "-" + "\033[1;34m")

    display_value_history(value_history=val_his_with_dis,
                          title="\033[1;34m" + "With Discount Factor = 0.9: " + "\033[0m")

    display_optimal_policy(optimal_policy=optimal_policy_dis,
                           title="\033[1;32m" + "Optimal Policy: " + "\033[0m")
