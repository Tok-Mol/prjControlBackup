# Приложение Система контроля хранения резервных копий (Control Backup)

**название**: _**Control Backup**_.

**дата**: _20.05.2022_

**версия**: _01.00.00_

---

**Назначение**: 

Контроль создания резервных копий.

## Функциональность версии

+ Сканирование `Системы каталогов`, сортируя результат в списки `Работа` (для дальнейшей работы) и `Ошибки` (фиксации `Логических ошибок` в `Системе каталогов`).
+ Определять для каждого найденного файла:
  + имя, расширение;
  + размер;
  + дату создания;
+ Сохранять результаты поиска в файл-отчет.
+ Настройки программы храним в конфигурационном файле `cfg_setting.py` в виде переменных;