def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def minimum_swaps(arr):
    new_arr = list(enumerate(arr))

    new_arr.sort(key=lambda x: x[1])
    count = 0

    index = 0
    while index < len(arr):
        if new_arr[index][0] == index:
            index += 1

            continue

        swap(new_arr, index, new_arr[index][0])
        count += 1
    return count
