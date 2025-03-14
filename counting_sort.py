def counting_sort(arr):
    max_num = arr[0]
    for i in range(1, len(arr)):
        if max_num < arr[i]:
            max_num = arr[i]
    count_arr = [0] * (max_num + 1)
    for i in range(len(arr)):
        count_arr[arr[i]] += 1
    counter = 0
    for i in range(len(count_arr)):
        for j in range(count_arr[i]):
            arr[counter] = i
            counter += 1
    return arr


def stable_counting_sort(arr):
    max_num = arr[0]
    for i in range(1, len(arr)):
        if max_num < arr[i]:
            max_num = arr[i]
    count_arr = [None] * (max_num + 1)
    for i in range(max_num + 1):
        count_arr[i] = []
    for i in range(len(arr)):
        count_arr[arr[i]].append(arr[i])
    counter = 0
    for i in range(len(count_arr)):
        for j in range(len(count_arr[i])):
            arr[counter] = count_arr[i][j]
            counter += 1
    return arr
print(stable_counting_sort([1,2,3,4,5,5,3,7]))

