import subprocess
import codecs


class CryptFile:

    def __init__(self):
        pass

    def encrypt_file(self, command):
        pass


cmd = r'C:\\Users\ksenofontov_d\cryptcp -encr -f "C:\\Users\ksenofontov_d\cert_1.p7b" C:\\Users\ksenofontov_d\test.txt C:\\Users\ksenofontov_d\PycharmProjects\pythonProject\exp\result.txt'
with open(r'C:\\Users\ksenofontov_d\PycharmProjects\pythonProject\exp\result.txt', 'w', encoding='utf8') as f:
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
print(result.stdout.decode("oem"))
f = codecs.open(r'C:\\Users\ksenofontov_d\PycharmProjects\pythonProject\exp\result.txt', 'r', 'oem')
u = f.read()
out = codecs.open(r'C:\\Users\ksenofontov_d\PycharmProjects\pythonProject\exp\result.txt', 'w', 'utf-8')
out.write(u)
