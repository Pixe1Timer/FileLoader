import typing
from classes.config_items import BaseItem
from classes.xml_loader import XMLFileLoader


class ConfigRoute(BaseItem):
    pattern: str
    source: str
    target: str
    types: str
    flags: str
    desc: str
    params_check = [
        {
            'param_name': 'pattern',
            'check_max_length': False,
            'mandatory_lowercase': False,
            'param_is_string': True
        },
        {
            'param_name': 'source',
            'check_max_length': False,
            'mandatory_lowercase': False,
            'param_is_string': True
        },
        {
            'param_name': 'target',
            'check_max_length': False,
            'mandatory_lowercase': False,
            'param_is_string': True
        },
        {
            'param_name': 'types',
            'check_max_length': False,
            'mandatory_lowercase': False,
            'param_is_string': True
        },
        {
            'param_name': 'flags',
            'check_max_length': False,
            'mandatory_lowercase': False,
            'param_is_string': True
        },
        {
            'param_name': 'desc',
            'check_max_length': False,
            'mandatory_lowercase': False,
            'param_is_string': True
        }
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def kwargs_parse(self, dict_values: typing.Dict):
        self.is_valid_dict(dict_values)
        self.pattern = dict_values.get('pattern')
        self.source = dict_values.get('source')
        self.target = dict_values.get('target')
        self.types = dict_values.get('types')
        self.flags = dict_values.get('flags')
        self.desc = dict_values.get('desc')


class ConfigRouteContainer(XMLFileLoader):
    store_class = ConfigRoute
