import unittest
import os
from classes.bank_certificates_classes import BankCertificatesContainer, BankCertificateFile
from utils.file_utils import create_temp_dir, remove_temp_dir


def create_new_file(file_dir, any_file_name):
    full_any_file_dir = os.path.join(file_dir, any_file_name)
    any_file = open(full_any_file_dir, mode='w')
    any_file.write('Some comment')
    any_file.close()
    return any_file


class TestBankCertificateFile(unittest.TestCase):

    certificates_list = [
        'dddddd',  # False
        '0648.11111111111.20220923174555.zzz',  # False
        '0646.11111111111.20241323174555.cer',  # False
        '0646.11111111111.202413231745.cer',  # False
        '8754.11111111111.2021z812143545.cer',  # False
        '0647.11111111111.20220923174555.del',  # True
        '0646.11111111111.20220923174555.cer',  # True
        '0645.11111111111.20220923174555.cer',  # True
    ]

    def test_certificates_container(self):
        full_file_paths_list = []
        temporary_folder = create_temp_dir()
        try:
            for certificate in self.certificates_list:
                new_certificate_file = create_new_file(temporary_folder, certificate)
                full_file_paths_list.append(new_certificate_file)
            bank_certificates_container_obj = BankCertificatesContainer(temporary_folder)
            self.assertEqual(len(bank_certificates_container_obj.get_certificates_list()), 3)
        finally:
            for any_file_path in full_file_paths_list:
                any_file_path.close()
            remove_temp_dir(temporary_folder)

    def test_certificate_file(self):
        full_file_paths_list = []
        temporary_folder = create_temp_dir()
        try:
            for count, certificate in enumerate(self.certificates_list):
                new_certificate_file = create_new_file(temporary_folder, certificate)
                full_file_paths_list.append(new_certificate_file)
                bank_certificate_file_obj = BankCertificateFile(temporary_folder, certificate)
                (self.assertFalse if count < 5 else self.assertTrue)(bank_certificate_file_obj.is_valid)
        finally:
            remove_temp_dir(temporary_folder)
