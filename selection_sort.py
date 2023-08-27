""" Selection Sort Algorithm in Python """


def selection_sort(arr: list, size: int) -> None:
    for i in range(size):
        min_i = i
        for j in range(i+1, size):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]


arr: list = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
size: int = len(arr)
selection_sort(arr, size)

print('The array after sorting in Ascending Order by selection sort is:')
print(arr)
