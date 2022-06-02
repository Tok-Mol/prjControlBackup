import os
import logging
import scr.pkt_language.lng_message as plng
from operator import itemgetter

logger = logging.getLogger("app.pkt_filesystem.fs_journal")


def fsj_journal_date(str_path: str, str_file: str, lst_data: list, str_date_min: str, str_date_max: str, bol_reverse: bool) -> bool:
    """
    Запись данных в txt-файл c сортировкой по дате (прямая/обратная).
    :param str_path: (str) папка для хранения файла-журнала.
    :param str_file: (str) имя файла-журнала.
    :param lst_data: (list) список словарей с данными о резервных копиях для сохранения
           в файле-отчёте.
           Формат списка: [{запись списка: dict}, {запись списка: dict},{запись списка: dict}]
           Каждая запись списка содержит словарь с данными о резервной копии.
           Структура записи списка в формате словаря:
           'server': (str) имя сервера
           'path': (str) mo.group(2) + '.' + mo.group(3) + '.' + mo.group(4),
           'file': (str)  mo.group(5),
           'date': (str)  pffi.fsfi_file_date_create(str_search_line),
           'size': (str)  pffi.fsfi_file_size(str_search_line),
           'id': (str) str(int_count),
           'matrix': (str)  str_matrix})
    :param str_date_min (str) минимальная дата создания резервной копии, формат 'YYYYMMDD'.
    :param str_date_max (str) максимальная дата создания резервной копии, формат 'YYYYMMDD'.
    :param bol_reverse: (bool) тип сортировки: (True) - по убыванию, (False) - по возрастанию.
    :return: (bool) файл-журнала создан: (True) - успешно, (False) - не создан.
    """

    logger.info(plng.JD_LOGGER_START)

    try:
        # Проверка входных
        # Проверка: (str_path) - тип содержимого параметра не СТРОКА.
        if type(str_path) != str:
            logger.critical(f'{plng.JD_PRM_STR_PATH_NOT_STR}, type({str(type(str_path))})')
            raise ValueError(plng.JD_PRM_STR_PATH_NOT_STR)

        # Проверка: (str_path) - наличия пути для хранения файла-журнала.
        if not os.path.exists(str_path):
            logger.critical(f'{plng.JD_PRM_STR_PATH_NOT_FOLDER}: {str_path}')
            raise ValueError(plng.JD_PRM_STR_PATH_NOT_FOLDER)

        # Проверка: (str_file) - имя файла-журнала.
        if type(str_file) != str:
            logger.critical(f'{plng.JD_PRM_STR_FILE_NOT_STR}, type({str(type(str_file))})')
            raise ValueError(plng.JD_PRM_STR_FILE_NOT_STR)

        # TODO: добавить проверку списка словарей с данными о резервных копиях.
        # TODO: добавить проверку str_date_min минимальная дата создания резервной копии.
        # TODO: добавить проверку str_date_max максимальная дата создания резервной копии.

        # Проверка: (bol_reverse) - флаг типа файла-журнала.
        if type(bol_reverse) != bool:
            logger.critical(f'{plng.JD_PRM_BOL_RVRS_NOT_BOOL}, type({str(type(bol_reverse))})')
            raise ValueError(plng.JD_PRM_BOL_RVRS_NOT_BOOL)

        # Сортировка списка словарей с данными о резервных копиях
        lst_data_sort: list = sorted(lst_data, key=itemgetter('path'), reverse=bol_reverse)

        if len(lst_data_sort) > 0:
            # Формируем имя файла-журнала
            if bol_reverse:
                # (True) - по убыванию,
                str_jrn_file = f'{str_path}\\{str_file}-{str_date_max}_{str_date_min}.txt'
            else:
                # (False) - по возрастанию
                str_jrn_file = f'{str_path}\\{str_file}-{str_date_min}_{str_date_max}.txt'

            rpt_file = open(str_jrn_file, 'w')

            str_server = ''
            str_date = ''
            for elem_data in lst_data_sort:
                if str_date != elem_data['path']:
                    str_date = elem_data['path']
                    rpt_file.write(str_date + '\n')
                    str_server = ''

                if str_server != elem_data['server']:
                    str_server = elem_data['server']
                    rpt_file.write('\t' + str_server + '\n')

                rpt_file.write('\t\t' +
                               elem_data['file'].ljust(20) + '\t' +
                               elem_data['date'].ljust(15) + '\t' +
                               elem_data['size'].ljust(10) + '\t' +
                               elem_data['id'].ljust(10) + '\t' + '\n')
            rpt_file.close()

        else:
            logger.error(f'{plng.JD_LST_DATA_SORT_NOT_DATA}.')
            return False

    except Exception as ex:
        logger.error(f'{plng.JD_ERROR_GNR}, {ex}.')
        return False

    logger.info(plng.JD_LOGGER_FINISH)

    return True


