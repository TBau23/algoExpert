def sortedSquaredArray(array):
    result = [0] * len(array)
    start = 0
    end = len(array) - 1
    insert = len(result) - 1
    while start <= end:
        if abs(array[start]) <= abs(array[end]):
            result[insert] = array[end] ** 2
            end = end - 1
        else:
            result[insert] = array[start] ** 2
            start = start + 1
            
        insert = insert - 1

    return result