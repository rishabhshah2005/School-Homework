# Q14.Write a menu driven program for following:

# 1. Area of a circle
# 2. Area of a rectangle
# 3. Area of a square
# 4. Area of trapezium


print("1. Area of a circle\n2. Area of a rectangle\n3. Area of a square\n4. Area of trapezium\n5. Exit")

while True:
    index = int(input("Enter the index of your calc: "))
    if index == 1:
        rad = float(input("Enter the radius: "))
        print(f"The area is {22/7 * rad ** 2}")

    elif index == 2:
        l = float(input("Enter Length: "))
        b = float(input("Enter breath: "))
        print(f"The area of the rectangle is {l*b}")

    elif index == 3:
        side = float(input("Enter Side: "))
        print(f"The area of the square is {side ** 2}")

    elif index == 4:
        side1 = float(input("Enter side 1: "))
        side2 = float(input("Enter side 2: "))
        h = float(input("Enter height: "))
        print(f"The area of trapezium is {((side1+side2)*h) / 2}")

    else:
        exit()

'''
OUTPUT:

1. Area of a circle
2. Area of a rectangle
3. Area of a square
4. Area of trapezium
5. Exit
Enter the index of your calc: 4
Enter side 1: 34
Enter side 2: 23
Enter height: 13
The area of trapezium is 370.5
Enter the index of your calc: 0
'''

