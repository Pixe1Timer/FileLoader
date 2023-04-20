import os


class SplitedFileLoader:
    def __init__(self, separator: str, file_path: str):

        self.separator = separator
        self.file_path = os.path.normpath(file_path)
        self.parsed_data = self._parse()

    def validate(self, data):
        if self.separator not in data:
            raise ValueError('Separator is not provided')

    def load(self) -> list:

        cur_dir = os.getcwd()
        full_file_path = os.path.join(cur_dir, self.file_path)
        try:
            with open(full_file_path) as file:
                all_lines = file.readlines()
                self.validate('\n'.join(all_lines))
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

    def _parse(self) -> list:

        data = self.load()
        parsed_data = [self._parsed_line(line) for line in data]
        parsed_data = [line for line in parsed_data if line is not None]
        return parsed_data
