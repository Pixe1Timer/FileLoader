from abc import ABC
import re


class BaseItem(ABC):
    def __init__(self, *args, **kwargs):
        if args:
            self.args_parse(args)
        else:
            self.kwargs_parse(kwargs)

    def args_parse(self, values):
        pass

    def kwargs_parse(self, dict_values):
        pass

    def is_valid_tuple(self, data_tuple):
        for line in data_tuple[:-1]:
            if not type(line) is str:
                raise TypeError('This parameter should be string!')
            elif len(line) > 19:
                raise ValueError('Length is out of range!')
        if not data_tuple[0].islower() or not data_tuple[2].islower():
            raise ValueError('Values are not lowercase!')

    def is_valid_dict(self, data_dict):
        for key in data_dict:
            if key != 'path':
                if not type(data_dict[key]) is str:
                    raise TypeError('This parameter should be string!')
                if len(data_dict[key]) > 10000:
                    raise ValueError('Length is out of range!')
                if (key != 'event_handler') and not data_dict[key].islower():
                    raise ValueError('Values are not lowercase!')


class Type1BaseItem(BaseItem):
    process_id: str
    event_handler: str
    message_id_suffix_2_letters: str
    din: str
    dout: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path_list = []

    def is_valid_tuple(self, data_tuple):
        super().is_valid_tuple(data_tuple)
        pass

    def is_valid_dict(self, data_dict):
        super().is_valid_dict(data_dict)
        pass

    def split_path(self, path):
        splitted_path = path.split(';')
        if not re.match(r'DIR.IN=', splitted_path[0]) or not re.match(r'DIR.OUT=', splitted_path[1]):
            raise ValueError('Невозможно найти нужные параметры!')
        self.din = splitted_path[0].split('=')[1]
        self.dout = splitted_path[1].split('=')[1]
        return self.din, self.dout

    def args_parse(self, values):
        self.is_valid_tuple(values)
        self.process_id = values[0]
        self.event_handler = values[1]
        self.message_id_suffix_2_letters = values[2]
        self.path_list = values[3]
        self.split_path(self.path_list)

    def kwargs_parse(self, dict_values):
        self.is_valid_dict(dict_values)
        self.process_id = dict_values.get('process_id')
        self.event_handler = dict_values.get('event_handler')
        self.message_id_suffix_2_letters = dict_values.get('message_id_suffix_2_letters')
        self.path_list = dict_values['path']
        self.split_path(self.path_list)
