import subprocess
import codecs


class FileExec:

    def __init__(self, file, *args):
        self.file = file
        self.params = args

    def exec_file_params(self):
        file_list = [self.file]
        file_list.extend(self.params)
        with open(r'C:\Users\ksenofontov_d\PycharmProjects\pythonProject\exp\result.txt', 'w', encoding='utf8'):
            result = subprocess.run(file_list, stdout=subprocess.PIPE, shell=True, cwd=r'C:/Users/ksenofontov_d')
            print(result.stdout.decode("oem"))


file_path = 'cryptcp.exe'
par1 = '-encr'
par2 = r'-f'
par3 = r'cert_1.p7b'
par4 = r'test.txt'
par5 = r'result.txt'
dir_exec = FileExec(file_path, par1, par2, par3, par4, par5)
dir_exec.exec_file_params()
