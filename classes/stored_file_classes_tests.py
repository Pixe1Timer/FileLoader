import platform
import random
import unittest
import os
from classes.stored_file_classes import StoredFileContainer
from utils.file_utils import create_temp_dir, remove_temp_dir
import string


class TestStoredFileContainer(unittest.TestCase):

    def test_block_files(self):
        if platform.system() == 'Linux':
            temporary_folder = create_temp_dir()
            all_files_list = []
            blocked_files_list = []
            unblocked_files_list = []
            random_file_names = ['block_file.txt', 'unblocked_file.txt']
            blocked_files_number = 0
            unblocked_files_number = 0
            try:
                for i in range(100):
                    random_file_name = random.choice(random_file_names)
                    if random_file_name == 'block_file.txt':
                        blocked_files_number = blocked_files_number + 1
                        blocked_file_name = os.path.join(temporary_folder, str(blocked_files_number).join('block_file.txt'))
                        blocked_file = open(blocked_file_name, mode='w')
                        blocked_file.write('Some contents')
                        blocked_files_list.append(blocked_file_name)
                        all_files_list.append(blocked_file_name)
                    else:
                        unblocked_files_number = unblocked_files_number + 1
                        unblocked_file_name = os.path.join(temporary_folder, str(unblocked_files_number).join('unblocked_file.txt'))
                        unblocked_file = open(unblocked_file_name, mode='w')
                        unblocked_file.write('Some contents')
                        unblocked_file.close()
                        unblocked_file = open(unblocked_file_name, mode='r')
                        _contents = unblocked_file.read()
                        unblocked_files_list.append(unblocked_file_name)
                        all_files_list.append(unblocked_file_name)
                self.assertEqual(len(blocked_files_list), len())
            finally:
                for i in range(100):
                    # Закрыть файлы
                    if blocked_file:
                        blocked_file.close()
                    if unblocked_file:
                        unblocked_file.close()
                    # Удалить временную папку
                    remove_temp_dir(temporary_dir)
                    pass
