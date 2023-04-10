from abc import ABC
import re
import typing


def check_parametrised_value(params_dict: dict, param_value: typing.Any):
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
    params_check = []

    def __init__(self, *args, **kwargs):
        if args:
            self.args_parse(args)
        else:
            self.kwargs_parse(kwargs)

    def args_parse(self, values: typing.Tuple):
        pass

    def kwargs_parse(self, dict_values: typing.Dict):
        pass

    def is_valid_tuple(self, data_tuple: typing.Tuple):
        for position, param_check_value in enumerate(self.params_check):
            param_value = data_tuple[position]
            check_parametrised_value(param_check_value, param_value)

    def is_valid_dict(self, data_dict: typing.Dict):
        for param_check_value in self.params_check:
            param_value = data_dict[param_check_value.get('param_name')]
            check_parametrised_value(param_check_value, param_value)


class ProcessConfig(BaseItem):
    process_id: str
    event_handler: str
    message_id_suffix: str
    din: str
    dout: str
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

    def __init__(self, *args: typing.Any, **kwargs: typing.Any):
        super().__init__(*args, **kwargs)
        self.path_list = []

    def is_valid_tuple(self, data_tuple: typing.Tuple):
        super().is_valid_tuple(data_tuple)
        pass

    def split_path(self, path: str):
        splitted_path = path.split(';')
        dir_in_str = splitted_path[0]
        dir_out_str = splitted_path[1]
        if not re.match(r'DIR.IN=', dir_in_str):
            raise ValueError(f'{dir_in_str} не является директорией!')
        if not re.match(r'DIR.OUT=', dir_out_str):
            raise ValueError(f'{dir_out_str} не является директорией!')
        self.din = dir_in_str.split('=')[1]
        self.dout = dir_out_str.split('=')[1]

    def args_parse(self, values: typing.Tuple):
        self.is_valid_tuple(values)
        self.process_id = values[0]
        self.event_handler = values[1]
        self.message_id_suffix = values[2]
        self.path_list = values[3]
        self.split_path(self.path_list)

    def kwargs_parse(self, dict_values: typing.Dict):
        self.is_valid_dict(dict_values)
        self.process_id = dict_values.get('process_id')
        self.event_handler = dict_values.get('event_handler')
        self.message_id_suffix = dict_values.get('message_id_suffix')
        self.path_list = dict_values['path']
        self.split_path(self.path_list)
