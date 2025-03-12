def merge(arr1, arr2):
    i = 0
    j = 0
    total = 0
    res = []
    while i < len(arr1) and j < len(arr2):
        l_size = len(arr1) - i
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            total += l_size
            j += 1
    res += arr1[i:]
    res += arr2[j:]
    return res, total

def split(arr):
    mid = len(arr)//2
    arr1 = arr[:mid]
    arr2 = arr[mid:]
    return arr1, arr2

def merge_sort(arr):
    total = 0
    if len(arr) == 1:
        return arr, 0
    else:
        arr1, arr2 = split(arr)
        arr1 = merge_sort(arr1)
        arr2 = merge_sort(arr2)
        total += arr1[1] + arr2[1]
        temp = merge(arr1[0], arr2[0])
        return temp[0], total + temp[1]


print(merge_sort([5,2,3,4,6]))