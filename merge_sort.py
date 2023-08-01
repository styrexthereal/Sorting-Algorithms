""" Merge Sort Algorithm in Python """


def merge_sort(arr: list) -> None:
    if len(arr) > 1:
        mid = len(arr) // 2
        sub_arr1 = arr[:mid]
        sub_arr2 = arr[mid:]

        merge_sort(sub_arr1)
        merge_sort(sub_arr2)

        i = j = k = 0

        while i < len(sub_arr1) and j < len(sub_arr2):
            if sub_arr1[i] < sub_arr2[j]:
                arr[k] = sub_arr1[i]
                i += 1
            else:
                arr[k] = sub_arr2[j]
                j += 1
            k += 1

        while i < len(sub_arr1):
            arr[k] = sub_arr1[i]
            i += 1
            k += 1

        while j < len(sub_arr2):
            arr[k] = sub_arr2[j]
            j += 1
            k += 1


arr: list = [10, 9, 2, 4, 6, 13]
merge_sort(arr)
print(arr)
