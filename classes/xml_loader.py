from lxml import etree


class XMLFileLoader:
    """
    Элемент для загрузки и разбора данных файла .xml
    """
    store_class = None

    def __init__(self, xml_content: dict | None = None):
        """
        Конструктор класса
        :param dict[str] | None xml_content: содержимое файла, если не указано - назначается по умолчанию
        """
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

    def load(self, file_path: str):
        """
        Загрузка файла .xml
        :param str file_path: путь к .xml файлу
        """
        with open(file_path) as f:
            self.xml_data = etree.parse(f)

    def parse(self) -> list:
        """
        Разбор данных файла
        :return: list: возврат обработанных данных файла
        """
        elements_list = []
        for element in self.xml_data.xpath('/*/*'):
            sub_elements = {}
            for key, value in self.xml_content.items():
                sub_elements[key] = element.find(value).text
            elements_list.append(self.store_class(sub_elements) if self.store_class else sub_elements)
        return elements_list
