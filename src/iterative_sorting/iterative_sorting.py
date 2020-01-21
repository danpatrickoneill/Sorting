test_arr = [2, 1, 6, 4, 9, 3]

# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            # print(arr[j], arr[smallest_index])
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    # print(arr)
    return arr


# print(selection_sort(test_arr))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    count = 1
    while count < len(arr):
        for i in range(len(arr) - 1):
            if arr[i + 1] < arr[i]:
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
                count = 1
            else:
                count += 1

    return arr


# print(bubble_sort(test_arr))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):
    d = {}
    for elem in arr:
        if elem > maximum:
            maximum = elem
        if elem < 0:
            return "Error, negative numbers not allowed in Count Sort"
        elif elem in d:
            d[elem] += 1
        else:
            d[elem] = 1

    for i in range(0, maximum + 1):
        if i not in d:
            d[i] = 0

    return arr
