"""
Python solution for challenge: "Subarrays with an odd number of odd numbers"
To start the tests, type from CLI: python tests.py
"""


def solve(arr):
    # Count of odd sequences
    count_odd_sequences = 0
    # Sequence management (even = 0, odd = 1)
    even_odd_sequence = 0
    # Number of occurrences of the even or odd sequences
    num_even_odd_sequences = [1, 0]
    for number in arr:
        # Check if the new contiguous sequence is even (% 2 = 0) or odd (% 2 = 1)
        even_odd_sequence += number
        even_odd_sequence %= 2
        # Update the number of occurrences of the odd sequences
        count_odd_sequences += num_even_odd_sequences[(even_odd_sequence + 1) % 2]
        # Update the number of occurrences of the all sequences (even or odd)
        num_even_odd_sequences[even_odd_sequence] += 1
    # Return the number of the odd sequences
    return count_odd_sequences
