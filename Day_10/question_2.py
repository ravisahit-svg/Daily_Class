'''
Remove Duplicates from a List
Write a Python function to remove duplicates from a list while preserving the order.
Input: [1, 2, 2, 3, 4, 4, 5]
Output: [1, 2, 3, 4, 5]
'''

def remove_duplicates(numbers):
    result = []

    for num in numbers:
        if num not in result:
            result = result + [num]

    return result


nums = [1, 2, 2, 3, 4, 4, 5]

print(remove_duplicates(nums))