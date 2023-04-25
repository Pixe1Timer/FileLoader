import os


class ExchangeConf:

    def __init__(self, conf_path):
        self.conf_path = conf_path
        self.names_confs = {'groups': '', 'users': '', 'procs': ''}
        self.scan_dir_for_file()

    def scan_dir_for_file(self):
        for key in self.names_confs:
            spec_path = os.path.join(self.conf_path, key)
            if os.path.exists(spec_path):
                self.names_confs[key] = spec_path
            else:
                raise FileNotFoundError(f'Ошибка в классе {__class__.__name__}: не найден файл {spec_path}!')
