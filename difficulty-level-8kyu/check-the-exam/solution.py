"""
Python solution for challenge: "Check the exam"
To start the tests, type from CLI: python tests-.py
"""


def check_exam(arr1, arr2):
    count = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            count += 4
        elif arr1[i] != arr2[i] and arr2[i]:
            count -= 1
    return count if count > 0 else 0

