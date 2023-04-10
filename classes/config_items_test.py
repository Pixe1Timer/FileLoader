from config_items import Type1BaseItem
import unittest


class Type1TestCase(unittest.TestCase):
    records = ('eraser', 'EraserHandler', 'er', 'DIR.IN=/usr/local/games/exch/proc/echo/in/;DIR.OUT=')
    dict1 = {'process_id': 'switch', 'event_handler': 'SwitchHandler', 'message_id_suffix_2_letters': 'sw', 'path':
             'DIR.IN=/usr/local/games/exch/proc/echo/in/;DIR.OUT='}

    def test_tuple(self):
        t = Type1BaseItem(*self.records)
        self.assertEqual(t.process_id, self.records[0])
        self.assertEqual(t.event_handler, self.records[1])
        self.assertEqual(t.message_id_suffix_2_letters, self.records[2])
        print(f'Input path:{t.din}, output path: {t.dout}')

    def test_dict(self):
        d = Type1BaseItem(**self.dict1)
        self.assertEqual(d.process_id, self.dict1['process_id'])
        self.assertEqual(d.event_handler, self.dict1['event_handler'])
        self.assertEqual(d.message_id_suffix_2_letters, self.dict1['message_id_suffix_2_letters'])
        print(f'Input path:{d.din}, output path: {d.dout}')
