from abc import ABC


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
        for line in data_tuple:
            if not type(line) is str:
                raise TypeError('This parameter should be string!')
            elif len(line) > 19:
                raise IndexError('Length is out of range!')
        if not data_tuple[0].islower() or not data_tuple[2].islower():
            raise ValueError('Values are not lowercase!')

    def is_valid_dict(self, data_dict):
        for key in data_dict:
            if not type(data_dict[key]) is str:
                raise TypeError('This parameter should be string!')
            if len(data_dict[key]) > 19:
                raise IndexError('Length is out of range!')
            if key != 'Event_handler' and (not data_dict[key].islower() or not data_dict[key].islower()):
                raise ValueError('Values are not lowercase!')


class Type1BaseItem(BaseItem):
    Process_ID: str
    Event_handler: str
    Message_ID_suffix_2_letters: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def is_valid_tuple(self, data_tuple):
        super().is_valid_tuple(data_tuple)

    def is_valid_dict(self, data_dict):
        super().is_valid_dict(data_dict)

    def args_parse(self, values):
        self.is_valid_tuple(values)
        self.Process_ID = values[0]
        self.Event_handler = values[1]
        self.Message_ID_suffix_2_letters = values[2]

    def kwargs_parse(self, dict_values):
        self.is_valid_dict(dict_values)
        self.Process_ID = dict_values.get('Process_ID')
        self.Event_handler = dict_values.get('Event_handler')
        self.Message_ID_suffix_2_letters = dict_values.get('Message_ID_suffix_2_letters')
