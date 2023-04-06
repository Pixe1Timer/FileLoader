from config_items import Type1BaseItem
import unittest


class Type1TestCase(unittest.TestCase):
    records = ('eraser', 'EraserHandler', 'er')
    dict1 = {'use_name': 'switch', 'full_name': 'SwitchHandler', 'short_name': 'sw'}

    def test_tuple(self):
        t = Type1BaseItem(*self.records)
        self.assertEqual(t.use_name, self.records[0])
        self.assertEqual(t.full_name, self.records[1])
        self.assertEqual(t.short_name, self.records[2])

    def test_dict(self):
        d = Type1BaseItem(**self.dict1)
        self.assertEqual(d.use_name, self.dict1['use_name'])
        self.assertEqual(d.full_name, self.dict1['full_name'])
        self.assertEqual(d.short_name, self.dict1['short_name'])
