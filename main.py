class MDP:
    """
    TODO: Docstring for MDP
    """

    def __init__(self,
                 states: list[str],
                 actions: list[str],
                 transitions: dict[str, dict[str, list[tuple[str, float]]]],
                 rewards: dict[str, dict[str, float]],
                 discount_factor: float = 1.0) -> None:
        """
        Initialize the MDP.

        :param states: list of states in the MDP.
        :param actions: list of actions in the MDP.
        :param transitions: dictionary representing state transition probabilities.
                            transitions[state][action] -> list of (next_state, probability) tuples.
        :param rewards: dictionary representing rewards for state-action pairs.
                        rewards[state][action] -> reward value.
        :param discount_factor: discount factor for future rewards.

        :return: None
        """
        self.states = states
        self.actions = actions
        self.transitions = transitions
        self.rewards = rewards
        self.discount_factor = discount_factor
        self.values = {state: 0.0 for state in states}
        self.policy = {state: actions[0] for state in states}

    def value_iteration(self,
                        epsilon: float = 0.01) -> None:
        """
        Perform value iteration to find the optimal policy.

        :param epsilon: convergence threshold.
        :return: None
        """
        while True:
            delta = 0
            for state in self.states:
                v = self.values[state]
                self.values[state] = max(self.compute_q_value(state, action) for action in self.actions)
                delta = max(delta, abs(v - self.values[state]))
            if delta < epsilon:
                break
        self.extract_policy()

    def compute_q_value(self,
                        state: str,
                        action: str) -> float:
        """
        Compute the Q-value for a state-action pair.

        :param state: the current state.
        :param action: the action taken from the current state.
        :return: the Q-value.
        """
        return self.rewards[state][action] + self.discount_factor * sum(
            prob * self.values[next_state] for next_state, prob in self.transitions[state][action])

    def extract_policy(self) -> None:
        """
        Extract the optimal policy based on the current value function.

        :return: None
        """
        for state in self.states:
            self.policy[state] = max(self.actions,
                                     key=lambda action: self.compute_q_value(state=state, action=action))

    def print_policy(self) -> None:
        """
        Print the optimal policy.

        :return: None
        """
        for state in self.policy:
            print(f"Optimal action for state {state}: {self.policy[state]}")


if __name__ == "__main__":
    states = ["S0", "S1", "S2"]
    actions = ["A0", "A1"]

    transitions = {"S0": {"A0": [("S0", 0.5), ("S1", 0.5)],
                          "A1": [("S0", 0.7), ("S2", 0.3)]},
                   "S1": {"A0": [("S0", 1.0)],
                          "A1": [("S1", 0.5), ("S2", 0.5)]},
                   "S2": {"A0": [("S0", 0.4), ("S2", 0.6)],
                          "A1": [("S1", 1.0)]}}

    rewards = {"S0": {"A0": -1, "A1": -2},
               "S1": {"A0": -2, "A1": -2},
               "S2": {"A0": -1, "A1": -1}}

    mdp_no_discount = MDP(states=states,
                          actions=actions,
                          transitions=transitions,
                          rewards=rewards,
                          discount_factor=1.0)

    mdp_no_discount.value_iteration()
    print("Policy without discounting:")
    mdp_no_discount.print_policy()

    mdp_discount = MDP(states=states,
                       actions=actions,
                       transitions=transitions,
                       rewards=rewards,
                       discount_factor=0.9)

    mdp_discount.value_iteration()
    print("\nPolicy with discounting (discount factor = 0.9):")
    mdp_discount.print_policy()
