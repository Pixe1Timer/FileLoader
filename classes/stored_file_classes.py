import os
from typing import Iterable

from classes.misc_classes import BlockedFilesDetector


class StoredFile:

    def __init__(self, file_path: str, file_name: str):
        self.file_path = file_path
        self.file_name = file_name

    def __str__(self):
        return str(self.get_full_file_name)

    @property
    def get_full_file_name(self):
        return os.path.join(self.file_path, self.file_name)


class StoredFileContainer:

    def __init__(self, file_directory: str):
        self.file_directory = file_directory
        self.files_list = []
        for files_instance in os.listdir(file_directory):
            self.files_list.append(StoredFile(file_directory, files_instance))

    def get_unlocked_files(self):
        unlocked_files_list = []
        block_files_det_obj = BlockedFilesDetector()
        for full_file_directory in self.files_list:
            if not block_files_det_obj.file_is_locked(full_file_directory.get_full_file_name):
                unlocked_files_list.append(full_file_directory.get_full_file_name)
        return unlocked_files_list


sf = StoredFile(r'/home/ubuntu/Downloads', 'PythonInstall.txt')
sfc = StoredFileContainer(sf.file_path)
print(sfc.get_unlocked_files())
