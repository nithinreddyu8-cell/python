class Car:
   def __init__(self, brand, color):
       self.brand = brand
       self.color = color

# create two objects from the Car class
car1 = Car('Toyota', 'red')
car2 = Car('Lambo', 'green')

print('Car 1 Brand:', car1.brand) # Car 1 Brand: Toyota
print('Car 1 Color:', car1.color) # Car 1 Color: red

print('Car 2 Brand:', car2.brand) # Car 2 Brand: Lambo
print('Car 2 Color:', car2.color) # Car 2 Color: green