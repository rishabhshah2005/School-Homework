price = float(input("Enter The price: "))
quan = float(input("Enter the quantity: "))

og_price = price * quan
discount = 10/100 * og_price
now_price = og_price - discount

print(f"Total amount = ${og_price}")
print(f"Discount(10%) = ${discount}")
print(f"Net amount = ${now_price}")

# Made by Rishabh Shah XI-A