import logging

# Налаштування логування
logging.basicConfig(
    filename='app.log',  # Лог-файл
    filemode='a',        # Додає логи до існуючого файлу
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
