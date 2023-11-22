from controll_model import Vehicle
from controll_enums import Manufacturer
# prepared csv module importer 
import csv
from typing import List

class VehicleFileManager:
    def __init__(self, file_path):
        self.file_path = file_path
    #reads data from the CSV file and then transforms that data into a different format using another method within the class 
    def import_vehicles_from_file(self):
        # "r" indicated that the file is opened for reading
        with open(self.file_path, 'r') as file:
            csv_reader = csv.reader(file)
            return self._transform_csv_vehicle_data_to_vehicles(csv_reader)
        
    #The function reads each row of the CSV file and extracts the values of the columns. 
    def _transform_csv_vehicle_data_to_vehicles(self, csv_reader):
        vehicles = []
        #starts a loop that iterates over each row in the csv_reader object
        for row in csv_reader:
            vehicle_id = row[0]
            manufacturer = row[1]
            model = row[2]
            engine_power = int(row[3])
            price = float(row[4])
            color = row[5]
            mileage = int(row[6])
            year = int(row[7])
            fuel_type = row[8]
            transmission = row[9]

            vehicle = Vehicle(vehicle_id, manufacturer, model, engine_power, price, color, mileage, year, fuel_type, transmission)
            vehicles.append(vehicle)

        return vehicles

    def rewrite_file(self, vehicle_list):
        # This mode creates a new file if it exists, it overwrites the file with the new data.
        with open(self.file_path, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            for vehicle in vehicle_list:
                vehicle_string_for_rewrite = self.prepare_the_vehicle_for_rewriting("", vehicle)
                #The vehicle_string_for_rewrite variable is then split into a list using the comma as a delimiter, and this list is passed to the csv_writer.writerow. 
                csv_writer.writerow(vehicle_string_for_rewrite.split(','))

    def prepare_the_vehicle_for_rewriting(self, vehicle_string_for_rewrite, vehicle):
        # Convert the Vehicle object's attributes to a CSV string
        vehicle_attributes = [
            str(vehicle.get_vehicle_id()),
            vehicle.get_manufacturer(),
            vehicle.get_model(),
            str(vehicle.get_engine_power()),
            str(vehicle.get_price()),
            vehicle.get_color(),
            str(vehicle.get_mileage()),
            str(vehicle.get_year()),
            vehicle.get_fuel_type(),
            vehicle.get_transmission()
        ]
        #Joins the attributes with commas and add to the vehicle_string_for_rewrite
        vehicle_string_for_rewrite = ','.join(vehicle_attributes)
        return vehicle_string_for_rewrite

class VehicleShopPrinter:

    def create_vehicle_list():
    # This function creates a list of Vehicle objects from predefined data
        return [
            Vehicle(1, "SKODA", "Superb", 190, 31000, "BLACK", 5000, 2015, "GASOLINE", "AUTOMATIC"),
            Vehicle(2, "AUDI", "A8", 460, 92000, "WHITE", 7500, 2019, "DIESEL_FUEL", "AUTOMATIC"),
            Vehicle(3, "VW", "Golf7", 220, 39000, "BLUE", 15000, 2012, "GASOLINE", "MANUAL"),
            Vehicle(4, "BMW", "X6", 320, 59000, "BLACK", 15000, 2012, "DIESEL_FUEL", "AUTOMATIC"),
            Vehicle(5, "BMW", "X5", 300, 39000, "WHITE", 153000, 2010, "DIESEL_FUEL", "AUTOMATIC"),
            Vehicle(6, "VW", "Tiguan", 420, 39000, "GREY", 15000, 2012, "DIESEL_FUEL", "AUTOMATIC"),
            Vehicle(7, "VW", "Passat", 220, 25000, "BROWN", 165000, 2013, "GASOLINE", "MANUAL"),
            Vehicle(8, "BMW", "530d", 187, 59000, "BLACK", 23000, 2016, "DIESEL_FUEL", "AUTOMATIC"),
            Vehicle(9, "AUDI", "A3", 350, 29000, "RED", 34000, 2012, "DIESEL_FUEL", "MANUAL"),
            Vehicle(10, "HONDA", "Civic", 150, 7000, "GREY", 153000, 2011, "DIESEL_FUEL", "AUTOMATIC")
        ]
    
    def print_available_vehicles(self, vehicle_list):
        
        print("########################### CATALOG ###########################")

        print("\nAvailable Vehicles:")
        for vehicle in vehicle_list:
            print(f"ID: {vehicle.get_vehicle_id()}, \n"
                  f"Manufacturer: {vehicle.get_manufacturer()}, \n"
                  f"Model: {vehicle.get_model()}, \n"
                  f"Price: {vehicle.get_price()}, \n"
                  f"Engine Power: {vehicle.get_engine_power()}HP, \n"
                  f"Color: {vehicle.get_color()}, \n"
                  f"Mileage: {vehicle.get_mileage()}km, \n"
                  f"Year: {vehicle.get_year()}, \n"
                  f"Fuel Type: {vehicle.get_fuel_type()}, \n"
                  f"Transmission: {vehicle.get_transmission()} \n")
        
        print("########################### CATALOG ###########################")
    
    def print_vehicle_sold_message(self, vehicle_chosen_id):
        print(f"\nVehicle with ID" + str(vehicle_chosen_id) + "was sold.")
    
    def print_vehicle_id_to_sell_message(self):
        print("\n\nPlease enter the number (ID) of the vehicle you want to sell: ")
    
    
class VehicleShopProcessor:
    # responsible to sell a specified vehicle by id
    def sell_vehicle(self, vehicles_list, vehicle_chosen_id):
        original_length = len(vehicles_list)
    
        #Prints the IDs before removal
        print("Vehicle IDs before removal:", [vehicle.get_vehicle_id() for vehicle in vehicles_list])
    
        vehicles_list[:] = [vehicle for vehicle in vehicles_list if str(vehicle.get_vehicle_id()) != str(vehicle_chosen_id)]
    
        #Prints the IDs after removal
        print("Vehicle IDs after removal:", [vehicle.get_vehicle_id() for vehicle in vehicles_list])
    
        if len(vehicles_list) < original_length:
           print("Vehicle with ID" + str(vehicle_chosen_id) + "has been sold.")
        else:
           print("Vehicle with ID" + str(vehicle_chosen_id) + "not found in the list.")

class VehicleTransformer:
    #Goes through each element of the input array, and if it is not a string, it is appended to the output list. 
    #If it is a string, calls another method called transform_to_vehicle_object to convert the string into a Vehicle object.
    def transform_data_array_to_vehicle_objects(self, vehicle_data_array: List[str]) -> List[Vehicle]:
        vehicle_objects = []
        for vehicle_string in vehicle_data_array:
            if not isinstance(vehicle_string, str):
                vehicle_objects.append(vehicle_string)
                continue
            elif not isinstance(vehicle_string, str):
                raise ValueError(f"Expected a string, but got: {type(vehicle_string).__name__}")
            vehicle_object = self.transform_to_vehicle_object(vehicle_string)
            vehicle_objects.append(vehicle_object)
        return vehicle_objects

    def transform_to_vehicle_object(self, vehicle_as_string: str) -> Vehicle: 
        vehicle_as_array = vehicle_as_string.split(",")
        vehicle_id = int(vehicle_as_array[0])
        manufacturer = self.get_manufacturer_from_string(vehicle_as_array[1].strip())

        vehicle = Vehicle(vehicle_id, manufacturer)
        return vehicle
    
    def get_manufacturer_from_string(self, manufacturer_as_string: str):
        for manufacturer in Manufacturer:
            if manufacturer.name == manufacturer_as_string:
                return manufacturer
        raise ValueError(f"Manufacturer not supported: {manufacturer_as_string}")
