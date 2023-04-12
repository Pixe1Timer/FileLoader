from abc import ABC
import re
import typing


def check_parametrised_value(params_dict, param_value):
    """
    Функция проверяет значение передаваемых параметров.
    :param params_dict: Словарь параметров
    :param param_value: Значение параметра
    """
    attr = params_dict.get('param_name')
    if params_dict.get('param_is_string', False):
        if not type(param_value) is str:
            raise TypeError(f'Параметр {attr} должен быть строкой!')
        if params_dict.get('check_max_length', False):
            max_length = params_dict.get('max_length')
            if len(param_value) > max_length:
                raise ValueError(
                    f'Максимально допустимая длина строки для параметра: {attr} - {max_length}. '
                    f'Передано: {param_value}, длина {len(param_value)}'
                )
        if params_dict.get('mandatory_lowercase', False):
            if not param_value.islower():
                raise ValueError(f'Значение {param_value} для параметра: {attr} не в нижнем регистре!')


class BaseItem(ABC):
    """
    интерфейсный класс для хранения объектов типа Item
    """
    params_check = []

    def __init__(self, *args, **kwargs):
        """
        Конструктор класса, инициализация которого зависит от передаваемых параметров.
        :param args: позиционные аргументы
        :param kwargs: именованные аргументы
        """
        if args:
            self.args_parse(args)
        else:
            self.kwargs_parse(kwargs)

    def args_parse(self, values: typing.Tuple):
        pass

    def kwargs_parse(self, dict_values: typing.Dict):
        pass

    def is_valid_tuple(self, data_tuple: typing.Tuple):
        """
        Функция для проверки значений кортежа.
        :param data_tuple: передаваемый кортеж.
        """
        for position, param_check_value in enumerate(self.params_check):
            param_value = data_tuple[position]
            check_parametrised_value(param_check_value, param_value)

    def is_valid_dict(self, data_dict: typing.Dict):
        """
        Функция для проверки значений словаря.
        :param data_dict: передаваемый словарь.
        """
        for param_check_value in self.params_check:
            param_value = data_dict[param_check_value.get('param_name')]
            check_parametrised_value(param_check_value, param_value)


