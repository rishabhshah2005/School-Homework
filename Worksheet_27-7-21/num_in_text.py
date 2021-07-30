# Q6.WAP to display Digit in text (0 to 9) .

text = input("Enter text: ")

for i in text:
    if i.isdigit():
        print(i)
    else:
        continue

'''
OUTPUT:

Enter text: now eve wa 34 fa 343fa
3
4
3
4
3
'''