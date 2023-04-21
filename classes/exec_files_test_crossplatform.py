from exec_files import EncryptExec, DecryptExec, SetSignatureExec, UnsetSignatureExec
import unittest
import os
import platform


class ExecFilesTestCaseWin(unittest.TestCase):
    if platform.system() == 'Windows':
        path_exe = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            r'cryptcp_exec')
    elif platform.system() == 'Linux':
        path_exe = r'/opt/cprocsp/bin/amd64/'
    else:
        print('Unknown platform!')

    def test_encrypt(self):
        certificate = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            r'cryptcp_exec/cert_1.p7b')
        message_to_code = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            r'cryptcp_exec/test.txt')
        coded_message = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            r'cryptcp_exec/result.txt')
        encr_exec = EncryptExec(
            certificate,
            message_to_code,
            coded_message,
            self.path_exe
        )
        self.assertEqual(encr_exec.cert, certificate)
        self.assertEqual(encr_exec.msg_to_code, message_to_code)
        self.assertEqual(encr_exec.coded_msg, coded_message)
        print(f'Код выполнения:{encr_exec.output[0]},\nВывод:{encr_exec.output[1]}')

    def test_decrypt(self):
        message_to_decode = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            r'cryptcp_exec/to_decode.txt')
        decoded_message = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            r'cryptcp_exec/decoded.txt')
        container = r'CN=Denis'
        pin_param = r'-pin'
        passphrase = r'Denis'
        decr_exec = DecryptExec(
            container,
            pin_param,
            passphrase,
            message_to_decode,
            decoded_message,
            self.path_exe)
        self.assertEqual(decr_exec.msg_to_decode, message_to_decode)
        self.assertEqual(decr_exec.decoded_msg, decoded_message)
        self.assertEqual(decr_exec.cont, container)
        print(f'Код выполнения:{decr_exec.output[0]},\nВывод:{decr_exec.output[1]}')

    def test_sign(self):
        container = r'CN=Denis'
        sign_file = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            r'cryptcp_exec/sign.txt')
        pin_param = r'-pin'
        passphrase = r'Denis'
        sign_exec = SetSignatureExec(
            container,
            pin_param,
            passphrase,
            sign_file,
            self.path_exe
        )
        self.assertEqual(sign_exec.cert, container)
        self.assertEqual(sign_exec.file_to_sign, sign_file)
        print(f'Код выполнения:{sign_exec.output[0]},\nВывод:{sign_exec.output[1]}')

    def test_unsign(self):
        signed_f = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            r'cryptcp_exec/sign.txt.sig')
        unsigned_f = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            r'cryptcp_exec/unsigned.txt')
        unsign_exec = UnsetSignatureExec(
            signed_f,
            unsigned_f,
            self.path_exe
        )
        self.assertEqual(unsign_exec.signed_file, signed_f)
        self.assertEqual(unsign_exec.unsigned_file, unsigned_f)
        print(f'Код выполнения:{unsign_exec.output[0]},\nВывод:{unsign_exec.output[1]}')
