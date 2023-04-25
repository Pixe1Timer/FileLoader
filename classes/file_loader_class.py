import os


class SplittedFileLoader:
    """
        Класс для загрузки и обработки данных из файла с разделителем

        Атрибуты:
        separator(str): разделитель параметров в строке
        file_path(str): путь к файлу

        Методы:
        set_generated_class(generated_class): установка класса, представляющего объекты, получаемые из строк файла
        load() -> list: загрузка данных из файла, возвращение списка строк
        parse_line(line: str) -> list or None: парсинг строки в список параметров, если строка валидна
        parse() -> list: обработка списка строк в список объектов класса generated_class, если он задан
    """
    def __init__(self, separator: str, file_path: str):
        """
        Инициализация атрибутов

        separator(str): разделитель параметров в строке
        file_path(str): путь к файлу
        """
        self.separator = separator
        self.file_path = os.path.normpath(file_path)
        self.generated_class = None
        self.parsed_data = self.parse()

    def set_generated_class(self, generated_class):
        """
        Установка класса, представляющего объекты, получаемые из строк файла

        generated_class: класс, представляющий объекты, получаемые из строк файла
        """
        self.generated_class = generated_class

    def load(self) -> list:
        """
        Загрузка данных из файла

        return: список строк, прочитанных из файла
        """
        expected_length = None
        try:
            with open(self.file_path) as file:
                all_lines = file.readlines()
                for line in all_lines:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        parsed_line = self.parse_line(line)
                        if expected_length is None:
                            expected_length = len(parsed_line)
                        if len(parsed_line) != expected_length:
                            raise ValueError('Количество параметров не совпадает!')
            data = all_lines
        except FileNotFoundError:
            raise ValueError("Файл с указанным путем не существует")
        return data

    def parse_line(self, line: str) -> list or None:
        """
        Парсинг строки в список параметров

        line(str): строка, которую нужно обработать

        return: возвращает список параметров, если строка валидна, иначе None
        """
        line = line.replace('\t', '').strip()
        if line and not line.startswith('#'):
            parsed_line = line.split(self.separator)
            parsed_line = [value.strip() for value in parsed_line]
            return parsed_line
        else:
            return None

    def parse(self) -> list:
        """
        Обработка списка строк в список объектов класса generated_class, если он задан

        return: список объектов или список списков параметров
        """
        data = self.load()
        parsed_data = []
        for line in data:
            parsed_value = self.parse_line(line)
            parsed_value = self.generated_class(*parsed_value) if self.generated_class else parsed_value
            parsed_data.append(parsed_value) if parsed_value else None
        return parsed_data
