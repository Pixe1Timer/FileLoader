import unittest
from classes.xml_loader import XMLFileLoader
import os


class XMLFileLoaderTest(unittest.TestCase):

    def test_parse_without_store_class(self):
        self.xml_file_path = '/home/ubuntu/forTest/route.xml'
        self.xml_data = '''
            <chain>
                <PATTERNS>pattern1</PATTERNS>
                <SOURCES>source1</SOURCES>
                <TARGETS>target1</TARGETS>
                <TYPES>type1</TYPES>
                <FLAGS>flag1</FLAGS>
                <DESC>desc1</DESC>
            </chain>
            <chain>
                <PATTERNS>pattern2</PATTERNS>
                <SOURCES>source2</SOURCES>
                <TARGETS>target2</TARGETS>
                <TYPES>type2</TYPES>
                <FLAGS>flag2</FLAGS>
                <DESC>desc2</DESC>
            </chain>
        '''
        with open(self.xml_file_path, 'w') as f:
            f.write('<exchange>{}</exchange>'.format(self.xml_data))

        loader = XMLFileLoader()
        loader.load(self.xml_file_path)
        actual_result = loader.parse()
        expected_result = [
            {
                'pattern': 'pattern1',
                'source': 'source1',
                'target': 'target1',
                'types': 'type1',
                'flags': 'flag1',
                'desc': 'desc1'
            },
            {
                'pattern': 'pattern2',
                'source': 'source2',
                'target': 'target2',
                'types': 'type2',
                'flags': 'flag2',
                'desc': 'desc2'
            }
        ]
        self.assertEqual(actual_result, expected_result)
        os.remove(self.xml_file_path)

    def test_parse_with_store_class(self):
        self.store_file_path = '/home/ubuntu/forTest/tree.xml'
        self.xml_data = '''
            <tree>
                <BRANCHES>branch1</BRANCHES>
                <LEAVES>leaf1</LEAVES>
                <FRUITS>fruit1</FRUITS>
            </tree>
            <tree>
                <BRANCHES>branch2</BRANCHES>
                <LEAVES>leaf2</LEAVES>
                <FRUITS>fruit2</FRUITS>
            </tree>
        '''
        with open(self.store_file_path, 'w') as f:
            f.write('<root>{}</root>'.format(self.xml_data))

        class TestXML:
            def __init__(self, dict_content: dict):
                self.branch = dict_content.get('branch')
                self.leaf = dict_content.get('leaf')
                self.fruit = dict_content.get('fruit')

            def __str__(self):
                return f'branch: {self.branch}, leaf: {self.leaf}, fruit: {self.fruit}'

        class CustomXMLLoader(XMLFileLoader):
            store_class = TestXML

        xml_content = {
            'branch': './BRANCHES',
            'leaf': './LEAVES',
            'fruit': './FRUITS'
        }

        loader = CustomXMLLoader(xml_content)
        loader.load(self.store_file_path)
        actual_result = loader.parse()
        actual_result_str = [str(obj) for obj in actual_result]
        expected_result = [
            {
                'branch': 'branch1',
                'leaf': 'leaf1',
                'fruit': 'fruit1'
            },
            {
                'branch': 'branch2',
                'leaf': 'leaf2',
                'fruit': 'fruit2'
            }
        ]
        expected_result_str = [str(obj) for obj in [TestXML(content) for content in expected_result]]
        self.assertEqual(actual_result_str, expected_result_str)
        os.remove(self.store_file_path)
