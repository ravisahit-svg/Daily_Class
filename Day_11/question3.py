'''
Find All Pairs in a List that Sum to a Specific Value
Write a Python function to find all pairs in a list that sum to a specific value.
Input: [1, 2, 3, 4, 5], Sum=6
Output: [(1, 5), (2, 4)]
'''
def find_pairs(numbers, target):
    pairs = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pairs = pairs + [(numbers[i], numbers[j])]

    return pairs


# Example
numbers = [1, 2, 3, 4, 5]
target = 6

result = find_pairs(numbers, target)

print(result)
