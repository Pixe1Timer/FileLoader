import subprocess


class FileExec:
    def __init__(self, *args):
        self.path = args[0]
        self.params = args[1:]

    def exec(self):
        """
        Функция для выполнения файлов с передаваемыми параметрами в командной строке, возвращает кортеж из двух
        элементов: кода выполнения команды и вывода
        """
        file_list = []
        file_list.extend([value for value in self.params])
        result = subprocess.run(file_list, stdout=subprocess.PIPE, shell=True, cwd=self.path,
                                stderr=subprocess.STDOUT)
        decoded_out = result.stdout.decode("oem")
        decoded_out.splitlines()
        return result.returncode, decoded_out


class EncryptExec:
    def __init__(self, path: str, cert: str, msg_to_code: str, coded_msg: str):
        self.file = 'cryptcp.exe'
        self.code = '-encr'
        self.param = r'-f'
        self.cert = cert
        self.msg_to_code = msg_to_code
        self.coded_msg = coded_msg
        self.path = path
        self.output = self.exec_encr()

    def exec_encr(self):
        """
        Функция создает экземпляр класса FileExec с параметрами, которые выполняют шифрование файла
        с помощью программы cryptcp
        """
        encr_obj = FileExec(self.path, self.file, self.code, self.param, self.cert, self.msg_to_code, self.coded_msg)
        exec_out = encr_obj.exec()
        return exec_out


class DecryptExec:
    def __init__(self, path: str, cont: str, msg_to_decode: str, decoded_msg: str):
        self.file = 'cryptcp.exe'
        self.code = '-decr'
        self.param = '-dn'
        self.cont = cont
        self.msg_to_decode = msg_to_decode
        self.decoded_msg = decoded_msg
        self.path = path
        self.output = self.exec_decr()

    def exec_decr(self):
        """
        Функция создает экземпляр класса FileExec с параметрами, которые выполняют дешифрование файла
        с помощью программы cryptcp
        """
        decr_obj = FileExec(self.path, self.file, self.code, self.param,
                            self.cont, self.msg_to_decode, self.decoded_msg)
        decr_out = decr_obj.exec()
        return decr_out


class SetSignatureExec:
    def __init__(self, path: str, cert: str, file_to_sign: str):
        self.file = 'cryptcp.exe'
        self.code = '-sign'
        self.param = '-dn'
        self.cert = cert
        self.file_to_sign = file_to_sign
        self.path = path
        self.output = self.exec_set_signature()

    def exec_set_signature(self):
        """
        Функция создает экземпляр класса FileExec с параметрами, которые создают ЭЦП файла
        с помощью программы cryptcp
        """
        set_obj = FileExec(self.path, self.file, self.code, self.param, self.cert, self.file_to_sign)
        set_out = set_obj.exec()
        return set_out


class UnsetSignatureExec:
    def __init__(self, path: str, signed_file: str, unsigned_file: str):
        self.file = 'cryptcp.exe'
        self.code = '-verify'
        self.signed_file = signed_file
        self.unsigned_file = unsigned_file
        self.path = path
        self.output = self.exec_unset_signature()

    def exec_unset_signature(self):
        """
        Функция создает экземпляр класса FileExec с параметрами, которые снимают ЭЦП с файла
        с помощью программы cryptcp
        """
        unset_obj = FileExec(self.path, self.file, self.code, self.signed_file, self.unsigned_file)
        unset_out = unset_obj.exec()
        return unset_out
