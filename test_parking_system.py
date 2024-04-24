import unittest, os, shutil
from car_manager import TextCarManager
from unittest.mock import patch, MagicMock, mock_open, call
from main_menu_functions import Main_menu_services
import sys
from io import StringIO

class TestParkingSystem(unittest.TestCase):

    def setUp(self):
        self.menu_services = Main_menu_services()
        self.license_plate = 'ABC123'
        self.brand = 'Toyota'
        self.manager = TextCarManager('parkings/TestParking')

        self.storage_dir = 'parkings/TestParking'
        self.manager = TextCarManager(self.storage_dir)

    @patch('builtins.input', return_value='TestParking')
    @patch('os.makedirs')
    @patch('os.path.exists', return_value=False)
    def test_create_parking(self, mock_exists, mock_makedirs, mock_input):
        self.menu_services.create_parking()
        mock_makedirs.assert_called_once_with(os.path.join('parkings', 'TestParking'))

    @patch('builtins.input', return_value='TestParking')
    @patch('os.path.exists', return_value=True)
    def test_select_parking(self, mock_exists, mock_input):
        parking_name, manager = self.menu_services.select_parking()
        self.assertEqual(parking_name, 'TestParking')
        self.assertIsNotNone(manager)
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='ABC123')
    def test_search_car(self, mock_input):
        with patch.object(TextCarManager, 'find_car_by_plate', return_value=('Toyota', 'TestParking')) as mock_find:
            brand, parking_name = self.menu_services.search_car()
            self.assertEqual(brand, 'Toyota')
            self.assertEqual(parking_name, 'TestParking')
            mock_find.assert_called_once_with('ABC123')
            mock_input.assert_called_once()

    @patch('os.listdir')
    def test_list_parkings(self, mock_listdir):
        mock_listdir.side_effect = [['TestParking1'], ['ABC123.txt', 'XYZ789.txt']]

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.menu_services.list_parkings()
            expected_output = "List of all parking spaces:\nTestParking1 - Occupancy: 2 cars\n"
            self.assertEqual(fake_output.getvalue(), expected_output)
            expected_calls = [call('parkings'), call(os.path.join('parkings', 'TestParking1'))]
            mock_listdir.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.input', return_value='TestParking')
    @patch('os.path.exists', return_value=True)
    @patch('os.rmdir')
    @patch('os.listdir', return_value=[])
    @patch('os.remove')
    def test_delete_parking(self, mock_remove, mock_listdir, mock_rmdir, mock_exists, mock_input):
        self.menu_services.delete_parking()
        mock_rmdir.assert_called_once_with(os.path.join('parkings', 'TestParking'))
        mock_input.assert_called_once()

  #-----------------------------------
        
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.join')
    def test_add_car(self, mock_path_join, mock_file_open):
        file_path = os.path.join('parkings/TestParking', f'{self.license_plate}.txt')
        mock_path_join.return_value = file_path
        self.manager.add_car(self.license_plate, self.brand)
        mock_file_open.assert_called_once_with(file_path, 'w')
        mock_file_open().write.assert_called_once_with(f'{self.license_plate}, {self.brand}\n')
    
    @patch('os.path.join')
    @patch('os.path.exists', return_value=True)
    @patch('os.remove')
    def test_remove_car(self, mock_remove, mock_exists, mock_path_join):
        file_path = os.path.join('parkings/TestParking', f'{self.license_plate}.txt')
        mock_path_join.return_value = file_path
        self.manager.remove_car(self.license_plate)
        mock_remove.assert_called_once_with(file_path)

    @patch('os.listdir', return_value=['ABC123.txt', 'XYZ789.txt'])
    def test_list_cars_in_parking(self, mock_listdir):
        mock_file_data = {'ABC123.txt': 'ABC123, Toyota', 'XYZ789.txt': 'XYZ789, Honda'}
        with patch('builtins.open', mock_open()) as mock_file:
            mock_file.side_effect = lambda f, mode: StringIO(mock_file_data[os.path.basename(f)])
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.manager.list_cars()
                expected_output = "Number of cars in the parking space: 2\nList of cars:\nABC123, Toyota\nXYZ789, Honda\n"
                self.assertEqual(fake_output.getvalue(), expected_output)
            calls = [call(os.path.join(self.storage_dir, 'ABC123.txt'), 'r'), 
                    call(os.path.join(self.storage_dir, 'XYZ789.txt'), 'r')]
            mock_file.assert_has_calls(calls, any_order=True)

    @patch('os.path.join', lambda a, b: f"{a}/{b}") 
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.remove')
    @patch('os.path.exists')
    def test_edit_car_car_exists(self, mock_exists, mock_remove, mock_file_open):
        mock_exists.return_value = True
        old_license_plate = 'ABC123'
        new_license_plate = 'XYZ789'
        brand = 'Toyota'
        
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.manager.edit_car(old_license_plate, new_license_plate, brand)
            self.assertEqual(fake_output.getvalue().strip(), "Car information edited successfully.")
        
        mock_remove.assert_called_once_with(f'{self.storage_dir}/{old_license_plate}.txt')
        mock_file_open.assert_called_once_with(f'{self.storage_dir}/{new_license_plate}.txt', 'w')
        mock_file_open().write.assert_called_once_with(f'{new_license_plate}, {brand}\n')

    @patch('os.path.join', lambda a, b: f"{a}/{b}") 
    @patch('os.remove')
    @patch('os.path.exists')
    def test_edit_car_car_not_found(self, mock_exists, mock_remove):
        mock_exists.return_value = False
        old_license_plate = 'ABC123'
        new_license_plate = 'XYZ789'
        brand = 'Toyota'
        
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.manager.edit_car(old_license_plate, new_license_plate, brand)
            self.assertEqual(fake_output.getvalue().strip(), "Car not found.")
        
        mock_remove.assert_not_called()
    
    @patch('os.path.join', lambda a, b: f"{a}/{b}")
    @patch('os.listdir')
    def test_find_car_by_plate_found(self, mock_listdir):
        # Mock data
        parking_dirs = ['TestParking1', 'TestParking2']
        car_files = {'TestParking1': ['ABC123.txt', 'DEF456.txt'], 'TestParking2': ['GHI789.txt']}
        car_data = {'ABC123.txt': 'ABC123, Toyota\n', 'DEF456.txt': 'DEF456, Honda\n', 'GHI789.txt': 'GHI789, Ford\n'}
        mock_file = mock_open(read_data='not important')

        mock_listdir.side_effect = lambda x: parking_dirs if x == 'parkings' else car_files.get(os.path.basename(x), [])
        mock_file().readline.side_effect = [car_data[filename] for parking in parking_dirs for filename in car_files.get(parking, [])]

        with patch('builtins.open', mock_file):
            brand, parking_name = self.manager.find_car_by_plate('DEF456')
            self.assertEqual((brand, parking_name), ('Honda', 'TestParking1'))

    @patch('os.path.join', lambda a, b: f"{a}/{b}")
    @patch('os.listdir', return_value=['TestParking1', 'TestParking2'])
    def test_find_car_by_plate_not_found(self, mock_listdir):
        car_files = {'TestParking1': ['ABC123.txt'], 'TestParking2': ['GHI789.txt']}
        car_data = {'ABC123.txt': 'ABC123, Toyota', 'GHI789.txt': 'GHI789, Ford'}
        mock_file = mock_open()

        mock_listdir.side_effect = lambda x: car_files.get(x.split('/')[-1], [])
        mock_file().readline.side_effect = lambda: car_data.get(os.path.basename(mock_file().name))

        with patch('builtins.open', mock_file):
            brand, parking_name = self.manager.find_car_by_plate('XYZ000')
            self.assertEqual((brand, parking_name), (None, None))

    def test_cleaning(self):
            current_directory = os.path.dirname(os.path.abspath(__file__))
            folder_path = os.path.join(current_directory, "parkings", "TestParking")
            
            try:
                shutil.rmtree(folder_path)
                print("Test folder deleted")
            except Exception as e:
                print("ERROR", e)

if __name__ == '__main__':
    unittest.main()
