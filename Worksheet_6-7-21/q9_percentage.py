totalmarks = 0

for i in range(1, 6):
    marks = float(input(f"Enter marks(/100) for sub{i}: "))
    totalmarks = totalmarks + marks

percent = (totalmarks/500) * 100

if percent <= 100:
    print(f"You got {str(percent)[0:4]}%")
else:
    print("Percentage cant exceed 100. Enter correct values")

# Made by Rishabh Shah XI-A