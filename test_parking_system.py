import unittest, os
from car_manager import TextCarManager
from unittest.mock import patch, MagicMock, mock_open, call
from main_menu_functions import Main_menu_services

class TestParkingSystem(unittest.TestCase):

    def setUp(self):
        """Настройка окружения перед каждым тестом."""
        self.menu_services = Main_menu_services()
        self.license_plate = 'ABC123'
        self.brand = 'Toyota'
        self.manager = TextCarManager('parkings/TestParking')
        #---------------
        self.storage_dir = 'parkings/TestParking'
        self.manager = TextCarManager(self.storage_dir)

    @patch('builtins.input', return_value='TestParking')
    @patch('os.makedirs')
    @patch('os.path.exists', return_value=False)
    def test_create_parking(self, mock_exists, mock_makedirs, mock_input):
        """Тестирование создания новой парковки."""
        self.menu_services.create_parking()
        mock_makedirs.assert_called_once_with(os.path.join('parkings', 'TestParking'))

    @patch('builtins.input', return_value='TestParking')
    @patch('os.path.exists', return_value=True)
    def test_select_parking(self, mock_exists, mock_input):
        """Тестирование выбора существующей парковки."""
        parking_name, manager = self.menu_services.select_parking()
        self.assertEqual(parking_name, 'TestParking')
        self.assertIsNotNone(manager)
        mock_input.assert_called_once()

    @patch('builtins.input', return_value='ABC123')
    def test_search_car(self, mock_input):
        """Тестирование поиска автомобиля по номерному знаку."""
        with patch.object(TextCarManager, 'find_car_by_plate', return_value=('Toyota', 'TestParking')) as mock_find:
            brand, parking_name = self.menu_services.search_car()
            self.assertEqual(brand, 'Toyota')
            self.assertEqual(parking_name, 'TestParking')
            mock_find.assert_called_once_with('ABC123')
            mock_input.assert_called_once()

    @patch('builtins.input', return_value='TestParking')
    @patch('os.path.exists', return_value=True)
    @patch('os.rmdir')
    @patch('os.listdir', return_value=[])
    @patch('os.remove')
    def test_delete_parking(self, mock_remove, mock_listdir, mock_rmdir, mock_exists, mock_input):
        """Тестирование удаления парковки."""
        self.menu_services.delete_parking()
        mock_rmdir.assert_called_once_with(os.path.join('parkings', 'TestParking'))
        mock_input.assert_called_once()

  #-----------------------------------
        
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.join')
    def test_add_car(self, mock_path_join, mock_file_open):
        """Тестирование добавления автомобиля."""
        # Путь, который должен быть создан для нового файла автомобиля.
        file_path = os.path.join('parkings/TestParking', f'{self.license_plate}.txt')
        mock_path_join.return_value = file_path

        # Действие: добавляем новый автомобиль.
        self.manager.add_car(self.license_plate, self.brand)

        # Проверяем, что файл был попытан открыть для записи.
        mock_file_open.assert_called_once_with(file_path, 'w')
        # Проверяем, что правильная информация была записана в файл.
        mock_file_open().write.assert_called_once_with(f'{self.license_plate}, {self.brand}\n')
    
    @patch('os.path.join')
    @patch('os.path.exists', return_value=True)
    @patch('os.remove')
    def test_remove_car(self, mock_remove, mock_exists, mock_path_join):
        """Тестирование удаления автомобиля."""
        # Путь к файлу автомобиля, который будет удален.
        file_path = os.path.join('parkings/TestParking', f'{self.license_plate}.txt')
        mock_path_join.return_value = file_path

        # Действие: удаляем автомобиль.
        self.manager.remove_car(self.license_plate)

        # Проверяем, что была сделана попытка удалить файл.
        mock_remove.assert_called_once_with(file_path)

    #-----------------------------------
    filePath = "/parkings/Testparking"
    os.rmdir(filePath)
if __name__ == '__main__':
    unittest.main()
