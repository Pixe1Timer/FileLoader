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

    def is_valid_dict(self, data_dict):
        for key in data_dict:
            if not type(data_dict[key]) is str:
                raise TypeError('This parameter should be string!')


class Type1BaseItem(BaseItem):
    use_name: str
    full_name: str
    short_name: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def is_valid_tuple(self, data_tuple):
        super().is_valid_tuple(data_tuple)

    def is_valid_dict(self, data_dict):
        super().is_valid_dict(data_dict)

    def args_parse(self, values):
        self.is_valid_tuple(values)
        self.use_name = values[0]
        self.full_name = values[1]
        self.short_name = values[2]

    def kwargs_parse(self, dict_values):
        self.is_valid_dict(dict_values)
        self.use_name = dict_values.get('use_name')
        self.full_name = dict_values.get('full_name')
        self.short_name = dict_values.get('short_name')
