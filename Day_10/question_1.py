'''
Find the Maximum and Minimum Elements in a List
Write a Python function to find the maximum and minimum elements in a given list.
Input: [3, 1, 4, 1, 5, 9]
Output: (9, 1)

'''


def find_max_min(numbers):
    maximum = numbers[0]
    minimum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

        if num < minimum:
            minimum = num

    return maximum, minimum


nums = [3, 1, 4, 1, 5, 9]

print(find_max_min(nums))