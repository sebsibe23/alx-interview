# 0x08. Making Change

## Algorithm | Python

### Project Overview

**Start Date**: June 18, 2024, 6:00 AM  
**End Date**: June 21, 2024, 6:00 AM  
**Checker Release Date**: June 19, 2024, 12:00 AM  
**Auto Review Launch**: At the deadline  

### Project Description

In the "0. Change comes from within" project, you will solve the classic coin change problem using dynamic programming and greedy algorithms. The goal is to find the minimum number of coins required to achieve a given total amount from a list of coin denominations. This project will test your understanding of algorithms and your ability to create efficient solutions.

### Key Concepts

#### Greedy Algorithms
- **Overview**: Learn how greedy algorithms work and their suitability for the coin change problem.
- **Limitations**: Understand the scenarios where greedy algorithms may not provide the optimal solution.

#### Dynamic Programming
- **Principles**: Grasp the basics of dynamic programming for solving optimization problems.
- **Key Concepts**: Understand overlapping subproblems and optimal substructure in the coin change problem.

#### Algorithmic Complexity
- **Analysis**: Analyze the time and space complexity of your algorithms.
- **Optimization**: Aim to create solutions with lower complexity to meet runtime constraints.

#### Problem-Solving Strategies
- **Decomposition**: Break down the problem into smaller, manageable sub-problems.
- **Approaches**: Compare iterative vs. recursive approaches to dynamic programming.

#### Python Programming
- **Techniques**: Manipulate lists and use list comprehensions effectively.
- **Implementation**: Implement functions with efficient looping and conditional statements.

### Resources

#### Python Official Documentation
- **More Control Flow Tools**: [Python Docs](https://docs.python.org/3/tutorial/controlflow.html)

#### GeeksforGeeks Articles
- **Coin Change | DP-7**: [GeeksforGeeks](https://www.geeksforgeeks.org/coin-change-dp-7/)
- **Greedy Algorithm to find Minimum number of Coins**: [GeeksforGeeks](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)

#### YouTube Tutorials
- **Dynamic Programming - Coin Change Problem**: Search on YouTube for step-by-step visual explanations.

### Additional Resources
- **Mock Technical Interview**

### Requirements

- **Editors**: vi, vim, emacs
- **Environment**: Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
- **File Standards**: 
  - All files should end with a new line
  - The first line of all your files should be exactly `#!/usr/bin/python3`
  - Code should follow PEP 8 style (version 1.7.x)
  - All files must be executable
- **README.md**: A README.md file at the root of the project folder is mandatory

### Task

#### 0. Change comes from within (mandatory)

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

- **Prototype**: `def makeChange(coins, total)`
- **Return**: The fewest number of coins needed to meet the total
  - If the total is 0 or less, return 0
  - If the total cannot be met by any number of coins, return -1
- **Parameters**:
  - `coins`: A list of the values of the coins in your possession
  - Each coin's value will always be an integer greater than 0
  - Assume you have an infinite number of each denomination of coin in the list

- **Evaluation**: Your solution’s runtime will be evaluated.

**Example Usage**:

```python
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))  # Output: 7

print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```

### Repository

- **GitHub Repository**: `alx-interview`
- **Directory**: `0x08-making_change`
- **File**: `0-making_change.py`
