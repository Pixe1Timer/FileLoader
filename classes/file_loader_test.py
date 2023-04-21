from file_loader_class import SplitedFileLoader
from utils.temp_file_creator import tempFileCreator
import unittest

test_data_sets = [
    {
        'set_data': [
            'Name|Value|546\n',
            'Example1|test|35\n',
            'Example2 | test|63\n',
            '# Example|test|35\n',
            ' '
        ],
        'expected_result': [
            ['Name', 'Value', '546'],
            ['Example1', 'test', '35'],
            ['Example2', 'test', '63']
        ]
    },
    #
    # {
    #     'set_data': [
    #         '''
    #        wepofjwefjopaeojfaowefihwefpiohOIFHOI
    #        124712
    #        e75qww 46a8sd46a8sd4 6 R*&%*)      &*_(^*T%&%^
    #        5
    #        \7
    #        684das4d68asd84as68d4684a6s8d46as8d4a86sd
    #         ''',
    #     ],
    #     'expected_exception': ValueError
    # },
]


class MyTestCase(unittest.TestCase):
    target_file_path = 'temp/file.txt'

    def test_file_loader(self):
        for test_case in test_data_sets:
            data = test_case.get('set_data')
            expected = test_case.get('expected_result')
            #exception = test_case.get('expected_exception')
            result = self.execute_logic(data)
            self.assertEqual(result, expected)

    def execute_logic(self, data):
            temp_file_creator = tempFileCreator(data, self.target_file_path)
            loader = SplitedFileLoader('|', self.target_file_path)
            result = loader.parsed_data
            temp_file_creator.purge()
            return result


if __name__ == '__main__':
    unittest.main()
