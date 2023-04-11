import os
from classes.misc_classes import BlockedFilesDetector


class StoredFile:

    def __init__(self, file_path: str, file_name: str):
        self.file_path = file_path
        self.file_name = file_name

    def __str__(self):
        return str(self.file_path)

    @property
    def full_file_name(self):
        return os.path.join(self.file_path, self.file_name)


class StoredFileContainer:

    def __init__(self, file_directory: str):
        self.file_directory = file_directory
        self.paths_list = []
        files_list = os.listdir(file_directory)
        for file in files_list:
            self.paths_list.append(StoredFile(file_directory, file))

    def unlocked_files(self):
        unlocked_files_list = []
        block_files_det_obj = BlockedFilesDetector()
        for one_file_path in self.paths_list:
            if not block_files_det_obj.file_is_locked(one_file_path.full_file_name):
                unlocked_files_list.append(one_file_path.full_file_name)
        return unlocked_files_list


"""
sf = StoredFile(r'/home/ubuntu/Downloads', 'PythonInstall.txt')
sfc = StoredFileContainer(sf.file_path)
print(sfc.unlocked_files())
"""
