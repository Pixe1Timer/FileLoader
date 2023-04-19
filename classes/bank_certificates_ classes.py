from stored_file_classes import StoredFile, StoredFileContainer
import datetime
import typing


class BankCertificateFile(StoredFile):
    bank_code: str
    snils: str
    end_date: datetime.datetime
    certificate_condition: str
    is_valid: bool

    def __init__(self, file_path: str, file_name: str):
        super().__init__(file_path, file_name)
        self.is_valid, self.error_str = self.certificate_name_parse()

    def certificate_name_parse(self) -> (bool, str):
        splited_file_name = self.file_name.split('.')
        if len(splited_file_name) == 4:
            self.bank_code = splited_file_name[0]
            self.snils = splited_file_name[1]
            if len(splited_file_name[2]) == 14:
                try:
                    self.end_date = datetime.datetime.strptime(splited_file_name[2], '%Y%m%d%H%M%S')
                except ValueError:
                    return False, f'Неверный формат даты'
            else:
                return False, f'Неверный формат даты'
            self.certificate_condition = splited_file_name[3]
            try:
                assert len(self.bank_code) == 4, f'Неверный код банка'
                assert len(self.snils) == 11, f'Неверный СНИЛС'
                assert self.certificate_condition == 'cer' \
                       or self.certificate_condition == 'del', f'Файл не является сертификатом'
            except AssertionError as a:
                return False, str(a)
            return True, (
                ' Код банка: {}; СНИЛС: {}; Срок окончания сертификата: {}; Состояние сертификата: {}'.
                format(self.bank_code, self.snils, self.end_date, self.certificate_condition))
        else:
            return False, f'{self.file_name} - Имя файла не соответствует имени сертификата'


class BankCertificatesContainer(StoredFileContainer):
    path_class: typing.Type[BankCertificateFile]
    path_class = BankCertificateFile

    def get_certificates_list(self) -> list[str]:
        certificates_list = []
        for certificate in self.files_list:
            if certificate.is_valid:
                certificates_list.append(certificate.get_full_file_name)
        return certificates_list
