from config_items import ProcessConfig
import unittest


class ProcessConfigTestCase(unittest.TestCase):

    def test_tuple(self):
        """
        unittest для проверки передачи значений кортежа
        """
        records = ('eraser', 'EraserHandler', 'er', 'DIR.IN=/usr/local/games/exch/proc/echo/in/;DIR.OUT=')
        t = ProcessConfig(*records)
        self.assertEqual(t.process_id, records[0])
        self.assertEqual(t.event_handler, records[1])
        self.assertEqual(t.message_id_suffix, records[2])
        self.assertEqual(t.dir_in, '/usr/local/games/exch/proc/echo/in/')
        self.assertEqual(t.dir_out, '')

    def test_dict(self):
        """
        unittest для проверки передачи значений словаря
        """
        dict1 = {
            'process_id': 'switch',
            'event_handler': 'SwitchHandler',
            'message_id_suffix': 'sw',
            'path': 'DIR.IN=/usr/local/games/exch/proc/echo/in/;DIR.OUT='
        }
        d = ProcessConfig(**dict1)
        self.assertEqual(d.process_id, dict1['process_id'])
        self.assertEqual(d.event_handler, dict1['event_handler'])
        self.assertEqual(d.message_id_suffix, dict1['message_id_suffix'])
        self.assertEqual(d.dir_in, '/usr/local/games/exch/proc/echo/in/')
        self.assertEqual(d.dir_out, '')

    def test_exception(self):
        """
        unittest для проверки вызова исключения
        :return:
        """
        not_underscore_records = (
            'erASer',
            'EraserHandler',
            'er',
            'DIR.IN=/usr/local/games/exch/proc/echo/in/;DIR.OUT='
        )
        with self.assertRaises(ValueError):
            _e = ProcessConfig(*not_underscore_records)
