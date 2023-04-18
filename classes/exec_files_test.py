from exec_files import EncryptExec, DecryptExec, SetSignatureExec, UnsetSignatureExec
import unittest


class ExecFilesTestCase(unittest.TestCase):

    def test_encrypt(self):
        certificate = r'cert_1.p7b'
        message_to_code = r'test.txt'
        coded_message = r'result.txt'
        encr_exec = EncryptExec(certificate, message_to_code, coded_message)
        self.assertEqual(encr_exec.cert, certificate)
        self.assertEqual(encr_exec.msg_to_code, message_to_code)
        self.assertEqual(encr_exec.coded_msg, coded_message)

    def test_decrypt(self):
        message_to_decode = r'to_decode.txt'
        decoded_message = r'decoded.txt'
        container = r'CN=Denis'
        decr_exec = DecryptExec(container, message_to_decode, decoded_message)
        self.assertEqual(decr_exec.msg_to_decode, message_to_decode)
        self.assertEqual(decr_exec.decoded_msg, decoded_message)
        self.assertEqual(decr_exec.cont, container)
        print(f'Return code:{decr_exec.output[0]},\nOutput:{decr_exec.output[1]}')

    def test_exception(self):
        container = r'CN=Paul'
        sign_file = r'sign.txt'
        with self.assertRaises(Exception):
            sign_exec = SetSignatureExec(container, sign_file)

    def test_sign(self):
        container = r'CN=Denis'
        sign_file = r'sign.txt'
        sign_exec = SetSignatureExec(container, sign_file)
        self.assertEqual(sign_exec.cert, container)
        self.assertEqual(sign_exec.file_to_sign, sign_file)
        print(f'Return code:{sign_exec.output[0]},\nOutput:{sign_exec.output[1]}')

    def test_unsign(self):
        signed_f = r'sign.txt.sig'
        unsigned_f = r'sign_new.txt'
        unsign_exec = UnsetSignatureExec(signed_f, unsigned_f)
        self.assertEqual(unsign_exec.signed_file, signed_f)
        self.assertEqual(unsign_exec.unsigned_file, unsigned_f)
        print(f'Return code:{unsign_exec.output[0]},\nOutput:{unsign_exec.output[1]}')
