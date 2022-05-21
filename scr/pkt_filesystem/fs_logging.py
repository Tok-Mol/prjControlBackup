def get_logging_dict_config():
    return {
        "version": 1,
        "formatters": {
            "detailed": {
                "format": "%(asctime)s - %(name)s:%(lineno)s - %(levelname)s - %(message)s"
            }
        },
        "handlers": {
            "std": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "detailed"
            },
            "file": {
                "class": "logging.FileHandler",
                "level": "DEBUG",
                "formatter": "detailed",
                "encoding": "utf8",
                "filename": "logs/control_backup.log"
            }
        },
        "loggers": {
            "app": {
                "handlers": ["std", "file"],
                "level": "DEBUG"
            }
        }
    }
