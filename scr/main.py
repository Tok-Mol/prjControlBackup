# import logging
import logging.config
import scr.pkt_config.cfg_setting as pcfg
import scr.pkt_language.lng_message as plng
import scr.pkt_filesystem.fs_logging as pfsl
import scr.pkt_filesystem.fs_storage_scan as pfss

# Загрузка конфигурации из кода словаря
logging.config.dictConfig(pfsl.get_logging_dict_config())
logger: logging = logging.getLogger("app.main")

if __name__ == '__main__':
    logger.info(f'{plng.MN_LOGGER_START}')

    lst_storage: list = []
    lst_storage_error: list = []
    lst_storage_date: list = []
    lst_storage, lst_storage_error, lst_storage_date = pfss.fsss_storage_scan(
        pcfg.CFG_STRG_PATH, pcfg.CFG_STRG_SEARCH)

    logger.debug(plng.MN_LOGGER_RESULT.format(len(lst_storage), len(lst_storage_error), len(lst_storage_date)))
    logger.info(f'{plng.MN_LOGGER_FINISH}')
