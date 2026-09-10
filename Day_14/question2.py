def check_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    for char in str1:
        count1 = 0
        count2 = 0

        for x in str1:
            if x == char:
                count1 += 1

        for y in str2:
            if y == char:
                count2 += 1

        if count1 != count2:
            return False

    return True


print(check_anagram("listen", "silent"))