test_arr = [2, 1, 6, 4, 9, 3]
# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    for i in range(elements):
        if arrA and arrB:
            if arrA[0] <= arrB[0]:
                merged_arr[i] = arrA.pop(0)
            else:
                merged_arr[i] = arrB.pop(0)
        elif arrA:
            merged_arr[i] = arrA.pop(0)
        else:
            merged_arr[i] = arrB.pop(0)
    return merged_arr


x = [1, 2, 6]
y = [3, 4, 9]
# print(merge(x, y))
# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    midpoint = len(arr) // 2
    # arr1 = [element
    #         for index, element in enumerate(arr) if index < midpoint]
    # arr2 = [element for index, element in enumerate(arr) if index >= midpoint]
    arr1 = arr[:midpoint]
    arr2 = arr[midpoint:]
    return merge(merge_sort(arr1), merge_sort(arr2))


# print(merge_sort(test_arr))

# Less recursive version
# def merge_sort(arr):
#     # TO-DO
#     if arr == []:
#         return []
#     arr = [[element] for element in arr]
#     print(arr)
#     while len(arr) > 1:
#         arr[0] = merge(arr[0], arr[-1])
#         arr.pop()
#     print(arr)
#     return arr[0]

# STRETCH: implement an in-place merge sort algorithm

test_arr2 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


def merge_in_place(arr, start, mid, end):
    # TO-DO
    print(arr, start, mid, end)
    while start < end and mid < end:
        if arr[start] <= arr[mid]:
            start += 1
        else:
            arr.insert(start, arr.pop(mid))
            start += 1
            mid += 1

    return arr


# merge_in_place(test_arr2, 0, len(test_arr2) // 2, len(test_arr2))


def merge_sort_in_place(arr, l, r):
    # TO-DO
    if len(arr) <= 1:
        return arr
    midpoint = (l + r) // 2

    arr1 = arr[:midpoint]
    arr2 = arr[midpoint:]
    return merge_in_place(arr1 + arr2, l, midpoint, r)


print(merge_sort_in_place(test_arr2, 0, len(test_arr2)))


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
