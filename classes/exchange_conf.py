import os


class ExchangeConf:
    groups_path: str
    users_path: str
    procs_path: str

    def __init__(self, conf_path):
        self.conf_path = conf_path
        self.paths_list = []
        self.names_confs = {'groups': '', 'users': '', 'procs': ''}
        self.scan_dir_for_file()

    def scan_dir_for_file(self):
        for filename in os.listdir(self.conf_path):
            if filename in self.names_confs:
                self.names_confs[filename] = os.path.abspath(filename)
        for key in self.names_confs:
            flag = True
            if self.names_confs[key] == '':
                print(f'Нет значения {key}')
                flag = False
        self.groups_path = self.names_confs['groups']
        self.users_path = self.names_confs['users']
        self.procs_path = self.names_confs['procs']
        if not flag:
            raise ValueError('Отсутствуют необходимые файлы!')
        else:
            print(
                f'Файл с группами:{self.groups_path},'
                f'\nФайл с пользователями:{self.users_path},'
                f'\nФайл с процессами {self.procs_path}'
            )


a = ExchangeConf('/home/ubuntu/PycharmProjects/exchange_conf/exp')
