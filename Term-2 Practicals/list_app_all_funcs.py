lst = [0,1,2,99,3,4,5,6,7,8,9]

lst.append(10)
print(lst)
lst_copy = lst.copy()
print(lst_copy)
cnt = lst.count(8)
print(cnt)
lst.extend([11,12,13])
print(lst)
ind = lst.index(4)
print(ind)
popped = lst.pop(13)
print(popped)
lst.remove(5)
print(lst)
lst.reverse()
print(lst)
lst.sort()
print(lst)
lst.clear()
print(lst)

# OUTPUT
# [0, 1, 2, 99, 3, 4, 5, 6, 7, 8, 9, 10]
# [0, 1, 2, 99, 3, 4, 5, 6, 7, 8, 9, 10]
# 1
# [0, 1, 2, 99, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# 5
# 12
# [0, 1, 2, 99, 3, 4, 6, 7, 8, 9, 10, 11, 13]
# [13, 11, 10, 9, 8, 7, 6, 4, 3, 99, 2, 1, 0]
# [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 13, 99]
# []

# Code by Rishabh Shah