
class Vehicle:
    def __init__(self, vehicle_id, manufacturer, model, engine_power, price, color, mileage, year, fuel_type, transmission) -> None:
        
        self.__vehicle_id = vehicle_id
        self.__manufacturer = manufacturer
        self.__model = model
        self.__engine_power = engine_power
        self.__price = price
        self.__color = color
        self.__mileage = mileage
        self.__year = year
        self.__fuel_type = fuel_type
        self.__transmission = transmission
        
    def set_vehicle_id(self, vehicle_id):
        self.vehicle_id = vehicle_id
    def get_vehicle_id(self):
        return self.__vehicle_id
    
    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer
    def get_manufacturer(self):
        return self.__manufacturer
    
    def set_model(self, model):
        self.__manufacturer = model
    def get_model(self):
        return self.__model
    
    def set_engine_power(self, engine_power):
        self.__engine_power = engine_power
    def get_engine_power(self):
        return self.__engine_power
    
    def set_price(self, price):
        self.__price = price
    def get_price(self):
        return self.__price
    
    def set_color(self, color):
        self.__color = color
    def get_color(self):
        return self.__color
    
    def set_mileage(self, mileage):
        self.__mileage = mileage
    def get_mileage(self):
        return self.__mileage
    
    def set_year(self, year):
        self.__year = year
    def get_year(self):
        return self.__year

    def set_fuel_type(self, fuel_type):
        self.__fuel_type = fuel_type
    def get_fuel_type(self):
        return self.__fuel_type

    def set_transmission(self, transmission):
        self.__transmission = transmission
    def get_transmission(self):
        return self.__transmission
    
