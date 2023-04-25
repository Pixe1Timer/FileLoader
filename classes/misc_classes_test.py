# Unit тесты для misc_classes
import platform
import unittest
import os
from classes.misc_classes import BlockedFilesDetector
from utils.file_utils import create_temp_dir, remove_temp_dir


class TestBlockFilesDetector(unittest.TestCase):
    """
    Unit test для тестирования компоненты unblocked_file_name
    """
    def test_block_files(self):
        if platform.system() == 'Linux':
            # Создать временную папку
            temporary_dir = create_temp_dir()
            blocked_file = None
            unblocked_file = None
            try:
                # Создать файл с блокировкой
                blocked_file_name = os.path.join(temporary_dir, 'block_file.txt')
                blocked_file = open(blocked_file_name, mode='w')
                blocked_file.write('Some contents')
                # Создать файл без блокировки
                unblocked_file_name = os.path.join(temporary_dir, 'unblocked_file.txt')
                unblocked_file = open(unblocked_file_name, mode='w')
                unblocked_file.write('Some contents')
                unblocked_file.close()
                unblocked_file = open(unblocked_file_name, mode='r')
                _contents = unblocked_file.read()
                block_files_det_obj = BlockedFilesDetector()
                self.assertTrue(block_files_det_obj.file_is_locked(blocked_file_name))
                self.assertFalse(block_files_det_obj.file_is_locked(unblocked_file_name))
            finally:
                # Закрыть файлы
                if blocked_file:
                    blocked_file.close()
                if unblocked_file:
                    unblocked_file.close()
                # Удалить временную папку
                remove_temp_dir(temporary_dir)
