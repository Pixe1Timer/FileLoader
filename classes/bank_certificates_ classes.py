from stored_file_classes import StoredFile, StoredFileContainer
import datetime
import typing


class BankCertificateFile(StoredFile):
    bank_code: str
    snils: str
    end_date: datetime.datetime
    certificate_condition: str

    def __init__(self, file_path: str, file_name: str):
        super().__init__(file_path, file_name)
        self.is_valid, self.error_str = self.is_valid_values(self.file_name, self.file_path)
        if self.is_valid:
            self.get_certificate_values()

    def is_valid_values(self, file_title: str, file_base_dir: str) -> (bool, str):
        self.file_name = file_title
        self.file_path = file_base_dir
        try:
            assert len(self.file_name) < 0, 'Имя файла не может быть пустым'
            assert len(self.file_path) < 0, 'Путь до файла не может быть пустым'
        except AssertionError as a:
            return False, str(a)
        return True

    def get_certificate_values(self) -> str:
        splited_file_name = self.file_name.split('.')
        if len(splited_file_name) == 4:
            self.bank_code = splited_file_name[0]
            self.snils = splited_file_name[1]
            self.end_date = datetime.datetime.strptime(splited_file_name[2], '%Y%m%d%H%M%S')
            self.certificate_condition = splited_file_name[3]
            try:
                assert self.certificate_condition == 'cer' \
                       or self.certificate_condition == 'del', 'Файл не является сертификатом'
            except AssertionError as a:
                return str(a)
            return (
                ' Код банка: {}\n СНИЛС: {}\n Срок окончания сертификата: {}\n Состояние сертификата: {}'.
                format(self.bank_code, self.snils, self.end_date, self.certificate_condition))
        else:
            return 'Имя файла не соответствует имени сертификата'


class BankCertificatesContainer(StoredFileContainer):
    path_class: typing.Type[BankCertificateFile]
    path_class = BankCertificateFile

    def get_available_certificates(self) -> list[str]:
        certificates_list = []
        for certificate in self.files_list:
            certificates_list.append(certificate.get_full_file_name)
        return certificates_list
