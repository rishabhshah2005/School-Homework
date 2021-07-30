# Q9.WAP to calculate gross salary of an employee for following allowance:


basic = float(input("Enter salary: "))

DA = 0.25 * basic
HRA = 0.15 * basic
PF = 0.12 * basic
TA = 0.075 * basic
net = basic + DA + HRA + TA

print(f"NetPay: {net}")
print(f"Gross Pay: {net - PF}")

'''
OUTPUT:

Enter salary: 120000
NetPay: 177000.0
Gross Pay: 162600.0
'''
