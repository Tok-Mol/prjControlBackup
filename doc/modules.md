# Приложение Система контроля хранения резервных копий (Control Backup). Описание пакетов, модулей.

**название**: _**Control Backup**_.

**дата**: _20.05.2022_

**версия**: _01.00.00_

---
## Файловая структура приложения.

```text
prjControlBackup
│   readme.md
├───doc
│       control_backup.md
│       document.md
│       installation.md
│       modules.md
│       quickstart.md
│       
└───scr
    │   main.py
    │   __init__.py
    │   
    ├───logs
    │       control_backup.log
    │       
    ├───pkt_config
    │       cfg_setting.py
    │       __init__.py
    │           
    ├───pkt_filesystem
    │       fs_files_info.py
    │       fs_logging.py
    │       fs_storage_scan.py
    │       __init__.py
    │           
    └───pkt_language
            lng_message.py
            __init__.py
```


## Список пакетов.

- _pkt_config_ -  
- _pkt_filesystem_ -  
- _pkt_language_ -

## pkt_config

### cfg_setting.py

- CFG_NAME 
- CFG_VERSION 
- CFG_DATE 
- CFG_STRG_PATH 
- CFG_STRG_SEARCH

## pkt_filesystem

### fs_files_info.py

- logger 
- fsfi_file_date_create 
- fsfi_file_size

### fs_logging.py

- get_logging_dict_config

### fs_storage_scan.py

- logger 
- fsss_storage_scan

## pkt_language

### lng_message.py

- SS_LOGGER_START
- SS_PRM_STR_PATH_NOT_STR
- SS_PRM_STR_PATH_NOT_FOLDER
- SS_PRM_STR_SEARCH_NOT_STR
- SS_ERROR_SCAN
- SS_LOGGER_RESULT
- SS_LOGGER_FINISH
- FD_PRM_STR_FILE_NAME_NOT_STR
- FD_PRM_STR_FILE_NAME_NOT_FILE
- FD_ERROR
- FS_PRM_STR_FILE_NAME_NOT_STR
- FS_PRM_STR_FILE_NAME_NOT_FILE
- FS_ERROR