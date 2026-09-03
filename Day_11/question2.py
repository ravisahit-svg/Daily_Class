'''
Merge Two Sorted Lists
Write a Python function to merge two sorted lists into a single sorted list.
Input: [1, 3, 5], [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
'''

def merge_sorted_lists(list1, list2):
    merged = []

    while list1 and list2:
        if list1[0] < list2[0]:
            merged = merged + [list1[0]]
            list1 = list1[1:]
        else:
            merged = merged + [list2[0]]
            list2 = list2[1:]

    merged = merged + list1
    merged = merged + list2

    return merged


# Example
list1 = [1, 3, 5]
list2 = [2, 4, 6]

result = merge_sorted_lists(list1, list2)

print(result)
