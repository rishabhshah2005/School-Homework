# Q15.WAP to calculate total selling price after levying of GST.

def calc_tax(pri, per):
    return (per/100) * pri

print("Is your item 1.Footwear or 2. Apparels")

index = input("Enter index of your item: ")

if index =='1':
    price = float(input("Enter price of footwear: "))

    if price >= 500:
        print(f"The total price is {price + (calc_tax(price, 18))}")

    else:
                print(f"The total price is {price + (calc_tax(price, 5))}")

if index =='2':
    price = float(input("Enter price of Apparel: "))

    if price >= 1000:
        print(f"The total price is {price + (calc_tax(price, 12))}")

    else:
        print(f"The total price is {price + (calc_tax(price, 5))}")

else:
    print("Enter correct index")

'''
OUTPUT:

Is your item 1.Footwear or 2. Apparels
Enter index of your item: 2
Enter price of Apparel: 3000
The total price is 3360.0
'''