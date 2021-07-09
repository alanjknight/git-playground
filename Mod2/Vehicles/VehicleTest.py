from Car import Car
from Truck import Truck
from Motorcycle import Motorcycle

v1 = Car("Hyundai", "Santa Fe", 10000)
v2 = Motorcycle("Honda", "FireBlade", 5000)
v3 = Truck("Ford", "Ranger",100000)

print(v1.to_string())
print(v2.to_string())
print(v3.to_string())
