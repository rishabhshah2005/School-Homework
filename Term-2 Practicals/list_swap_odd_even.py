lst = [0,1,2,3,4,5,6,7,8,9]

for i in lst:
    ind = lst.index(i)
    if ind % 2 == 0:
        try:
            a = lst[ind+1]
            lst[ind+1] = i
            lst[ind] = a
        except:
            pass

print(lst)

#OUTPUT
# [1, 0, 3, 2, 5, 4, 7, 6, 9, 8]

# Code by Rishabh Shah