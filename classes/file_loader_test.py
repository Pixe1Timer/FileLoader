from file_loader_class import SplittedFileLoader
from utils.temp_file_creator import tempFileCreator
import unittest

test_data_sets = [
    {
        'set_data': [
            'Name|Value|546\n',
            'Example1|test|45\n',
            'Example2|test|63\n',
            '# Example|test|35\n',
            ' '
        ],
        'expected_result': [
            ['Name', 'Value', '546'],
            ['Example1', 'test', '45'],
            ['Example2', 'test', '63']
        ],
        'wrong_data': [
            'Name|Value|546\n',
            'Example1|test|45|123\n',
            'Example2|test|63\n',
            '# Example|test|35\n',
            ' '
        ],
    },
]


class MyTestCase(unittest.TestCase):
    target_file_path = 'temp/file.txt'

    def test_file_loader(self):
        for test_case in test_data_sets:
            data = test_case.get('set_data')
            expected = test_case.get('expected_result')
            result = self.execute_logic(data)
            self.assertEqual(result, expected)

    def test_exception(self):
        for test_case in test_data_sets:
            data = test_case.get('wrong_data')
            with self.assertRaises(ValueError):
                _result = self.execute_logic(data)

    def execute_logic(self, data):
        temp_file_creator = tempFileCreator(data, self.target_file_path)
        loader = SplittedFileLoader('|', self.target_file_path)
        result = loader.parsed_data
        temp_file_creator.purge()
        return result
