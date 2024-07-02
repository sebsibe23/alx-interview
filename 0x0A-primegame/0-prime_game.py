#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.

    Args:
        x (int): The number of rounds in the game.
        nums (list): List of integers where each integer represents the
                     upper limit of numbers to consider for primes in
                     each round.

    Returns:
        str: The name of the player with the most wins ('Maria' or 'Ben').
             Returns None if there is a tie or invalid input.
    """
    try:
        if x < 1 or not nums:
            return None
        marias_wins, bens_wins = 0, 0

        # Generate primes up to the maximum number in nums
        n = max(nums)
        primes = [True for _ in range(1, n + 1)]
        primes[0] = False  # 1 is not a prime number

        for i, is_prime in enumerate(primes, 1):
            if i == 1 or not is_prime:
                continue
            for j in range(i + i, n + 1, i):
                primes[j - 1] = False

        # Count the primes for each round in nums
        for _, n in zip(range(x), nums):
            primes_count = len(list(filter(lambda x: x, primes[0: n])))
            bens_wins += primes_count % 2 == 0
            marias_wins += primes_count % 2 == 1

        if marias_wins == bens_wins:
            return None
        return 'Maria' if marias_wins > bens_wins else 'Ben'

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
