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
    age: int
    name: str
    gender: str
    key: bool

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def args_parse(self, values):
        self.age = values[0]
        self.name = values[1]
        self.gender = values[2]

    def kwargs_parse(self, dict_values):
        self.age = dict_values.get('age')
        self.name = dict_values.get('name')
        self.gender = dict_values.get('gender')

    def is_valid(self) -> (bool, str):
        pass


records = (10, 'Paul', 'F')
dict1 = {'age': 22, 'name': 'Denis', 'gender': 'M'}
s = Type1BaseItem(*records)
a = Type1BaseItem(age=22, name='Denis', gender='M')
print(s.age, s.name, s.gender)
print(a.age, a.name, a.gender)
