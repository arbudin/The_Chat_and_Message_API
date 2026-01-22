import logging

# Создаем логгер
logger = logging.getLogger("chat_api")
logger.setLevel(logging.INFO)

# Формат логов
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

# Логирование в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Логирование в файл
file_handler = logging.FileHandler("chat_api.log", encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
