def flatten_list(nested_list):
    result = []

    for sublist in nested_list:
        for item in sublist:
            result.append(item)

    return result

numbers = [[1, 2], [3, 4], [5]]

print(flatten_list(numbers))