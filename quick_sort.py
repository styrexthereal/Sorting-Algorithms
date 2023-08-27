""" Quick Sort Algorithm in Python """


def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose the pivot element
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


arr: list = [10, 5, 2, 8, 3, 7, 1]
sorted_arr: list = quick_sort(arr)
print(sorted_arr)
