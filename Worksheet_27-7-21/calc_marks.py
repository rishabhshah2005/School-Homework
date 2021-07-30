# Q11.WAP to accept marks for 5 subjects , 
# calculate the percentage and print the grade.

totalmarks = 0

for i in range(1, 6):
    marks = float(input(f"Enter marks(/100) for sub{i}: "))
    totalmarks = totalmarks + marks

percent = (totalmarks/500) * 100

if percent <= 100:
    print(f"You got {str(percent)[0:4]}%")
else:
    print("Percentage cant exceed 100. Enter correct values")

'''
OUTPUT:

Enter marks(/100) for sub1: 90
Enter marks(/100) for sub2: 89
Enter marks(/100) for sub3: 99 
Enter marks(/100) for sub4: 100
Enter marks(/100) for sub5: 83 
You got 92.2%
'''
