# Классы для вспомогательных функций


class FileDescriptor:
    """
    Элемент для хранения информации о файле (используется в OpenFilesDetector)
    """
    def __init__(
        self,
        process: int,
        file_name: str,
        file_descriptor: str,
        file_lock_status: str,
        access_mode: str
    ):
        """
        Конструктор класс. При создании передаются хранимые атрибуты
        :param int process: идентификатор процесса
        :param str file_name: имя файла (с путем)
        :param str file_descriptor: файловый дескриптор
        :param str file_lock_status: статус блокировки
        :param str access_mode: режим доступа (расширенный статус блокировки)
        """
        self.process = process
        self.file_name = file_name
        self.file_descriptor = file_descriptor
        self.file_lock_status = file_lock_status
        self.access_mode = access_mode

    @property
    def is_locked(self):
        """
        Статус блокировки
        :return: bool: True если на файл установлена блокировка
        """
        return self.access_mode.lower() in ('u', 'w')


class BlockedFilesDetector:
    """
    Класс для определения открытых файлов. Корректно работает на Linux
    """
    def __init__(self):
        """
        Конструктор класса. При выполнении считывается список блокировок для последующего использовании класса
        """
        from utils.file_utils import get_files_list_with_status
        self.opened_files = get_files_list_with_status()

    def file_is_locked(self, file_name: str) -> bool:
        """
        Проверить блокирован ли файл
        :param str file_name: Полный путь к файлу
        :return: bool: True если файл блокирован
        """
        for file_descriptor_obj in self.opened_files:
            if file_descriptor_obj.file_name == file_name and file_descriptor_obj.is_locked:
                return True
        return False
