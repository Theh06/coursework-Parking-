from car_manager import CarManagerFactory
from car_manager import TextCarManager
import os


class Main_menu_services:

    @staticmethod
    def create_parking():
        parking_name = input("Enter the name of the new parking space: ")
        parking_dir = os.path.join('parkings', parking_name)
        if not os.path.exists(parking_dir):
            os.makedirs(parking_dir)
            print(f"Parking space '{parking_name}' created.")
        else:
            print("A parking space with that name already exists.")

    def select_parking(self):
        parking_name = input("Enter the name of the parking space to work with: ")
        parking_dir = os.path.join('parkings', parking_name)
        if os.path.exists(parking_dir):
            manager = CarManagerFactory.get_manager('text', parking_dir)
            return parking_name, manager
        print("Parking space not found.")
        return None, None

    def list_parkings(self):
        print("List of all parking spaces:")
        for name in os.listdir('parkings'):
            parking_dir = os.path.join('parkings', name)
            num_cars = sum(1 for file in os.listdir(parking_dir) if file.endswith('.txt'))
            print(f"{name} - Occupancy: {num_cars} cars")

    def delete_parking(self):
        parking_name = input("Enter the name of the parking space to delete: ")
        parking_dir = os.path.join('parkings', parking_name)
        if os.path.exists(parking_dir):
            for file in os.listdir(parking_dir):
                os.remove(os.path.join(parking_dir, file))
            os.rmdir(parking_dir)
            print(f"Parking space '{parking_name}' deleted.")
        else:
            print("Parking space not found.")

    def search_car(self):
        license_plate = input("Enter the license plate number of the car to search for: ")
        for name in os.listdir('parkings'):
            parking_dir = os.path.join('parkings', name)
            manager = TextCarManager(parking_dir)
            if manager:
                brand, parking_name = manager.find_car_by_plate(license_plate)
                if brand:
                    print(f"Car with license plate {license_plate}, {brand} found in {parking_name}.")
                    return brand, parking_name
        print(f"No matching car found in any parking space.")
