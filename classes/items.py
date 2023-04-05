from abc import ABC


class BaseItem(ABC):
    def __init__(self, *args, **kwargs):
        if args:
            self.args_parse(args)
        else:
            self.kwargs_parse(kwargs)

    def is_valid(self) -> (bool, str):
        return True, ''

    def args_parse(self, values):
        pass

    def kwargs_parse(self, dict_values):
        pass


class Type1BaseItem(BaseItem):
    use_name: str
    full_name: str
    short_name: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def args_parse(self, values):
        self.use_name = values[0]
        self.full_name = values[1]
        self.short_name = values[2]

    def kwargs_parse(self, dict_values):
        self.use_name = dict_values.get('use_name')
        self.full_name = dict_values.get('full_name')
        self.short_name = dict_values.get('short_name')

    def is_valid(self) -> (bool, str):
        try:
            pass
        except:
            pass


records = ('eraser', 'EraserHandler', 'er')
dict1 = {'use_name': 'switch', 'full_name': 'SwitchHandler', 'short_name': 'sw'}
s = Type1BaseItem(*records)
a = Type1BaseItem(**dict1)
print(s.use_name, s.full_name, s.short_name)
print(a.use_name, a.full_name, a.short_name)
