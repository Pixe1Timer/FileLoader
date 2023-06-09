from __future__ import annotations
import os
import shutil
from typing import TextIO, List


class tempFileCreator:

    def __init__(self, file_content: List[str], file_path: str):
        """Конструктор класса tempFileCreator.

        Аргументы:
        file_content -- список строк, содержащих данные для файла
        file_path -- путь к файлу

        """
        dirname, filename = self.extract_dirname_filename(file_path)
        self.test_data = '\n'.join(file_content)
        self.dirname = dirname
        self.filename = filename
        self.dir_full_path = self.create_temp_dir(self.dirname)
        self.file_obj = self.create_temp_file(self.filename)
        self.fill_temp_file_with_data()

    def extract_dirname_filename(self, path_str: str) -> (str, str):
        """Метод extract_dirname_filename получает путь к файлу и разделяет его на путь до директории
        и имя файла.

        Аргументы:
        path -- путь к файлу.

        Возвращает пару значений: имя директории и имя файла.

        """
        normalize_path = os.path.normpath(path_str)
        filename = os.path.basename(normalize_path)
        dirname = os.path.dirname(normalize_path)
    
        return dirname, filename

    def create_temp_dir(self, dirname: str = "temp") -> str:
        """Метод create_temp_dir создает директорию с именем dirname в текущей директории или возвращает
        существующую.

        Аргументы:
        dirname -- имя директории (по умолчанию: "temp").

        Возвращает строку с путем к директории.

        """
        current_dir = os.getcwd()
        full_path = os.path.join(current_dir, dirname)

        if os.path.exists(full_path):
            return full_path

        os.mkdir(full_path)
        return full_path

    def create_temp_file(self, filename="temp_file.txt") -> TextIO:
        """Метод create_temp_file создает временный файл с именем filename
        и возвращает объект TextIO для записи в него данных.

        Аргументы:
        filename -- имя временного файла (по умолчанию: "temp_file.txt").

        Возвращает объект TextIO.

        """
        full_file_path = os.path.join(self.dir_full_path, filename)
        file = open(full_file_path, 'w')
        return file

    def fill_temp_file_with_data(self):
        """Метод fill_temp_file_with_data записывает данные из атрибута self.test_data в созданный временный файл."""
        self.file_obj.write(self.test_data)
        self.file_obj.close()

    def purge(self):
        """Метод purge удаляет созданную временную директорию с файлами.

        Вызывает исключение ValueError, если путь к директории начинается не со значения функции getcwd()
        плюс поддиректория temp.

        """
        remove_temp_dir(self.dir_full_path)
