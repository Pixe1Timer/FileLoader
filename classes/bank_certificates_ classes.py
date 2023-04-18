from stored_file_classes import StoredFile, StoredFileContainer
import datetime
import typing
import os


class BankCertificateFile(StoredFile):

    bank_code: str
    snils: str
    date_and_time: datetime.datetime
    certificate_condition: str

    def __init__(self, file_path: str, file_name: str):
        super().__init__(file_path, file_name)

    def get_certificate_values(self) -> list[str]:
        splited_file_name = self.file_name.split('.')
        self.bank_code = splited_file_name[0]
        self.snils = splited_file_name[1]
        self.date_and_time = datetime.datetime.strptime(splited_file_name[2], '%Y%m%d%H%M%S')
        self.certificate_condition = splited_file_name[3]
        return splited_file_name

    def __str__(self):
        super().__str__()

    def get_full_file_name(self):
        super().get_full_file_name()


class BankCertificatesContainer(StoredFileContainer):

    CertificateFile: typing.Type[BankCertificateFile]
    CertificateFile = BankCertificateFile

    def __init__(self, file_directory: str):
        super().__init__(file_directory)

    def get_available_certificates(self) -> list[str]:
        certificates_list = []
        for certificate in self.files_list:
            certificate_name = os.path.basename(certificate.get_full_file_name)
            certificate_dir = os.path.dirname(certificate.get_full_file_name)
            bcf = BankCertificateFile(certificate_dir, certificate_name)
            if len(bcf.get_certificate_values()) == 4:
                if bcf.certificate_condition == 'cer':
                    certificates_list.append(certificate.get_full_file_name)
                else:
                    pass
            else:
                pass
        return certificates_list
