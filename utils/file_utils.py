# Утилиты для работы с файлами
import platform
import typing
from classes.misc_classes import FileDescriptor
import os
from uuid import uuid4
import tempfile


lsof_output_formatting = []


def generate_file_descriptor(**kwargs):
    """
    Создать объект файлового дескриптора
    :param dict kwargs:
    :return: FileDescriptor
    """
    process_number: str = kwargs.get('process_number', '')
    file_name: str = kwargs.get('file_name', '')
    file_descriptor: str = kwargs.get('file_descriptor', '')
    file_lock_status: str = kwargs.get('file_lock_status', '')
    access_mode: str = kwargs.get('access_mode', '')
    return FileDescriptor(
        int(process_number),
        file_name,
        file_descriptor,
        file_lock_status,
        access_mode
    )


def parse_lsof_output(lsof_output: [str]) -> typing.Iterable[FileDescriptor]:
    """
    Разобрать вывод от lsof
    :param [str] lsof_output: список строк вывода lsof
    :return: typing.Iterable[FileDescriptor]: список объектов описания файлов
    """
    process_number = None
    file_descriptor = None
    file_name = ''
    file_lock_status = ''
    access_mode = ''
    result = []
    for lsof_output_line in lsof_output:
        if lsof_output_line:
            line_first_letter = lsof_output_line[0]
            if line_first_letter in ('p', 'f'):
                if process_number and file_descriptor:
                    result.append(
                        generate_file_descriptor(
                            process_number=process_number,
                            file_descriptor=file_descriptor,
                            file_name=file_name,
                            file_lock_status=file_lock_status,
                            access_mode=access_mode
                        )
                    )
                if line_first_letter == 'p':
                    process_number = lsof_output_line[1:]
                elif line_first_letter == 'f':
                    file_descriptor = lsof_output_line[1:]
                file_name = ''
                file_lock_status = ''
                access_mode = ''
            if line_first_letter == 'n':
                file_name = lsof_output_line[1:]
            if line_first_letter == 'l':
                file_lock_status = lsof_output_line[1:]
            if line_first_letter == 'a':
                access_mode = lsof_output_line[1:]
    return result


def get_files_list_with_status() -> typing.Iterable[FileDescriptor]:
    """ Получить список файлов из lsof
    :return  typing.Iterable[FileDescriptor]: список объектов описания файлов
    """
    if platform.system() == 'Linux':
        import subprocess
        lsof_output = subprocess.check_output(['lsof', '-F'], text=True).split('\n')
        return parse_lsof_output(lsof_output)
    else:
        return []


def create_temp_dir(base_path: str | None = None) -> str:
    """
    Создать временную папку (Используем стандартный модуль tempfile)
    :param str | None base_path: базовый путь для создания папки
    :return: str: путь созданной папки
    """
    tmp_dir_name = tempfile.mkdtemp(suffix=None, prefix=None, dir=base_path)
    return tmp_dir_name


def remove_temp_dir(temp_dir_path: str):
    """
    Удалить папку с удалением всех файлов
    :param str temp_dir_path: Путь до удаляемой папки
    :return: None
    """
    for root, dirs, files in os.walk(temp_dir_path, topdown=False):
        for name in files:
            try:
                os.chmod(os.path.join(root, name), 0o777)
            except PermissionError:
                pass
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(temp_dir_path)
