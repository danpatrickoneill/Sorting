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
    midpoint = len(arr) / 2
    arr1 = [element
            for index, element in enumerate(arr) if index < midpoint]
    arr2 = [element for index, element in enumerate(arr) if index >= midpoint]
    print(arr1, arr2)
    return merge(merge_sort(arr1), merge_sort(arr2))


print(merge_sort(test_arr))

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


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
