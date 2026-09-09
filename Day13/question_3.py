def find_pairs(numbers, target):
    return [
        (numbers[i], numbers[j])
        for i in range(len(numbers))
        for j in range(i + 1, len(numbers))
        if numbers[i] + numbers[j] == target
    ]


numbers = [1, 2, 3, 4, 5]
target = 6

print(find_pairs(numbers, target))