from lxml import etree


class XMLFileLoader:
    def __init__(self, xml_content=None):
        self.store_class = None
        self.xml_data = None
        if xml_content is None:
            self.xml_content = {
                'pattern': './PATTERNS',
                'source': './SOURCES',
                'target': './TARGETS',
                'types': './TYPES',
                'flags': './FLAGS',
                'desc': './DESC'
            }
        else:
            self.xml_content = xml_content

    def load(self, file_path):
        with open(file_path) as f:
            self.xml_data = etree.parse(f)

    def parse(self):
        elements_list = []
        for element in self.xml_data.xpath('/chain'):
            sub_elements = {}
            for key, value in self.xml_content:
                sub_elements[key] = element.xpath(value).text
            elements_list.append(self.store_class(sub_elements) if self.store_class else sub_elements)
        return elements_list
