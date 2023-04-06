from abc import ABC
import unittest


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
        pass

    def is_valid_dict(self, data_dict):
        pass


class Type1BaseItem(BaseItem):
    use_name: str
    full_name: str
    short_name: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def is_valid_tuple(self, data_tuple):
        for line in data_tuple:
            if not type(line) is str:
                raise TypeError('This parameter should be string!')

    def is_valid_dict(self, data_dict):
        for key in data_dict:
            if not type(data_dict[key]) is str:
                raise TypeError('This parameter should be string!')

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


class Type1TestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(Type1TestCase, self).__init__(*args, **kwargs)
        self.records_test = records
        self.dict1_test = dict1

    def test_use_name_tuple(self):
        self.assertEqual(s.use_name, self.records_test[0])

    def test_full_name_tuple(self):
        self.assertEqual(s.full_name, self.records_test[1])

    def test_short_name_tuple(self):
        self.assertEqual(s.short_name, self.records_test[2])

    def test_use_name_dict(self):
        self.assertEqual(a.use_name, self.dict1_test['use_name'])

    def test_full_name_dict(self):
        self.assertEqual(a.full_name, self.dict1_test['full_name'])

    def test_short_name_dict(self):
        self.assertEqual(a.short_name, self.dict1_test['short_name'])


records = ('eraser', 'EraserHandler', 'er')
dict1 = {'use_name': 'switch', 'full_name': 'SwitchHandler', 'short_name': 'sw'}
s = Type1BaseItem(*records)
a = Type1BaseItem(**dict1)
