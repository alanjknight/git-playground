from Vehicle import Vehicle

class Car(Vehicle):
    base_sale_price = 8000
    wheels = 4
    
    def vehicle_type(self):
        return ("Car")
