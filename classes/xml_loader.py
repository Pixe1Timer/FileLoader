from lxml import etree


class XMLFileLoader:

    def __init__(self, xml_route=None):
        self.xml_data = None
        if xml_route is None:
            self.xml_route = {
                'pattern': './PATTERNS',
                'source': './SOURCES',
                'target': './TARGETS',
                'types': './TYPES',
                'flags': './FLAGS',
                'desc': './DESC'
            }
        else:
            self.xml_route = xml_route

    def load(self, file_path):
        with open(file_path) as f:
            self.xml_data = etree.parse(f)

    def parse(self):
        chains = []
        for chain_element in self.xml_data.xpath('/chain'):
            chain = {}
            for key, value in self.xml_route:
                chain[key] = chain_element.xpath(value).text
            chains.append(chain)
        return chains
