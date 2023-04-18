from exec_files import EncryptExec, DecryptExec, SetSignatureExec, UnsetSignatureExec
import unittest


class ExecFilesTestCase(unittest.TestCase):

    def test_encrypt(self):
        certificate = r'cert_1.p7b'
        message_to_code = r'test.txt'
        coded_message = r'result.txt'
        path = r'C:/Users/ksenofontov_d'
        encr_exec = EncryptExec(path, certificate, message_to_code, coded_message)
        self.assertEqual(encr_exec.cert, certificate)
        self.assertEqual(encr_exec.msg_to_code, message_to_code)
        self.assertEqual(encr_exec.coded_msg, coded_message)
        print(f'Код выполнения:{encr_exec.output[0]},\nВывод:{encr_exec.output[1]}')

    def test_decrypt(self):
        message_to_decode = r'to_decode.txt'
        decoded_message = r'decoded.txt'
        container = r'CN=Denis'
        path = r'C:/Users/ksenofontov_d'
        decr_exec = DecryptExec(path, container, message_to_decode, decoded_message)
        self.assertEqual(decr_exec.msg_to_decode, message_to_decode)
        self.assertEqual(decr_exec.decoded_msg, decoded_message)
        self.assertEqual(decr_exec.cont, container)
        print(f'Код выполнения:{decr_exec.output[0]},\nВывод:{decr_exec.output[1]}')

    def test_sign(self):
        container = r'CN=Denis'
        sign_file = r'sign.txt'
        path = r'C:/Users/ksenofontov_d'
        sign_exec = SetSignatureExec(path, container, sign_file)
        self.assertEqual(sign_exec.cert, container)
        self.assertEqual(sign_exec.file_to_sign, sign_file)
        print(f'Код выполнения:{sign_exec.output[0]},\nВывод:{sign_exec.output[1]}')

    def test_unsign(self):
        signed_f = r'sign.txt.sig'
        unsigned_f = r'sign_new.txt'
        path = r'C:/Users/ksenofontov_d'
        unsign_exec = UnsetSignatureExec(path, signed_f, unsigned_f)
        self.assertEqual(unsign_exec.signed_file, signed_f)
        self.assertEqual(unsign_exec.unsigned_file, unsigned_f)
        print(f'Код выполнения:{unsign_exec.output[0]},\nВывод:{unsign_exec.output[1]}')
