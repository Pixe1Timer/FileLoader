import os
import typing
from stored_file_classes import StoredFile, StoredFileContainer


class BankCertificateFile(StoredFile):

    def __init__(self, file_path: str, file_name: str):
        super().__init__(file_path, file_name)

    def get_certificate_values(self):
        super().get_certificate_values()


class BankCertificatesContainer(StoredFileContainer):

    CertificateFile: typing.Type[BankCertificateFile]
    CertificateFile = BankCertificateFile

    def __init__(self, file_directory: str):
        super().__init__(file_directory)

    def get_available_certificates(self) -> typing.Iterable[BankCertificateFile]:
        pass
