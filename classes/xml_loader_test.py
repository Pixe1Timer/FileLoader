import unittest
from classes.xml_loader import XMLFileLoader
from utils.file_utils import create_temp_dir, remove_temp_dir
import os


class XMLFileLoaderTest(unittest.TestCase):
    def test_parse_without_store_class(self):
        temporary_folder = create_temp_dir()
        no_class_file = None
        try:
            no_class_path = os.path.join(temporary_folder, 'route.xml')
            xml_data = '''
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
            with open(no_class_path, 'w') as no_class_file:
                no_class_file.write('<exchange>{}</exchange>'.format(xml_data))
            loader = XMLFileLoader()
            loader.load(str(no_class_path))
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
        finally:
            if no_class_file:
                no_class_file.close()
            remove_temp_dir(temporary_folder)

    def test_parse_with_store_class(self):
        temporary_folder = create_temp_dir()
        stored_class_file = None
        try:
            stored_class_path = os.path.join(temporary_folder, 'tree.xml')
            class_data = '''
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

            with open(stored_class_path, 'w') as stored_class_file:
                stored_class_file.write('<root>{}</root>'.format(class_data))

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
            loader.load(str(stored_class_path))
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
        finally:
            if stored_class_file:
                stored_class_file.close()
            remove_temp_dir(temporary_folder)
