from controller_general import VehicleFileManager, VehicleShopPrinter, VehicleShopProcessor, VehicleTransformer


class VehicleShop:

    def start(self):

        # File reading
        vehicle_file_manager = VehicleFileManager("vehicle-list.csv")
        vehicle_data_as_string_list = vehicle_file_manager.import_vehicles_from_file()
    
        # Transformation into Vehicle Python Objects
        vehicle_transformer = VehicleTransformer()
        vehicle_list = vehicle_transformer.transform_data_array_to_vehicle_objects(vehicle_data_as_string_list)

        # Printing available vehicles
        vehicle_shop_printer = VehicleShopPrinter()
        vehicle_shop_printer.print_available_vehicles(vehicle_list)

        # User interaction - selecting a vehicle to sell
        vehicle_shop_printer.print_vehicle_id_to_sell_message()
        vehicle_chosen_id = int(input())

        # Selling a vehicle
        vehicle_shop_processor = VehicleShopProcessor()
        vehicle_shop_processor.sell_vehicle(vehicle_list, vehicle_chosen_id)

        # Write new vehicle list back to file
        vehicle_file_manager.rewrite_file(vehicle_list)
      

        # print sold vehicle information and new vehicle list
        vehicle_shop_printer.print_vehicle_sold_message(vehicle_chosen_id)
        vehicle_shop_printer.print_available_vehicles(vehicle_list)

vehicle_shop = VehicleShop()
vehicle_shop.start()