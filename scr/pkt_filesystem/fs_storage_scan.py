import os
import re
import logging
import scr.pkt_language.lng_message as plng
import scr.pkt_filesystem.fs_files_info as pffi

logger = logging.getLogger("app.pkt_filesystem.fs_storage_scan")


def fsss_storage_scan(str_path: str, str_search: str) -> (list, list, list):
    """
    Сканировать папку с ХРАНИЛИЩЕМ, вернуть список элементов ХРАНИЛИЩА.
    :param   (str) str_path: папка ХРАНИЛИЩА.
    :param   (str) str_search: строка поиска.
    :return: (список) содержимое Хранилища,
             (список) Логические ошибки,
             (список) дат по которым есть данные в Хранилище.
    """

    logger.info(plng.SS_LOGGER_START)

    try:
        # Проверка входных
        # Проверка: (str_path) - тип содержимого параметра не СТРОКА.
        if type(str_path) != str:
            logger.critical(plng.SS_PRM_STR_PATH_NOT_STR + ', type(' + str(type(str_path)) + ')')
            raise ValueError(plng.SS_PRM_STR_PATH_NOT_STR)

        # Проверка: (str_path) - наличия папки Хранилища.
        if not os.path.exists(str_path):
            logger.critical(plng.SS_PRM_STR_PATH_NOT_FOLDER + ': ' + str_path)
            raise ValueError(plng.SS_PRM_STR_PATH_NOT_FOLDER)

        # Проверка: (str_search) - строка поиска.
        if type(str_search) != str:
            logger.critical(plng.SS_PRM_STR_SEARCH_NOT_STR + ', type(' + str(type(str_search)) + ')')
            raise ValueError(plng.SS_PRM_STR_SEARCH_NOT_STR)

        name_regex: re = re.compile(str_search)

        int_count: int = 0
        lst_storage: list = []
        lst_storage_error: list = []
        lst_storage_date: list = []
        str_search_line: str = ''

        for root, dirs, files in os.walk(str_path):

            for f in files:
                str_search_line = root + "\\" + f
                mo = name_regex.search(str_search_line)

                if mo:
                    int_count += 1
                    str_matrix: str = ''

                    lst_storage.append({
                        'server': mo.group(1),
                        'path': mo.group(2) + '.' + mo.group(3) + '.' + mo.group(4),
                        'file': mo.group(5),
                        'date': pffi.fsfi_file_date_create(str_search_line),
                        'size': pffi.fsfi_file_size(str_search_line),
                        'id': str(int_count),
                        'matrix': str_matrix})

                    logger.info(f'server: {mo.group(1)}, path: {mo.group(2)}.{mo.group(3)}.{mo.group(4)} file: {mo.group(5)} date: {pffi.fsfi_file_date_create(str_search_line)} size: {pffi.fsfi_file_size(str_search_line)} id: {str(int_count)}')

                    lst_storage_date.append(int(mo.group(2) + mo.group(3) + mo.group(4)))
                    logger.debug(f'{mo.group(2) + mo.group(3) + mo.group(4)}')
                else:
                    lst_storage_error.append(str_search_line)
                    logger.warning(f'{str_search_line}')

        logger.info(f'{plng.SS_LOGGER_RESULT}')
        logger.info(f'всего: {len(lst_storage)}, о:{len(lst_storage_error)}, д:{len(lst_storage_date)}')

    except Exception as ex:
        logger.error(f'{plng.SS_ERROR_SCAN}, {ex}.')

    logger.info(plng.SS_LOGGER_FINISH)

    return lst_storage, lst_storage_error, lst_storage_date
