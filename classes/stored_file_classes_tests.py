import platform
import random
import unittest
import os
from classes.stored_file_classes import StoredFileContainer
from utils.file_utils import create_temp_dir, remove_temp_dir


class TestStoredFileContainer(unittest.TestCase):

    def test_block_files(self):
        if platform.system() == 'Linux':
            temporary_folder = create_temp_dir()
            blocked_files_list = []
            unblocked_files_list = []
            random_file_names = ['block_file.txt', 'unblocked_file.txt']
            try:
                for i in range(100):
                    random_file_name = random.choice(random_file_names)
                    if random_file_name == 'block_file.txt':
                        blocked_file_name = os.path.join(temporary_folder, str(i).join('block_file.txt'))
                        blocked_file = open(blocked_file_name, mode='w')
                        blocked_file.write('Some contents')
                        blocked_files_list.append(blocked_file_name)
                    else:
                        unblocked_file_name = os.path.join(temporary_folder, str(i).join('unblocked_file.txt'))
                        unblocked_file = open(unblocked_file_name, mode='w')
                        unblocked_file.write('Some contents')
                        unblocked_file.close()
                        unblocked_file = open(unblocked_file_name, mode='r')
                        _contents = unblocked_file.read()
                        unblocked_files_list.append(unblocked_file_name)
                stored_file_container_obj = StoredFileContainer(temporary_folder)
                self.assertEqual(len(unblocked_files_list), len(stored_file_container_obj.get_unlocked_files))
            finally:
                for any_file in blocked_files_list:
                    with open(any_file) as file_txt:
                        file_txt.close()
                for any_file in unblocked_files_list:
                    with open(any_file) as file_txt:
                        file_txt.close()
                remove_temp_dir(temporary_folder)
