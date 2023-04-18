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
        decoded_out = result.stdout.decode("oem")
        decoded_out.splitlines()
        return result.returncode, decoded_out


class EncryptExec:
    def __init__(self, cert, msg_to_code, coded_msg):
        self.file = 'cryptcp.exe'
        self.code = '-encr'
        self.param = r'-f'
        self.cert = cert
        self.msg_to_code = msg_to_code
        self.coded_msg = coded_msg
        self.output = self.exec_encr()

    def exec_encr(self):
        encr_obj = FileExec(self.file, self.code, self.param, self.cert, self.msg_to_code, self.coded_msg)
        exec_out = encr_obj.exec()
        return exec_out


class DecryptExec:
    def __init__(self, cont, msg_to_decode, decoded_msg):
        self.file = 'cryptcp.exe'
        self.code = '-decr'
        self.param = '-dn'
        self.cont = cont
        self.msg_to_decode = msg_to_decode
        self.decoded_msg = decoded_msg
        self.output = self.exec_decr()

    def exec_decr(self):
        decr_obj = FileExec(self.file, self.code, self.param, self.cont, self.msg_to_decode, self.decoded_msg)
        decr_out = decr_obj.exec()
        return decr_out


class SetSignatureExec:
    def __init__(self, cert, file_to_sign):
        self.file = 'cryptcp.exe'
        self.code = '-sign'
        self.param = '-dn'
        self.cert = cert
        self.file_to_sign = file_to_sign
        self.output = self.exec_set_signature()

    def exec_set_signature(self):
        set_obj = FileExec(self.file, self.code, self.param, self.cert, self.file_to_sign)
        set_out = set_obj.exec()
        return set_out


class UnsetSignatureExec:
    def __init__(self, signed_file, unsigned_file):
        self.file = 'cryptcp.exe'
        self.code = '-verify'
        self.signed_file = signed_file
        self.unsigned_file = unsigned_file
        self.output = self.exec_unset_signature()

    def exec_unset_signature(self):
        unset_obj = FileExec(self.file, self.code, self.signed_file, self.unsigned_file)
        unset_out = unset_obj.exec()
        return unset_out
