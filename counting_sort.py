def counting_sort(unsorted: list):
    size = len(unsorted)
    sorted_list = [0]*size
    _max = max(unsorted, key=lambda item:item[0])[0]
    
    # get counts of each integer in unsorted
    count = [0]*(_max+1)
    for i in range(size):
        count[unsorted[i][0]] += 1
        # print(count)
    
    # get cumulative count
    for i in range(1, _max+1):
        count[i] += count[i-1]
        # print(count)
    
    # create sorted list
    i = size - 1
    while i >= 0:
        sorted_list[count[unsorted[i][0]] - 1] = unsorted[i]
        count[unsorted[i][0]] -= 1
        # print(sorted_list)
        # print(count)
        i -= 1
    
    return sorted_list

# unsorted1 = [5, 2, 1, 7, 3, 3, 5, 2, 7, 4, 11]
# unsorted2 = [4, 1, 2, 2, 3, 9, 8, 9, 2]
unsorted3 = [(3,'a'), (1,'a'), (1,'b'), (2,'a'), (2,'b')]
# print(counting_sort(unsorted1))
# print(counting_sort(unsorted2))
print(counting_sort(unsorted3))