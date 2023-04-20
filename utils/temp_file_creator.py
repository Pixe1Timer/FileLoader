from __future__ import annotations
import os
import shutil
from typing import TextIO, List


class tempFileCreator:
    def __init__(self, file_content: List[str], file_path: str):
        dirname, filename = self.extract_dirname_filename(file_path)
        self.test_data = '\n'.join(file_content)
        self.dirname = dirname
        self.filename = filename
        self.dir_full_path = self.create_temp_dir(self.dirname)
        self.file = self.create_temp_file(self.filename)
        self.fill_temp_file_with_data()

    def extract_dirname_filename(self, path: str) -> (str, str):
        dir_and_file_arr = path.split('/')
        dirname = dir_and_file_arr[0]
        filename = dir_and_file_arr[1]
        return dirname, filename

    def create_temp_dir(self, dirname: str = "temp") -> str:
        current_dir = os.getcwd()
        full_path = os.path.join(current_dir, dirname)

        if os.path.exists(full_path):
            return full_path

        os.mkdir(full_path)
        return full_path

    def create_temp_file(self, filename="temp_file.txt") -> TextIO:
        full_file_path = os.path.join(self.dir_full_path, filename)
        file = open(full_file_path, 'w')
        return file

    def fill_temp_file_with_data(self):
        self.file.write(self.test_data)
        self.file.close()

    def purge(self):
        shutil.rmtree(self.dir_full_path)
