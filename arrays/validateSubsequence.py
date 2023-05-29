arr = [5, 1, 22, 25, 6, -1, 8, 10]
sub = [1, 6, -1, 10]

def isValidSubsequence(array, sub):
    toCompare = []
    for num in array:
        if num in sub and len(toCompare) < len(sub):
            toCompare.append(num)

    return toCompare == sub


print(isValidSubsequence(arr, sub))