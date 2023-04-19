import subprocess
import os


class FileExec:
    def __init__(self, *args):
        """
        :param args: передаваемые позиционные параметры
        """
        self.params = args

    def exec(self):
        """
        Функция для выполнения файлов с передаваемыми параметрами в командной строке
        :return: возвращает кортеж из двух элементов: кода выполнения команды и вывода
        """
        file_list = []
        file_list.extend([value for value in self.params])
        result = subprocess.run(file_list, stdout=subprocess.PIPE, shell=True,
                                stderr=subprocess.STDOUT)
        decoded_out = result.stdout.decode("oem")
        decoded_out.splitlines()
        return result.returncode, decoded_out


class EncryptExec:
    def __init__(self, cert: str, msg_to_code: str, coded_msg: str):
        """
        :param cert: сертификат
        :param msg_to_code: сообщение, которое нужно закодировать
        :param coded_msg: закодированное сообщение
        file: исполняемый файл
        code: код для выполнения операции шифрования
        param: параметры для выполнения файла
        """
        self.file = '../cryptcp_exec/cryptcp.exe'
        self.file_with_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.file)
        self.code = '-encr'
        self.param = r'-f'
        self.cert = cert
        self.msg_to_code = msg_to_code
        self.coded_msg = coded_msg
        self.output = self.exec_encr()

    def exec_encr(self):
        """
        Функция создает экземпляр класса FileExec с параметрами, которые выполняют шифрование файла
        с помощью программы cryptcp
        :return: возвращает вывод подпроцесса
        """
        encr_obj = FileExec(self.file_with_path, self.code, self.param, self.cert, self.msg_to_code, self.coded_msg)
        exec_out = encr_obj.exec()
        return exec_out


class DecryptExec:
    def __init__(self, cont: str, msg_to_decode: str, decoded_msg: str):
        """
        :param cont: параметр для поиска контейнера с заданным сертификатом
        :param msg_to_decode: сообщение, которое нужно раскодировать
        :param decoded_msg: раскодированное сообщение
        file: исполняемый файл
        code: код для выполнения операции дешифрования
        param: параметры для выполнения файла
        """
        self.file = '../cryptcp_exec/cryptcp.exe'
        self.file_with_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.file)
        self.code = '-decr'
        self.param = '-dn'
        self.cont = cont
        self.msg_to_decode = msg_to_decode
        self.decoded_msg = decoded_msg
        self.output = self.exec_decr()

    def exec_decr(self):
        """
        Функция создает экземпляр класса FileExec с параметрами, которые выполняют дешифрование файла
        с помощью программы cryptcp
        :return: возвращает вывод подпроцесса
        """
        decr_obj = FileExec(self.file_with_path, self.code, self.param,
                            self.cont, self.msg_to_decode, self.decoded_msg)
        decr_out = decr_obj.exec()
        return decr_out


class SetSignatureExec:
    def __init__(self, cert: str, file_to_sign: str):
        """
        :param cert: параметр для поиска контейнера с заданным сертификатом
        :param file_to_sign: файл, которйы нужно подписать
        file: исполняемый файл
        code: код для выполнения операции подписания
        param: параметры для выполнения файла
        """
        self.file = '../cryptcp_exec/cryptcp.exe'
        self.file_with_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.file)
        self.code = '-sign'
        self.param = '-dn'
        self.cert = cert
        self.file_to_sign = file_to_sign
        self.output = self.exec_set_signature()

    def exec_set_signature(self):
        """
        Функция создает экземпляр класса FileExec с параметрами, которые создают ЭЦП файла
        с помощью программы cryptcp
        :return: возвращает вывод подпроцесса
        """
        set_obj = FileExec(self.file_with_path, self.code, self.param, self.cert, self.file_to_sign)
        set_out = set_obj.exec()
        return set_out


class UnsetSignatureExec:
    def __init__(self, signed_file: str, unsigned_file: str):
        """
        :param signed_file: сообщение, с которого надо снять подпись
        :param unsigned_file: файл, в который надо вывести текст исходного сообщения
        file: исполняемый файл
        code: код для выполнения операции снятия подписи
        param: параметры для выполнения файла
        """
        self.file = '../cryptcp_exec/cryptcp.exe'
        self.file_with_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.file)
        self.code = '-verify'
        self.signed_file = signed_file
        self.unsigned_file = unsigned_file
        self.output = self.exec_unset_signature()

    def exec_unset_signature(self):
        """
        Функция создает экземпляр класса FileExec с параметрами, которые снимают ЭЦП с файла
        с помощью программы cryptcp
        :return: возвращает вывод подпроцесса
        """
        unset_obj = FileExec(self.file_with_path, self.code, self.signed_file, self.unsigned_file)
        unset_out = unset_obj.exec()
        return unset_out
