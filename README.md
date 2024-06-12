# Fundamental of Artificial Intelligence - MDP Algorithm

This repository contains my `MDP algorithm` assignment for the **Fundamental of Artificial Intelligence** course
at [An-Najah National University (NNU)](https://www.najah.edu/en/#).

## Overview

This project implements the Value Iteration algorithm for **Markov Decision Processes (MDP)**. The Value Iteration
algorithm
is used to determine the optimal policy and value function for a given set of states and transition probabilities.

## Problem Description

In Artificial Intelligence, many real-world problems can be modeled as Markov Decision Processes (MDPs). An MDP is a
mathematical framework used to model decision-making problems where outcomes are partially random and partially under
the control of a decision-maker. The MDP algorithm is a solution method for determining the optimal policy, which
defines the best action to take in each state to maximize long-term rewards.

### Why MDP Algorithm?

The MDP algorithm is valuable because it provides a systematic approach to decision-making in uncertain environments. By
modeling a problem as an MDP, we can find the optimal policy that maximizes expected rewards over time. This is
particularly useful in various domains such as robotics, finance, healthcare, and more.

### How MDP Works

MDP works by iteratively updating the value function for each state-action pair based on the expected future rewards.
The algorithm calculates the value of being in a particular state and taking a particular action, considering the
immediate reward and the expected future rewards discounted by a factor called the discount factor (gamma). By repeating
this process, the algorithm converges to the optimal value function and policy.

## Features

- **Value Iteration**: Computes the value function for each state-action pair and determines the optimal policy.
- **Value History Display**: Prints the value history in a tabular format using pandas.
- **Optimal Policy Display**: Prints the optimal policy for each state.

## Getting Started

1. Clone this repository to your local machine:

```zsh
git clone git@github.com:IsmaelMousa/mdp-value-iteration.git
```

2. Navigate to the **mdp-value-iteration** directory:

```zsh
cd mdp-value-iteration
```

3. Setup virtual environment:

```zsh
python3 -m venv .venv
```

4. Activate the virtual environment:

```zsh
source .venv/bin/activate
```

5. Install the required dependencies:

```zsh
make install
```

6. Run the program:

```zsh
make run
```

### Results

```zsh
Without Discount Factor: 
i        0      1        2           3           4
S1 a1  0.0  100.0  100.100  100.101089  100.101190
S1 a2  0.0   90.0  101.089  101.189989  101.191178
S2 a3  0.0   11.0   11.100   11.101089   11.101190
S3     0.0    0.0    0.000    0.000000    0.000000

Optimal Policy: 
Optimal action for state S1: a2
Optimal action for state S2: a3

--------------------------------------------------

With Discount Factor = 0.9: 
i        0      1         2           3           4
S1 a1  0.0  100.0  100.0900  100.090081  100.090081
S1 a2  0.0   90.0   99.9801  100.061100  100.061173
S2 a3  0.0   11.0   11.0900   11.090081   11.090081
S3     0.0    0.0    0.0000    0.000000    0.000000

Optimal Policy: 
Optimal action for state S1: a1
Optimal action for state S2: a3
```

## Conclusion

In conclusion, the MDP algorithm provides a powerful framework for modeling and solving decision-making problems in
artificial intelligence. By understanding the problem description, the workings of MDP, and the output it generates, one
can effectively apply this algorithm to a wide range of real-world scenarios.