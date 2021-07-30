# Q10.WAP to calculate tax on the income.
# Income Rate
# upto 250000 0%
# 250000-500000 5%
# 500000-1000000 20%
# above 1000000 30%

inc = int(input("Enter income: "))

def calc_tax(per):
    global inc
    if per == 0:
        return "You dont have to pay tax"
    else:
        return (per/100) * inc

if inc < 250000:
    calc_tax(0)

elif 250000 <= inc <= 500000:
    print(f"Your tax is {calc_tax(5)}")

elif 500000 < inc <= 1000000:
    print(f"Your tax is {calc_tax(20)}")

else:
    print(f"Your tax is {calc_tax(30)}")

'''
OUTPUT:

Enter income: 500000
Your tax is 25000.0

'''