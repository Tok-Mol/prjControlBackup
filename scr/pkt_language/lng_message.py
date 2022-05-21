# scr/main.py
MN_LOGGER_START = "Старт приложения Control Backup v.01.00.00, 20.05.2022."
MN_LOGGER_RESULT = "Результат>> всего: {0}, ошибок: {1}, даты: {2}"
MN_LOGGER_FINISH = "Окончание работы приложения Control Backup v.01.00.00, 20.05.2022."

# scr/pkt_filesystem/fs_storage_scan.py
# > def fsss_storage_scan(str_path: str, str_search: str) -> (list, list, list):
SS_LOGGER_START = "Старт сканирования ХРАНИЛИЩА."
SS_PRM_STR_PATH_NOT_STR = "Аргумент (str_path: путь к папке Хранилища) должен быть строкой."
SS_PRM_STR_PATH_NOT_FOLDER = "Папка Хранилища не существует."
SS_PRM_STR_SEARCH_NOT_STR = "Аргумент (str_search: строка поиска) должен быть строкой."
SS_ERROR_SCAN = "Ошибка сканирования"
SS_LOGGER_RESULT = "Результат сканирования ХРАНИЛИЩА:"
SS_LOGGER_FINISH = "Окончание сканирования ХРАНИЛИЩА."

# scr/pkt_filesystem/fs_files_info.py
# > fsfi_file_date_create(str_file_name: str) -> str:
FD_PRM_STR_FILE_NAME_NOT_STR = "Аргумент (str_file_name: путь файлу) должен быть строкой."
FD_PRM_STR_FILE_NAME_NOT_FILE = "Файл не обнаружен."
FD_ERROR = "Ошибка определения даты создания файла"
# > fsfi_file_size(str_file_name: str) -> str:
FS_PRM_STR_FILE_NAME_NOT_STR = "Аргумент (str_file_name: путь файлу) должен быть строкой."
FS_PRM_STR_FILE_NAME_NOT_FILE = "Файл не обнаружен."
FS_ERROR = "Ошибка определения размера файла"

