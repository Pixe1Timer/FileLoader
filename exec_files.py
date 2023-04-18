import subprocess


class FileExec:
    def __init__(self, *args):
        self.params = args

    def exec(self):
        file_list = []
        file_list.extend([value for value in self.params])
        result = subprocess.run(file_list, stdout=subprocess.PIPE, shell=True, cwd=r'C:/Users/ksenofontov_d',
                                stderr=subprocess.STDOUT)
        if result.returncode != 0:
            raise Exception(f'Invalid result: {result.returncode}')
        result.stdout.decode("oem")


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
    def __init__(self, cont, msg_to_decode, decoded_msg):
        self.file = 'cryptcp.exe'
        self.code = '-decr'
        self.param = '-dn'
        self.cont = cont
        self.msg_to_decode = msg_to_decode
        self.decoded_msg = decoded_msg
        self.exec_decr()

    def exec_decr(self):
        decr_obj = FileExec(self.file, self.code, self.param, self.cont, self.msg_to_decode, self.decoded_msg)
        decr_obj.exec()


class SetSignatureExec:
    def __init__(self, cert, file_to_sign):
        self.file = 'cryptcp.exe'
        self.code = '-sign'
        self.param = '-dn'
        self.cert = cert
        self.file_to_sign = file_to_sign
        self.exec_set_signature()

    def exec_set_signature(self):
        set_obj = FileExec(self.file, self.code, self.param, self.cert, self.file_to_sign)
        set_obj.exec()


class UnsetSignatureExec:
    def __init__(self, signed_file, unsigned_file):
        self.file = 'cryptcp.exe'
        self.code = '-verify'
        self.signed_file = signed_file
        self.unsigned_file = unsigned_file
        self.exec_unset_signature()

    def exec_unset_signature(self):
        unset_obj = FileExec(self.file, self.code, self.signed_file, self.unsigned_file)
        unset_obj.exec()


certificate = r'cert_1.p7b'
message_to_code = r'test.txt'
coded_message = r'result.txt'
message_to_decode = r'to_decode.txt'
decoded_message = r'decoded.txt'
container = r'CN=Denis'
sign_file = r'sign.txt'
signed_f = r'sign.txt.sig'
unsigned_f = r'sign_new.txt'
encr_exec = EncryptExec(certificate, message_to_code, coded_message)
decr_exec = DecryptExec(container, message_to_decode, decoded_message)
sign_exec = SetSignatureExec(container, sign_file)
unsign_exec = UnsetSignatureExec(signed_f, unsigned_f)
