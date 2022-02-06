from doctest import OutputChecker


lst = [1, 1, 2, 3, 4, 5, 6, 1, 1, 7, 8, 1, 10, 22, 1, 34, 4]

cnt = 0
inp = int(input('Enter num: '))
for i in lst:
    if i == inp:
        cnt+=1

print(f"{inp} occured {cnt} times.")

# OUTPUT
# Enter num: 1
# 1 occured 6 times.

# Code by Rishabh Shah