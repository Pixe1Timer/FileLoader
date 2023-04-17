import os
from classes.misc_classes import BlockedFilesDetector
import typing


class StoredFile:
    """
    Класс, предназначенный для хранения информации
    и статусе файла, включая данные о его блокировке.
    """
    bank_code: str
    snils: str
    date_and_time: str
    certificate_condition: str

    def __init__(self, file_path: str, file_name: str):
        """
        Конструктор класса. При создании передаются хранимые атрибуты
        :param str file_path: путь файла, без имени файла
        :param str file_name: имя файла с расширением
        """
        self.file_path = file_path
        self.file_name = file_name

    def get_certificate_values(self):
        pass

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

    @property
    def get_splited_file_name(self):
        splited_file_name = self.file_name.split('.')
        self.bank_code = splited_file_name[0]
        self.snils = splited_file_name[1]
        self.date_and_time = splited_file_name[2]
        self.certificate_condition = splited_file_name[3]
        return splited_file_name


class StoredFileContainer:
    """
    Класс, предназначенный для получения списка файлов и определения
    готовности файлов для обработки(отсутствие блокирововк на файле)
    """
    path_class: typing.Type[StoredFile]
    path_class = StoredFile

    CertificateFile: typing.Type[StoredFile]
    CertificateFile = StoredFile

    def __init__(self, file_directory: str):
        """
        Класс конструктор. Заполняет полными директориями файлов
        список для последующего использования класса
        :param str file_directory: путь файла без имени файла
        """
        self.file_directory = file_directory
        self.files_list = []
        self.certificates_list = []
        for files_instance in os.listdir(file_directory):
            self.files_list.append(self.path_class(file_directory, files_instance))
            self.certificates_list.append(self.CertificateFile(file_directory, files_instance))

    def get_unlocked_files(self) -> list[str]:
        """
        Проверить блокирован ли файл и отобрать неблокированные файлы
        :return: list[str]: список незаблокированных файлов
        """
        unlocked_files_list = []
        block_files_det_obj = BlockedFilesDetector()
        for full_file_directory in self.files_list:
            if not block_files_det_obj.file_is_locked(full_file_directory.get_full_file_name):
                unlocked_files_list.append(full_file_directory.get_full_file_name)
        return unlocked_files_list

    def make_a_choice(self, choice: str):
        self.choice = choice
        if choice == 'cer':
            self.get_available_certificates()
        elif choice == 'del':

        elif choice == 'all'

        else:
            raise ValueError('Введите "cer", "del" или "all"')

    def get_deleted_certificates(self):
        pass

    def get_available_certificates(self) -> 'typing.Iterable[StoredFile]':
        checked_certificates_list = []
        for certificate in self.certificates_list:
            splited_file_name = certificate.get_splited_file_name
            if len(splited_file_name) == 4:
                self.bank_code = splited_file_name[0]
                self.snils = splited_file_name[1]
                self.date_and_time = splited_file_name[2]
                self.certificate_condition = splited_file_name[3]
                if self.certificate_condition == 'cer':
                    checked_certificates_list.append(certificate)
#        return checked_certificates_list

    def get_all_certificates(self):
        pass
