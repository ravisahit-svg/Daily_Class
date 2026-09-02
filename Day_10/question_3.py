'''
Find the Intersection of Two Lists
Write a Python function to find the intersection of two lists.
Input: [1, 2, 3, 4], [3, 4, 5, 6]
Output: [3, 4]

'''

def find_intersection(list1, list2):
    result = []

    for item in list1:
        if item in list2 and item not in result:
            result = result + [item]

    return result


a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

print(find_intersection(a, b))