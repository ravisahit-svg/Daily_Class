'''

Flatten a Nested List
Write a Python function to flatten a nested list.
Input: [[1, 2], [3, 4], [5]]
Output: [1, 2, 3, 4, 5]

'''

def flatten_list(nested_list):
    flattened = []

    for sublist in nested_list:
        flattened = flattened + sublist

    return flattened


# Example
numbers = [[1, 2], [3, 4], [5]]

result = flatten_list(numbers)

print(result)
