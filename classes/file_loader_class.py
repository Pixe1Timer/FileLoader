import os


class SplitedFileLoader:
    def __init__(self, separator: str, file_path: str):
        self.separator = separator
        self.file_path = os.path.normpath(file_path)
        self.parsed_data = self._parse()

    def validate(self, data, expected_length):
        if self.separator not in data:
            raise ValueError('Separator is not provided')
        if len(data.split(self.separator)) != expected_length:
            raise ValueError('Incorrect number of elements in line')

    def load(self) -> list:
        base_file_path = os.path.basename(self.file_path)
        file_dir = os.path.dirname(os.path.abspath(self.file_path))
        full_file_path = os.path.join(file_dir, base_file_path)
        try:
            with open(full_file_path) as file:
                all_lines = file.readlines()
                for line in all_lines:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        self.validate(line, len(line.split(self.separator)))
                data = [line for line in all_lines]
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
        parsed_data = [self._parsed_line(line) for line in data]
        parsed_data = [line for line in parsed_data if line]
        return parsed_data
