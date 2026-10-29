amount = float(input("Enter order amount: "))

if amount >= 1000:
    charge = 0
else:
    charge = 50

print("Delivery charge:", charge)