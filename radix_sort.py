from math import log

def radix_sort(arr, no_of_digit):
    max_num = arr[0]
    for i in range(1, len(arr)):
        if max_num < arr[i]:
            max_num = arr[i]
    col = int(log(max_num, 10)) + 1
    arr = [(i, None) for i in arr]
    for i in range(col//no_of_digit):
        # cur = 10 ** i
        count_arr = [None] * (10 ** no_of_digit)
        # initiliazing empty seperate chaining for each iteration
        for j in range((10 ** no_of_digit)):
            count_arr[j] = []
        for j in range(len(arr)):
            count_arr[(arr[j][0]%10**(i+1))//10**i].append(arr[j])
        counter = 0
        for i in range(len(count_arr)):
            for j in range(len(count_arr[i])):
                arr[counter] = count_arr[i][j]
                counter += 1
    return arr

# print(radix_sort([1234098,8970987,2346643,10012310],3))
print(radix_sort([464,392,554,402],1))
