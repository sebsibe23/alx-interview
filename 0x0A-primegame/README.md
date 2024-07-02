# 0x0A. Prime Game

## Algorithm | Python

### Project Overview

This project involves solving a competitive game scenario using concepts from prime numbers, game theory, and algorithm optimization. The challenge is to determine the winner of a game where players take turns removing prime numbers and their multiples from a set of consecutive integers.

### Project Timeline
- **Project Start:** Jul 1, 2024, 6:00 AM
- **Project End:** Jul 5, 2024, 6:00 AM
- **Checker Release:** Jul 2, 2024, 6:00 AM
- **Auto Review:** At the deadline

### Concepts Needed

#### Prime Numbers
- Understanding prime numbers and efficient algorithms for identifying them.
- Efficient algorithms for identifying prime numbers within a range.

#### Sieve of Eratosthenes
- An efficient algorithm for finding all prime numbers up to any given limit, which is useful for this task.

#### Game Theory
- Basic principles of competitive games where players take turns.
- Understanding win conditions and strategies for optimal play.

#### Dynamic Programming/Memoization
- Using previous results to make future calculations faster, potentially necessary for optimizing the solution for multiple rounds of the game.

#### Python Programming
- Loops and conditional statements for implementing game logic and algorithms.
- Arrays and lists for storing integers and tracking removed numbers.

### Resources

#### Prime Numbers and Sieve of Eratosthenes
- **Khan Academy:** Introduction to prime numbers.
- **Sieve of Eratosthenes in Python:** Step-by-step guide to implementing the sieve algorithm in Python.

#### Game Theory Basics
- **Game Theory Introduction:** Simple explanation of game theory and strategic decision-making.

#### Dynamic Programming
- **What Is Dynamic Programming With Python Examples:** Introduction to dynamic programming with Python examples.

#### Python Official Documentation
- **Python Lists:** Managing lists in Python, useful for tracking the game state.

### Requirements

#### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should use the PEP 8 style (version 1.7.x)
- All files must be executable

### Tasks

#### 0. Prime Game (Mandatory)
Maria and Ben are playing a game with the following rules:
- Given a set of consecutive integers starting from 1 up to and including `n`, they take turns choosing a prime number from the set and removing that number and its multiples.
- The player who cannot make a move loses the game.
- They play `x` rounds, with `n` varying for each round. Maria always goes first and both players play optimally.

**Prototype:** `def isWinner(x, nums)`

- `x`: Number of rounds.
- `nums`: Array of `n` values for each round.

**Return:** Name of the player who won the most rounds. If the winner cannot be determined, return `None`.

- Assume `n` and `x` will not be larger than 10000.
- Do not import any packages for this task.

**Example:**

```python
x = 3
nums = [4, 5, 1]

# First round: n = 4
# Maria picks 2 and removes 2, 4 (leaving 1, 3)
# Ben picks 3 and removes 3 (leaving 1)
# Ben wins (no prime numbers left for Maria)

# Second round: n = 5
# Maria picks 2 and removes 2, 4 (leaving 1, 3, 5)
# Ben picks 3 and removes 3 (leaving 1, 5)
# Maria picks 5 and removes 5 (leaving 1)
# Maria wins (no prime numbers left for Ben)

# Third round: n = 1
# Ben wins (no prime numbers for Maria to choose)

# Result: Ben has the most wins

print(isWinner(5, [2, 5, 1, 4, 3]))  # Output: Winner: Ben
```

### Example Usage

Create a file `main_0.py`:

```python
#!/usr/bin/python3
isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
```

Execute the script:

```shell
carrie@ubuntu:~/0x0A-primegame$ ./main_0.py
Winner: Ben
```

### Repository

- **GitHub repository:** `alx-interview`
- **Directory:** `0x0A-primegame`
- **File:** `0-prime_game.py`
