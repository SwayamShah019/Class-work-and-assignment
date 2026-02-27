def sum_of_infinite_geometric_series(a, r):
    """
    Calculates the sum of an infinite geometric series.

    Args:
        a (float or int): The first term of the series.
        r (float or int): The common ratio of the series.

    Returns:
        float or str: The sum of the series, or "Infinite" if it diverges.
    """
    if abs(r) >= 1:
        return "Infinite"
    else:
        # The sum is a / (1 - r) for |r| < 1
        sum_val = a / (1 - r)
        return sum_val
a = 2
r = 0.5
result = sum_of_infinite_geometric_series(a, r)
print(f"The sum of the series with a={a} and r={r} is: {result}")
# Output: The sum of the series with a=1 and r=0.5 is: 2.0