class ProcessConfig(BaseItem):
    """
    Дочерний класс для хранения информации о процессах из файла procs

    Attributes
    ----------
    process_id: str
        номера процесса
    event_handler: str
        обработчик событий
    message_id_suffix: str
        двухсимвольный идентификатор
    dir_in: str
        путь входной директории
    dir_out: str
        путь выходной директории
    """
    process_id: str
    event_handler: str
    message_id_suffix: str
    dir_in: str
    dir_out: str
    params_check = [
        {
            'param_name': 'process_id',
            'check_max_length': True,
            'max_length': 8,
            'mandatory_lowercase': True,
            'param_is_string': True
        },
        {
            'param_name': 'event_handler',
            'check_max_length': True,
            'max_length': 19,
            'mandatory_lowercase': False,
            'param_is_string': True
        },
        {
            'param_name': 'message_id_suffix',
            'check_max_length': True,
            'max_length': 2,
            'mandatory_lowercase': True,
            'param_is_string': True
        },
        {
            'param_name': 'path',
            'check_max_length': False,
            'max_length': '',
        }
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def split_path(self, path: str):
        """
        Метод разделят переменную пути и присваивает значения параметрам класса
        :param path: изначально переданный путь
        """
        splitted_path = path.split(';')
        dir_in_str = splitted_path[0]
        dir_out_str = splitted_path[1]
        if not re.match(r'DIR.IN=', dir_in_str):
            raise ValueError(f'Описание параметра {dir_in_str} не соответствует шаблону!')
        if not re.match(r'DIR.OUT=', dir_out_str):
            raise ValueError(f'Описание параметра {dir_out_str} не соответствует шаблону!')
        self.dir_in = dir_in_str.split('=')[1]
        self.dir_out = dir_out_str.split('=')[1]

    def args_parse(self, values: typing.Tuple):
        """
        Метод парсит данные и присваивает значения позиционных аргументов экземпляру класса
        :param values: передаваемые в виде кортежа значения
        """
        self.is_valid_tuple(values)
        self.process_id = values[0]
        self.event_handler = values[1]
        self.message_id_suffix = values[2]
        path_list = values[3]
        self.split_path(path_list)

    def kwargs_parse(self, dict_values: typing.Dict):
        """
        Метод парсит данные и присваивает значения именованных аргументов экземпляру класса
        :param dict_values: передаваемые в виде словаря значения
        """
        self.is_valid_dict(dict_values)
        self.process_id = dict_values.get('process_id')
        self.event_handler = dict_values.get('event_handler')
        self.message_id_suffix = dict_values.get('message_id_suffix')
        path_list = dict_values['path']
        self.split_path(path_list)


class UserConfig(BaseItem):
    user_id: str
    member_id: str
    in_process_id: str
    out_process_id: str
    address: str
    encrypt_id: str
    key_alias: str
    flags: str
    user_desc: str
    params_check = [
        {
            'param_name': 'user_id',
            'check_max_length': True,
            'max_length': 8,
            'mandatory_lowercase': False,
            'param_is_string': True
        },
        {
            'param_name': 'member_id',
            'check_max_length': True,
            'max_length': 8,
            'mandatory_lowercase': False,
            'param_is_string': True
        },
        {
            'param_name': 'in_process_id',
            'check_max_length': True,
            'max_length': 8,
            'mandatory_lowercase': True,
            'param_is_string': True
        },
        {
            'param_name': 'out_process_id',
            'check_max_length': True,
            'max_length': 8,
            'mandatory_lowercase': True,
            'param_is_string': True
        },
        {
            'param_name': 'address',
            'check_max_length': False,
            'mandatory_lowercase': True,
            'param_is_string': True
        },
        {
            'param_name': 'encrypt_id',
            'check_max_length': True,
            'max_length': 10,
            'mandatory_lowercase': False,
            'param_is_string': True
        },
        {
            'param_name': 'key_alias',
            'check_max_length': True,
            'max_length': 1111,
            'mandatory_lowercase': False,
            'param_is_string': True
        },
        {
            'param_name': 'flags',
            'check_max_length': True,
            'max_length': 30,
            'mandatory_lowercase': False,
            'param_is_string': True
        },
        {
            'param_name': 'user_desc',
            'check_max_length': False,
            'mandatory_lowercase': False,
            'param_is_string': True
        }
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def args_parse(self, values: typing.Tuple):
        """
        Метод парсит данные и присваивает значения позиционных аргументов экземпляру класса
        :param values: передаваемые в виде кортежа значения
        """
        self.is_valid_tuple(values)
        self.user_id = values[0]
        self.member_id = values[1]
        self.in_process_id = values[2]
        self.out_process_id = values[3]
        self.address = values[4]
        self.encrypt_id = values[5]
        self.key_alias = values[6]
        self.flags = values[7]
        self.user_desc = values[8]

    def kwargs_parse(self, dict_values: typing.Dict):
        """
        Метод парсит данные и присваивает значения именованных аргументов экземпляру класса
        :param dict_values: передаваемые в виде словаря значения
        """
        self.is_valid_dict(dict_values)
        self.user_id = dict_values.get('user_id')
        self.member_id = dict_values.get('member_id')
        self.in_process_id = dict_values.get('in_process_id')
        self.out_process_id = dict_values.get('out_process_id')
        self.address = dict_values.get('address')
        self.encrypt_id = dict_values.get('encrypt_id')
        self.key_alias = dict_values.get('key_alias')
        self.flags = dict_values.get('flags')
        self.user_desc = dict_values.get('user_desc')


class GroupConfig(BaseItem):
    group_name: str
    users: list
    params_check = [
        {
            'param_name': 'group_name',
            'check_max_length': True,
            'max_length': 8,
            'mandatory_lowercase': False,
            'param_is_string': True
        },
        {
            'param_name': 'users',
            'check_max_length': False,
            'mandatory_lowercase': False,
            'param_is_string': True
        }
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def split_users(self, users: str):
        """
        Метод разделят переменную пользователей и присваивает значения параметрам класса
        :param users: изначально переданные пользователи
        """
        splitted_users = users.split(',')
        self.users= splitted_users

    def args_parse(self, values: typing.Tuple):
        """
        Метод парсит данные и присваивает значения позиционных аргументов экземпляру класса
        :param values: передаваемые в виде кортежа значения
        """
        self.is_valid_tuple(values)
        self.group_name = values[0]
        users = values[1]
        self.split_users(users)

    def kwargs_parse(self, dict_values: typing.Dict):
        """
        Метод парсит данные и присваивает значения именованных аргументов экземпляру класса
        :param dict_values: передаваемые в виде словаря значения
        """
        self.is_valid_dict(dict_values)
        self.group_name = dict_values.get('group_name')
        users = dict_values['users']
        self.split_users(users)
