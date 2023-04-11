from config_items import ProcessConfig, UserConfig
import unittest


class ProcessConfigTestCase(unittest.TestCase):

    def test_tuple_procs(self):
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

    def test_dict_procs(self):
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

    def test_exception_procs(self):
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

    def test_tuple_user(self):
        """
        unittest для проверки передачи значений кортежа
        """
        records_user = ('0015',
                        '015',
                        'csin',
                        'mailout',
                        'sas-tamcard@primbank.ru',
                        'CS',
                        'BC=0015',
                        '-',
                        'PRIMORYE bank')
        t1 = UserConfig(*records_user)
        self.assertEqual(t1.user_id, records_user[0])
        self.assertEqual(t1.member_id, records_user[1])
        self.assertEqual(t1.in_process_id, records_user[2])
        self.assertEqual(t1.out_process_id, records_user[3])
        self.assertEqual(t1.address, records_user[4])
        self.assertEqual(t1.encrypt_id, records_user[5])
        self.assertEqual(t1.key_alias, records_user[6])
        self.assertEqual(t1.flags, records_user[7])
        self.assertEqual(t1.user_desc, records_user[8])

    def test_dict_user(self):
        """
        unittest для проверки передачи значений словаря
        """
        dict_user = {
            'user_id': '0015',
            'member_id': '015',
            'in_process_id': 'csin',
            'out_process_id': 'mailout',
            'address': 'sas-tamcard@primbank.ru',
            'encrypt_id': 'CS',
            'key_alias': 'BC=0015',
            'flags': '-',
            'user_desc': 'PRIMORYE bank',
        }
        d1 = UserConfig(**dict_user)
        self.assertEqual(d1.user_id, dict_user['user_id'])
        self.assertEqual(d1.member_id, dict_user['member_id'])
        self.assertEqual(d1.in_process_id, dict_user['in_process_id'])
        self.assertEqual(d1.out_process_id, dict_user['out_process_id'])
        self.assertEqual(d1.address, dict_user['address'])
        self.assertEqual(d1.encrypt_id, dict_user['encrypt_id'])
        self.assertEqual(d1.key_alias, dict_user['key_alias'])
        self.assertEqual(d1.flags, dict_user['flags'])
        self.assertEqual(d1.user_desc, dict_user['user_desc'])

    def test_exception_user(self):
        """
        unittest для проверки вызова исключения
        """
        not_underscore_records_user = (
            '0015',
            '015',
            'csin',
            'mailout',
            'sas-tamcard@primbank.ru',
            'CS',
            'BC=0015',
            '-',
            'PRIMORYE bank'
        )
        with self.assertRaises(ValueError):
            _aa = ProcessConfig(*not_underscore_records_user)
