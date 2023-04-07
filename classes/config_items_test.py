from config_items import Type1BaseItem
import unittest


class Type1TestCase(unittest.TestCase):
    records = ('eraser', 'EraserHandler', 'er')
    dict1 = {'Process_ID': 'switch', 'Event_handler': 'SwitchHandler', 'Message_ID_suffix_2_letters': 'sw'}

    def test_tuple(self):
        t = Type1BaseItem(*self.records)
        self.assertEqual(t.Process_ID, self.records[0])
        self.assertEqual(t.Event_handler, self.records[1])
        self.assertEqual(t.Message_ID_suffix_2_letters, self.records[2])

    def test_dict(self):
        d = Type1BaseItem(**self.dict1)
        self.assertEqual(d.Process_ID, self.dict1['Process_ID'])
        self.assertEqual(d.Event_handler, self.dict1['Event_handler'])
        self.assertEqual(d.Message_ID_suffix_2_letters, self.dict1['Message_ID_suffix_2_letters'])
