import subprocess


class FileExec:
    def __init__(self, *args):
        self.params = args

    def exec(self):
        file_list = []
        file_list.extend([value for value in self.params])
        with open(r'C:\Users\ksenofontov_d\PycharmProjects\pythonProject\exp\result.txt', 'w', encoding='utf8'):
            result = subprocess.run(file_list, stdout=subprocess.PIPE, shell=True, cwd=r'C:/Users/ksenofontov_d')
            print(result.stdout.decode("oem"))


class EncryptExec:
    def __init__(self, cert, msg_to_code, coded_msg):
        self.file = 'cryptcp.exe'
        self.code = '-encr'
        self.param = r'-f'
        self.cert = cert
        self.msg_to_code = msg_to_code
        self.coded_msg = coded_msg
        self.exec_encr()

    def exec_encr(self):
        encr_obj = FileExec(self.file, self.code, self.param, self.cert, self.msg_to_code, self.coded_msg)
        encr_obj.exec()


class DecryptExec:
    def __init__(self, cert, msg_to_code, coded_msg):
        self.file = 'cryptcp.exe'
        self.code = '-decr'
        self.param = '-start'
        self.cert = cert
        self.msg_to_decode = msg_to_code
        self.decoded_msg = coded_msg
        self.exec_decr()

    def exec_decr(self):
        decr_obj = FileExec(self.file, self.code, self.cert, self.msg_to_decode, self.decoded_msg)
        decr_obj.exec()

"""""""""
class SetSignatureExec:
    def exec_set_signature(self):
        set_obj = FileExec()
        set_obj.exec()


class UnsetSignatureExec:
    def exec_unset_signature(self):
        unset_obj = FileExec()
        unset_obj.exec()

"""""""""

certificate = r'cert_1.p7b'
message_to_code = r'test.txt'
coded_message = r'result.txt'
message_to_decode = r'result.txt'
decoded_message = r'test.txt'
decr_exec = DecryptExec(certificate, message_to_code, coded_message)
