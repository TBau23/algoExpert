def twoNumberSum(array, targetSum):
    dict = {}
    for num in array:
        dict[num] = targetSum - num

    for num in dict:
        if dict[num] in array and dict[num] != num:
            return [num, dict[num]]
    return []



test = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10

print(twoNumberSum(test, target))