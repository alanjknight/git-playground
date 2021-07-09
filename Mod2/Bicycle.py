class Bicycle:
    wheels = 2
    def __init__(self, make, model):
        self.make=make
        self.model=model

        #start in first gear
        self.gear = 1

    def change_gear(self, gear):
        self.gear=gear


my_bike = Bicycle("Cannondale", "Optimo")
print(my_bike.make)
print(my_bike.model)
print(my_bike.wheels)
print(my_bike.gear)
my_bike.change_gear(3)
print(my_bike.gear)
