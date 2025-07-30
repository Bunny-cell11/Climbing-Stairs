def climbStairs(n: int) -> int:
    """
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Args:
        n: An integer representing the number of steps.

    Returns:
        An integer representing the number of distinct ways to climb to the top.
    """
    if n <= 2:
        return n

    # dp[i] will store the number of ways to climb to the i-th step
    dp = [0] * (n + 1)

    # Base cases
    dp[1] = 1  # One way to climb to the first step (1)
    dp[2] = 2  # Two ways to climb to the second step (1+1, 2)

    # Iterate from the 3rd step up to n
    for i in range(3, n + 1):
        # To reach the i-th step, you can either come from the (i-1)-th step (taking 1 step)
        # or from the (i-2)-th step (taking 2 steps).
        # The total number of ways to reach the i-th step is the sum of the ways to reach these two previous steps.
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# Example Usage:
n1 = 2
result1 = climbStairs(n1)
print(f"Number of ways to climb {n1} stairs: {result1}")  # Output: 2

n2 = 3
result2 = climbStairs(n2)
print(f"Number of ways to climb {n2} stairs: {result2}")  # Output: 3

n3 = 10
result3 = climbStairs(n3)
print(f"Number of ways to climb {n3} stairs: {result3}") # Output: 89
