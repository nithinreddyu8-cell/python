cars=["ford","volvo","bmw"]
print(cars[0])
cars[1]="toyota"
print(cars)


#tuples

mytuple=("apple","banana","cherry")
myit=iter(mytuple)
print(next(myit))


import platform 
print(platform.system())


#scnerio based quedtion

amount=int(input("enter a dilvery amount\n"))
if amount >= 1000:
  charge=0
else:
  charge=50
  
print("yours orderis:",charge)


amount=int(input("enter a total purchase amount:\n"))
if amount >= 10000:
  dis=(20/100)*amount
elif amount >= 5000 :
  dis=(10/100)*amount
elif amount >= 2000:
  dis=(5/100)*amount
else:
  dis= "no discount"

final_bill=amount-dis
print("final bill is:",final_bill)