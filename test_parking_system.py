import unittest
import os
from unittest.mock import patch, MagicMock, mock_open
from main_menu_functions import Main_menu_services
from parking_menu_functions import Parking_menu_services
from car_manager import CarManagerFactory, TextCarManager

class TestParkingSystem(unittest.TestCase):
    def setUp(self):
        """Настройка окружения перед каждым тестом."""
        self.menu_services = Main_menu_services()
        self.parking_services = Parking_menu_services()
        self.manager = TextCarManager('parkings/TestParking')

    @patch('builtins.input', side_effect=['TestParking'])
    @patch('os.makedirs')
    def test_create_parking(self, mock_makedirs, mock_input):
        """Тестирование создания новой парковки."""
        parking_dir = os.path.join('parkings', 'TestParking')
        with patch('os.path.exists', return_value=False):
            self.menu_services.create_parking()
            mock_makedirs.assert_called_once_with(parking_dir)


    @patch('builtins.input', side_effect=['TestParking'])
    def test_select_parking_existing(self, mock_input):
        """Тестирование выбора существующей парковки."""
        with patch('os.path.exists', return_value=True):
            parking_name, manager = self.menu_services.select_parking()
            self.assertEqual(parking_name, 'TestParking')
            self.assertIsInstance(manager, TextCarManager)
            mock_input.assert_called_once()

    def test_add_car(self):
        """Тестирование добавления автомобиля."""
        with patch.object(TextCarManager, 'add_car', return_value=None) as mock_add_car:
            self.manager.add_car('ABC123', 'Toyota')
            mock_add_car.assert_called_once_with('ABC123', 'Toyota')

    @patch('builtins.print')
    @patch('os.listdir', return_value=['ABC123.txt'])
    @patch('builtins.open', mock_open(read_data='ABC123, Toyota\n'))
    @patch('os.path.join', return_value='parkings/TestParking/ABC123.txt')
    def test_list_cars(self, mock_join, mock_file_open, mock_listdir, mock_print):
        """Тестирование просмотра списка автомобилей."""
        self.manager.list_cars()
        # Проверяем, что print был вызван с правильным аргументом
        mock_print.assert_called_with('ABC123, Toyota')

    @patch('builtins.input', side_effect=['ABC123'])
    def test_search_car(self, mock_input):
        """Тестирование поиска автомобиля по номерному знаку."""
        with patch.object(TextCarManager, 'find_car_by_plate', return_value=('Toyota', 'TestParking')) as mock_find:
            brand, parking = self.manager.find_car_by_plate('ABC123')
            mock_find.assert_called_once_with('ABC123')
            self.assertEqual(brand, 'Toyota')
            self.assertEqual(parking, 'TestParking')

    @patch('os.path.join')
    @patch('os.path.exists', return_value=True)
    @patch('os.remove')
    @patch('builtins.open', new_callable=mock_open, read_data='ABC123, Toyota\n')
    def test_edit_car(self, mock_file_open, mock_remove, mock_exists, mock_join):
        """Тестирование редактирования информации об автомобиле."""
        # Параметры
        old_license_plate = 'ABC123'
        new_license_plate = 'XYZ789'
        brand = 'Toyota'
        storage_dir = 'parkings/TestParking'
        old_file_path = os.path.join(storage_dir, f'{old_license_plate}.txt')
        new_file_path = os.path.join(storage_dir, f'{new_license_plate}.txt')

        # Установка моков для join и exists
        mock_join.side_effect = [old_file_path, new_file_path]
        mock_exists.return_value = True  # Предполагаем, что старый файл существует

        # Тестирование метода edit_car
        self.manager.edit_car(old_license_plate, new_license_plate, brand)

        # Проверка, что старый файл был удалён
        mock_remove.assert_called_once_with(old_file_path)
        # Проверка, что новый файл был создан с новым номерным знаком и маркой
        mock_file_open.assert_called_once_with(new_file_path, 'w')
        mock_file_open().write.assert_called_once_with(f'{new_license_plate}, {brand}\n')

    def test_remove_car(self):
        """Тестирование удаления автомобиля."""
        with patch.object(TextCarManager, 'remove_car', return_value=None) as mock_remove_car:
            self.manager.remove_car('ABC123')
            mock_remove_car.assert_called_once_with('ABC123')

    @patch('builtins.input', side_effect=['TestParking'])
    @patch('os.rmdir')
    @patch('os.remove')
    def test_delete_parking_existing(self, mock_remove, mock_rmdir, mock_input):
        """Тестирование удаления существующей парковки."""
        with patch('os.path.exists', return_value=True), \
            patch('os.listdir', return_value=['car1.txt', 'car2.txt']):
            self.menu_services.delete_parking()
            # Проверка, что os.remove вызывается для каждого файла в парковке
            calls = [unittest.mock.call(os.path.join('parkings', 'TestParking', 'car1.txt')),
                    unittest.mock.call(os.path.join('parkings', 'TestParking', 'car2.txt'))]
            mock_remove.assert_has_calls(calls, any_order=True)
            mock_rmdir.assert_called_once_with(os.path.join('parkings', 'TestParking'))

if __name__ == '__main__':
    unittest.main()

# python -m unittest test_parking_system.py
