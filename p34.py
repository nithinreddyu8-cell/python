amount = float(input("Enter purchase amount: "))

if amount >= 10000:
    discount = amount * 20 / 100
elif amount >= 5000:
    discount = amount * 10 / 100
elif amount >= 2000:
    discount = amount * 5 / 100
else:
    discount = 0

final_bill = amount - discount

print("Discount:", discount)
print("Final bill:", final_bill)
prices = [1500, 2500, 6000, 12000]

for price in prices:
    print("Product price:", price)

while True:
    amount = float(input("Enter purchase amount: "))

    if amount >= 10000:
        discount = amount * 0.20
        category = "High-value order"
    elif amount >= 5000:
        discount = amount * 0.10
        category = "Medium-value order"
    elif amount >= 2000:
        discount = amount * 0.05
        category = "Low-value order"
    else:
        discount = 0
        category = "Regular order"

    final_bill = amount - discount

    print("Category:", category)
    print("Discount:", discount)
    print("Final bill:", final_bill)

    choice = input("Continue? (yes/no): ")

    if choice.lower() != "yes":
        break
def calculate_marks(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

marks = [75, 80, 85]

total, average = calculate_marks(marks)

print("Total marks:", total)
print("Average marks:", average)
marks = [75, 80, 85]

print("Maximum marks:", max(marks))

def calculate_average(marks):
    return sum(marks) / len(marks)

print("Average marks:", calculate_average(marks))
def calculate_average(marks):
    return sum(marks) / len(marks)

print(calculate_average([75, 80, 85]))
print(calculate_average([60, 70, 90]))