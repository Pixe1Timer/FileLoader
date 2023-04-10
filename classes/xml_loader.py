from lxml import etree


class XMLFileLoader:
    def __init__(self):
        self.xml_data = None

    def load(self, file_path):
        with open(file_path) as f:
            self.xml_data = etree.parse(f)

    def parse(self):
        chains = []
        for chain_element in self.xml_data.xpath('/chain'):
            pattern = chain_element.xpath('./PATTERNS').text
            source = chain_element.xpath('./SOURCES').text
            target = chain_element.xpath('./TARGETS').text
            types = chain_element.xpath('./TYPES').text
            flags = chain_element.xpath('./FLAGS').text
            desc = chain_element.xpath('./DESC').text

            chain = {'pattern': pattern,
                     'source': source,
                     'target': target,
                     'types': types,
                     'flags': flags,
                     'desc': desc}
            chains.append(chain)
        return chains
