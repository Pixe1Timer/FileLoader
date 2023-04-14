from stored_file_classes import StoredFileContainer, StoredFile

class Mhib(StoredFile):

    def __init__(self, file_path: str, file_name : str):
        super().__init__(file_path, file_name)

    def call_function_stored_file_container(self):
        f = StoredFileContainer(self.file_path, self.file_name)
        print(f.get_unlocked_files())


sf = Mhib('/home/ubuntu/Downloads', 'Python install')
print(sf.call_function_stored_file_container())
