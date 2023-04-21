import subprocess
import os


class FileExec:
    def __init__(self, *args):
        """
        :param args: передаваемые позиционные параметры
        """
        self.path = args[0]
        self.params = args[1:]

    def exec(self):
        """
        Функция для выполнения файлов с передаваемыми параметрами в командной строке
        :return: возвращает кортеж из двух элементов: кода выполнения команды и вывода
        """
        file_list = [self.path]
        file_list.extend([value for value in self.params])
        result = subprocess.run(file_list, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        decoded_out = result.stdout.decode("cp866")
        decoded_out.splitlines()
        return result.returncode, decoded_out


class EncryptExec:
    def __init__(self,
                 cert: str,
                 msg_to_code: str,
                 coded_msg: str,
                 path: str,
                 file_name='cryptcp'):
        """
        Класс для вызова утилиты cryptcp в режиме шифрования файла
        Атрибуты:
            cert: сертификат
            msg_to_code: сообщение, которое нужно закодировать
            coded_msg: закодированное сообщение
            file: исполняемый файл
            code: код для выполнения операции шифрования
            param: параметры для выполнения файла
        """
        self.file_with_path = os.path.join(path, file_name)
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
        encr_obj = FileExec(
            self.file_with_path,
            self.code,
            self.param,
            self.cert,
            self.msg_to_code,
            self.coded_msg
        )
        exec_out = encr_obj.exec()
        return exec_out


class DecryptExec:
    def __init__(
            self,
            cont: str,
            pin_param: str,
            passphrase: str,
            msg_to_decode: str,
            decoded_msg: str,
            path: str,
            file_name='cryptcp'
    ):
        """
        Класс для вызова утилиты cryptcp в режиме дешифрования файла
            cont: параметр для поиска контейнера с заданным сертификатом
            msg_to_decode: сообщение, которое нужно раскодировать
            decoded_msg: раскодированное сообщение
            file: исполняемый файл
            code: код для выполнения операции дешифрования
            param: параметры для выполнения файла
        """
        self.file_with_path = os.path.join(path, file_name)
        self.code = '-decr'
        self.param = '-dn'
        self.cont = cont
        self.pin_param = pin_param
        self.passphrase = passphrase
        self.msg_to_decode = msg_to_decode
        self.decoded_msg = decoded_msg
        self.output = self.exec_decr()

    def exec_decr(self):
        """
        Функция создает экземпляр класса FileExec с параметрами, которые выполняют дешифрование файла
        с помощью программы cryptcp
        :return: возвращает вывод подпроцесса
        """
        decr_obj = FileExec(
            self.file_with_path,
            self.code,
            self.param,
            self.cont,
            self.pin_param,
            self.passphrase,
            self.msg_to_decode,
            self.decoded_msg)
        decr_out = decr_obj.exec()
        return decr_out


class SetSignatureExec:
    def __init__(self,
                 cert: str,
                 pin_param: str,
                 passphrase: str,
                 file_to_sign: str,
                 path: str,
                 file_name='cryptcp'):
        """
        Класс для вызова утилиты cryptcp в режиме подписания файла
            cert: параметр для поиска контейнера с заданным сертификатом
            file_to_sign: файл, который нужно подписать
            file: исполняемый файл
            code: код для выполнения операции подписания
            param: параметры для выполнения файла
        """
        self.file_with_path = os.path.join(path, file_name)
        self.code = '-sign'
        self.param = '-dn'
        self.cert = cert
        self.pin_param = pin_param
        self.passphrase = passphrase
        self.file_to_sign = file_to_sign
        self.output = self.exec_set_signature()

    def exec_set_signature(self):
        """
        Функция создает экземпляр класса FileExec с параметрами, которые создают ЭЦП файла
        с помощью программы cryptcp
        :return: возвращает вывод подпроцесса
        """
        set_obj = FileExec(
            self.file_with_path,
            self.code,
            self.pin_param,
            self.passphrase,
            self.param,
            self.cert,
            self.file_to_sign)
        set_out = set_obj.exec()
        return set_out


class UnsetSignatureExec:
    def __init__(self,
                 signed_file: str,
                 unsigned_file: str,
                 path: str,
                 file_name='cryptcp'):
        """
        Класс для вызова утилиты cryptcp в режиме дешифрования файла
            signed_file: сообщение с которого надо снять подпись
            unsigned_file: файл, в который надо вывести текст исходного сообщения
            file: исполняемый файл
            code: код для выполнения операции снятия подписи
            param: параметры для выполнения файла
        """
        self.file_with_path = os.path.join(path, file_name)
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
        unset_obj = FileExec(
            self.file_with_path,
            self.code,
            self.signed_file,
            self.unsigned_file)
        unset_out = unset_obj.exec()
        return unset_out
