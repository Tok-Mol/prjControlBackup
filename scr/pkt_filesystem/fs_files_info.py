import os
import logging
import scr.pkt_language.lng_message as plng
from datetime import datetime

logger = logging.getLogger("app.pkt_filesystem.fs_files_info")


def fsfi_file_date_create(str_file_name: str) -> str:
    """
    Файл - Дата создания
    :param   (str) str_file_name: имя файла.
    :return: (str) дата-время создания файла.
    """
    try:
        # Проверка: (str_file_name) - тип содержимого параметра не СТРОКА.
        if type(str_file_name) != str:
            logger.critical(plng.FD_PRM_STR_FILE_NAME_NOT_STR + ', type(' + str(type(str_file_name)) + ')')
            raise ValueError(plng.FD_PRM_STR_FILE_NAME_NOT_STR)

        str_result: str = ""
        if os.path.exists(str_file_name):
            # file available
            str_result = str(datetime.fromtimestamp(os.path.getctime(str_file_name)).strftime("%Y-%m-%d %H:%M"))
        else:
            # no file
            logger.error(f'{plng.FD_PRM_STR_FILE_NAME_NOT_FILE}, fsfi_file_date_create(), аргумент: {str_file_name}.')
            str_result = ""
        return str_result
    except Exception as ex:
        logger.error(f'{plng.FD_ERROR}, fsfi_file_date_create(), аргумент: {str_file_name}, ошибка: {ex}')
        return ''


def fsfi_file_size(str_file_name: str) -> str:
    """
    Файл - Размер
    :param   (str) str_file_name:  str_file_name: имя файла.
    :return: (str) размер файла.
    """
    try:
        # Проверка: (str_file_name) - тип содержимого параметра не СТРОКА.
        if type(str_file_name) != str:
            logger.critical(plng.FS_PRM_STR_FILE_NAME_NOT_STR + ', type(' + str(type(str_file_name)) + ')')
            raise ValueError(plng.FS_PRM_STR_FILE_NAME_NOT_STR)

        str_result: str = ""
        if os.path.exists(str_file_name):
            # file available
            str_result = str(os.path.getsize(str_file_name))
        else:
            # no file
            logger.error(f'{plng.FS_PRM_STR_FILE_NAME_NOT_FILE}, fsfi_file_size(), аргумент: {str_file_name}.')
            str_result = ""
        return str_result
    except Exception as ex:
        logger.error(f'{plng.FS_ERROR}, fsfi_file_size(), аргумент: {str_file_name}, ошибка: {ex}')
        return ''
