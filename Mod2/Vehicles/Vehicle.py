from abc import ABC, abstractmethod

class Vehicle(ABC):
    base_sale_price = 0
    wheels = 0
    
    def __init__(self, make, model, miles):
        self.make=make
        self.model=model
        self.miles=miles

    def sale_price(self):
        return 5000.0 * self.wheels

    def purchase_price(self):
        return self.base_sale_price - (0.1 * self.miles)

    @abstractmethod
    def vehicle_type(self):
        pass    

    def to_string(self):
        return self.make, self.model, self.miles, self.base_sale_price, self.wheels, self.vehicle_type()