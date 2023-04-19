from stored_file_classes import StoredFile, StoredFileContainer
import datetime
import typing


def end_date_check(certificate_date: str) -> bool:
    if len(certificate_date) == 14:
        try:
            bool(datetime.datetime.strptime(certificate_date, '%Y%m%d%H%M%S'))
        except ValueError:
            return False
        return True
    else:
        return False


class BankCertificateFile(StoredFile):
    bank_code: str
    snils: str
    end_date: datetime.datetime
    certificate_condition: str

    def __init__(self, file_path: str, file_name: str):
        super().__init__(file_path, file_name)

    def certificate_name_parse(self, file_title: str) -> str:
        self.file_name = file_title
        splited_file_name = self.file_name.split('.')
        if len(splited_file_name) == 4:
            if end_date_check(splited_file_name[2]):
                self.bank_code = splited_file_name[0]
                self.snils = splited_file_name[1]
                self.end_date = datetime.datetime.strptime(splited_file_name[2], '%Y%m%d%H%M%S')
                self.certificate_condition = splited_file_name[3]
                try:
                    assert len(self.bank_code) == 4, f'{file_title} - Неверный код банка'
                    assert len(self.snils) == 11, f'{file_title} - Неверный СНИЛС'
                    assert self.certificate_condition == 'cer' \
                           or self.certificate_condition == 'del', f'{file_title} - Файл не является сертификатом'
                except AssertionError as a:
                    return str(a)
                return (
                    ' Код банка: {}\n СНИЛС: {}\n Срок окончания сертификата: {}\n Состояние сертификата: {}'.
                    format(self.bank_code, self.snils, self.end_date, self.certificate_condition))
            else:
                return f'{self.file_name} - Неверный формат даты'
        else:
            return f'{self.file_name} - Имя файла не соответствует имени сертификата'


class BankCertificatesContainer(StoredFileContainer):
    path_class: typing.Type[BankCertificateFile]
    path_class = BankCertificateFile

    def get_certificates_list(self) -> list[str]:
        certificates_list = []
        for certificate in self.files_list:
            certificates_list.append(certificate.get_full_file_name)
        return certificates_list
