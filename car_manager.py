import os
from abc import ABC, abstractmethod

class CarManager(ABC):

    def __init__(self, storage_dir):
        self.storage_dir = storage_dir
        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir)

    @abstractmethod
    def add_car(self, license_plate, brand):
        pass

    @abstractmethod
    def remove_car(self, license_plate):
        pass

    @abstractmethod
    def list_cars(self):
        pass

class CarManagerFactory:

    @staticmethod
    def get_manager(manager_type, storage_dir):
        if manager_type == 'text':
            return TextCarManager(storage_dir)
        raise ValueError("Unknown manager type")

class TextCarManager(CarManager):

    _instance = None

    def __new__(cls, storage_dir):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, storage_dir):
        if not hasattr(self, 'initialized'):
            super().__init__(storage_dir)
            self.initialized = True

    def add_car(self, license_plate, brand):
        file_path = os.path.join(self.storage_dir, f'{license_plate}.txt')
        with open(file_path, 'w') as file:
            file.write(f'{license_plate}, {brand}\n')
        print(f"Car {license_plate} of brand {brand} added.")
    
    def edit_car(self, old_license_plate, new_license_plate, brand):
        old_file_path = os.path.join(self.storage_dir, f'{old_license_plate}.txt')
        if os.path.exists(old_file_path):
            os.remove(old_file_path)
            new_file_path = os.path.join(self.storage_dir, f'{new_license_plate}.txt')
            with open(new_file_path, 'w') as file:
                file.write(f'{new_license_plate}, {brand}\n')
            print("Car information edited successfully.")
        else:
            print("Car not found.")

    def remove_car(self, license_plate):
        file_path = os.path.join(self.storage_dir, f'{license_plate}.txt')
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Car {license_plate} removed.")
        else:
            print("Car not found.")

    def list_cars(self):
        car_files = [filename for filename in os.listdir(self.storage_dir) if filename.endswith('.txt')]
        num_cars = len(car_files)
        print(f"Number of cars in the parking space: {num_cars}")
        if num_cars > 0:
            print("List of cars:")
            for filename in car_files:
                with open(os.path.join(self.storage_dir, filename), 'r') as file:
                    car_info = file.readline().strip()
                    print(car_info)
        else:
            print("No cars parked in this space.")
    
    def find_car_by_plate(self, license_plate):
        for name in os.listdir('parkings'):
            parking_dir = os.path.join('parkings', name)
            car_files = [filename for filename in os.listdir(parking_dir) if filename.endswith('.txt')]
            for filename in car_files:
                with open(os.path.join(parking_dir, filename), 'r') as file:
                    car_info = file.readline().strip()
                    plate, brand = car_info.split(', ')
                    if plate == license_plate:
                        return brand, name 
        return None, None
