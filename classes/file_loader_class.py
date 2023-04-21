import os


class SplitedFileLoader:
    def __init__(self, separator: str, file_path: str):
        self.separator = separator
        self.file_path = os.path.normpath(file_path)
        self.parsed_data = self._parse()

    def load(self) -> list:
        expected_length = None
        try:
            with open(self.file_path) as file:
                all_lines = file.readlines()
                for line in all_lines:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        parsed_line = self._parsed_line(line)
                        if expected_length is None:
                            expected_length = len(parsed_line)
                        if len(parsed_line) != expected_length:
                            raise ValueError('Количество параметров не совпадает!')
            data = all_lines
        except FileNotFoundError:
            raise ValueError("Файл с указанным путем не существует")
        return data

    def _parsed_line(self, line: str) -> list or None:
        line = line.replace('\t', '').strip()
        if line and not line.startswith('#'):
            parsed_line = line.split(self.separator)
            parsed_line = [value.strip() for value in parsed_line]
            return parsed_line
        else:
            return None

    def filter_data(self, data):
        def filter_func(x):
            return x is not None

        filtered_data = filter(filter_func, [self._parsed_line(line) for line in data])
        return list(filtered_data)

    def _parse(self) -> list:
        data = self.load()
        parsed_data = self.filter_data(data)
        return parsed_data