def fsj_journal_server(str_path: str, str_file: str, lst_data: list, str_date_min: str, str_date_max: str, bol_reverse: bool) -> bool:
    """
    Запись данных в txt-файл c сортировкой по дате (прямая/обратная).
    :param str_path: (str) папка для хранения файла-журнала.
    :param str_file: (str) имя файла-журнала.
    :param lst_data: (list) список словарей с данными о резервных копиях для сохранения
           в файле-отчёте.
           Формат списка: [{запись списка: dict}, {запись списка: dict},{запись списка: dict}]
           Каждая запись списка содержит словарь с данными о резервной копии.
           Структура записи списка в формате словаря:
           'server': (str) имя сервера
           'path': (str) mo.group(2) + '.' + mo.group(3) + '.' + mo.group(4),
           'file': (str)  mo.group(5),
           'date': (str)  pffi.fsfi_file_date_create(str_search_line),
           'size': (str)  pffi.fsfi_file_size(str_search_line),
           'id': (str) str(int_count),
           'matrix': (str)  str_matrix})
    :param str_date_min (str) минимальная дата создания резервной копии, формат 'YYYYMMDD'.
    :param str_date_max (str) максимальная дата создания резервной копии, формат 'YYYYMMDD'.
    :param bol_reverse: (bool) тип сортировки: (True) - по убыванию, (False) - по возрастанию.
    :return: (bool) файл-журнала создан: (True) - успешно, (False) - не создан.
    """

    logger.info(plng.JD_LOGGER_START)

    try:
        # Проверка входных
        # Проверка: (str_path) - тип содержимого параметра не СТРОКА.
        if type(str_path) != str:
            logger.critical(f'{plng.JD_PRM_STR_PATH_NOT_STR}, type({str(type(str_path))})')
            raise ValueError(plng.JD_PRM_STR_PATH_NOT_STR)

        # Проверка: (str_path) - наличия пути для хранения файла-журнала.
        if not os.path.exists(str_path):
            logger.critical(f'{plng.JD_PRM_STR_PATH_NOT_FOLDER}: {str_path}')
            raise ValueError(plng.JD_PRM_STR_PATH_NOT_FOLDER)

        # Проверка: (str_file) - имя файла-журнала.
        if type(str_file) != str:
            logger.critical(f'{plng.JD_PRM_STR_FILE_NOT_STR}, type({str(type(str_file))})')
            raise ValueError(plng.JD_PRM_STR_FILE_NOT_STR)

        # TODO: добавить проверку списка словарей с данными о резервных копиях.
        # TODO: добавить проверку str_date_min минимальная дата создания резервной копии.
        # TODO: добавить проверку str_date_max максимальная дата создания резервной копии.

        # Проверка: (bol_reverse) - флаг типа файла-журнала.
        if type(bol_reverse) != bool:
            logger.critical(f'{plng.JD_PRM_BOL_RVRS_NOT_BOOL}, type({str(type(bol_reverse))})')
            raise ValueError(plng.JD_PRM_BOL_RVRS_NOT_BOOL)

            # Сортировка списка словарей с данными о резервных копиях
        lst_data_sort: list = sorted(lst_data, key=itemgetter('server', 'path'), reverse=bol_reverse)

        if len(lst_data_sort) > 0:
            # Формируем имя файла-журнала
            if bol_reverse:
                # (True) - по убыванию,
                str_jrn_file = f'{str_path}\\{str_file}-{str_date_max}_{str_date_min}.txt'
            else:
                # (False) - по возрастанию
                str_jrn_file = f'{str_path}\\{str_file}-{str_date_min}_{str_date_max}.txt'

            rpt_file = open(str_jrn_file, 'w')

            str_server = ''
            str_date = ''

            for elem_data in lst_data_sort:
                if str_server != elem_data['server']:
                    str_server = elem_data['server']
                    rpt_file.write(str_server + '\n')
                    str_date = ''

                if str_date != elem_data['path']:
                    str_date = elem_data['path']
                    rpt_file.write('\t' + str_date + '\n')

                rpt_file.write('\t\t' +
                               elem_data['file'].ljust(20) + '\t' +
                               elem_data['date'].ljust(15) + '\t' +
                               elem_data['size'].ljust(10) + '\t' +
                               elem_data['id'].ljust(10) + '\t' + '\n')
            rpt_file.close()

        else:
            logger.error(f'{plng.JD_LST_DATA_SORT_NOT_DATA}.')
            return False

    except Exception as ex:
        logger.error(f'{plng.JD_ERROR_GNR}, {ex}.')
        return False

    logger.info(plng.JD_LOGGER_FINISH)

    return True
