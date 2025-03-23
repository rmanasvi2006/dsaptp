def longestMountainOptimal(arr):
    n = len(arr)
    max_length, i = 0, 1

    while i < n - 1:
        while i < n - 1 and arr[i] == arr[i - 1]:
            i += 1
        start = i - 1
        while i < n - 1 and arr[i] > arr[i - 1]:
            i += 1
        peak = i - 1
        while i < n - 1 and arr[i] < arr[i - 1]:
            i += 1
        if peak != start and peak != i - 1:
            max_length = max(max_length, i - start)
    return max_length

arr = [2, 1, 4, 7, 3, 2, 5]
print(longestMountainOptimal(arr))
