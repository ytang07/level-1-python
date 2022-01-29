# create a nested list
nlist1 = [[]]
nlist2 = [[1,2],[3,4,5]]

# create a list with list comprehension
nlist_comp1 = [[i for i in range(5)], [i for i in range(7)], [i for i in range(3)]]
nlist_comp2 = [[i for i in range(n)] for n in range(3)]
print(nlist_comp1)
print(nlist_comp2)

# append a list
list1 = [8, 7, 6]
nlist_comp1.append(list1)
print(nlist_comp1)

# concat nested lists
concat_nlist = nlist_comp1 + nlist_comp2
print(concat_nlist)

# reverse a nested list
concat_nlist.reverse()
print(concat_nlist)
concat_nlist.reverse()

# reverse sub elements of nested list
for _list in concat_nlist:
    _list.reverse()
print(concat_nlist)
for _list in concat_nlist:
    _list.reverse()

# reverse sub elements + elements of a nested list
for _list in concat_nlist:
    _list.reverse()
concat_nlist.reverse()
print(concat_nlist)
for _list in concat_nlist:
    _list.reverse()
concat_nlist.reverse()

# flatten list
flat_list = [ele for sublist in concat_nlist for ele in sublist]
print(flat_list)

# reverse elements of a flattened list
flat_list.reverse()
print(flat_list)
