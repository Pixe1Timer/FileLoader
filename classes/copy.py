import os
from classes.misc_classes import BlockedFilesDetector


class StoredFile:
    """
    Класс, предназначенный для хранения информации
    и статусе файла, включая данные о его блокировке.
    """
    def __init__(self, file_path: str, file_name: str):
        """
        Конструктор класса. При создании передаются хранимые атрибуты
        :param str file_path: путь файла, без имени файла
        :param str file_name: имя файла с расширением
        """
        self.file_path = file_path
        self.file_name = file_name

    def __str__(self):
        """
        Строковое представление метода get_full_file_name
        :return: str: полный путь файла
        """
        return self.get_full_file_name

    @property
    def get_full_file_name(self):
        """
        Получить полный путь файла
        :return: str: объединение пути и имени файла
        """
        return os.path.join(self.file_path, self.file_name)


class StoredFileContainer(StoredFile):
    """
    Класс, предназначенный для получения списка файлов и определения
    готовности файлов для обработки(отсутствие блокирововк на файле)
    """
    def __init__(self, file_path: str, file_name: str):
        super().__init__(file_path, file_name)
        """
        Класс конструктор. Заполняет полными директориями фалов
        список для последующего использования класса
        :param str file_directory: путь файла без имени файла
        """
        self.files_list = []
        for files_instance in os.listdir(file_path):
            self.files_list.append(os.path.join(file_path, files_instance))

    def get_unlocked_files(self) -> list[str]:
        """
        Проверить блокирован ли файл и отобрать неблокированные файлы
        :return: list[str]: список незаблокированных файлов
        """
        unlocked_files_list = []
        block_files_det_obj = BlockedFilesDetector()
        for full_file_directory in self.files_list:
            if not block_files_det_obj.file_is_locked(full_file_directory):
                unlocked_files_list.append(full_file_directory)
        return unlocked_files_list


sfc = StoredFileContainer(r'/home/ubuntu/Downloads', 'PythonInstall.txt')
print(sfc.get_unlocked_files())
