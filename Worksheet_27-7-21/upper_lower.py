# Q8.WAP to check given character is lower case , uppercase,digit or special symbol.

inp = input("Enter char: ")

if inp.isdigit():
    print("The char is digit")

elif inp.islower():
    print("The char is in lowercase")

elif inp.isupper():
    print("The char is in uppercase")

else:
    print("Its a special char")

'''
OUTPUT:

Enter char: r
The char is in lowercase
'''

    