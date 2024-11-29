import os
import logging

class FileStorage:
    def __init__(self, default_dir="Uploads"):
        # Ініціалізуємо директорію за замовчуванням
        self.default_dir = default_dir
        if not os.path.exists(self.default_dir):
            os.makedirs(self.default_dir)
    
    def save_to_file(self, data, file_name="output.txt"):
        """ Зберігає дані у файл. """
        file_path = os.path.join(self.default_dir, file_name)

        try:
            with open(file_path, 'w') as file:
                file.write(data)
            logging.info(f"Data saved to {file_path}")
            print(f"Data saved successfully to {file_path}")
        except IOError as e:
            logging.error(f"File save error: {e}")
            raise IOError("The file could not be uploaded, please try again")

    def read_from_file(self, file_name="output.txt"):
        """ Читає дані з файлу. """
        file_path = os.path.join(self.default_dir, file_name)
        try:
            with open(file_path, 'r') as file:
                data = file.read()
            logging.info(f"Data read from {file_path}")
            return data
        except IOError as e:
            logging.error(f"File read error: {e}")
            raise IOError("The file could not be read, please check if the file exists")

    def delete_file(self, file_name="output.txt"):
        """ Видаляє файл за вказаним шляхом. """
        file_path = os.path.join(self.default_dir, file_name)
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                logging.info(f"File {file_path} deleted successfully.")
                print(f"File {file_path} deleted successfully.")
            else:
                print(f"File {file_path} does not exist.")
                logging.warning(f"Attempted to delete non-existing file: {file_path}")
        except Exception as e:
            logging.error(f"Error deleting file: {e}")
            raise IOError("An error occurred while attempting to delete the file.")
