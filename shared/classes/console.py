import logging
import random
from pyfiglet import FigletFont
#import GlobalVariables as Global
from lab3.BLL.classes.ascii import Ascii
from pyfiglet import FigletFont, figlet_format
from shared_lib.ascii import Ascii

logger = logging.getLogger(__name__)

class Console:
    def __init__(self):
        self.ascii_art = Ascii()
        logger.info("Console initialized")
        self.__prompt()

    def __prompt(self):
        while True:
            self.ascii_art.print(is_random=True)
            choice = input("1 - Enter text\n"
                           "2 - Change font\n"
                           "3 - Change width and height\n"
                           "4 - Change color\n"
                           "5 - Save to file\n"
                           "0 - Exit\n"
                           "Your choice: ")
            match choice:
                case "1":
                    self.enter_text()
                case "2":
                    self.change_font()
                case "3":
                    self.change_width_and_height()
                case "4":
                    self.change_color()
                case "5":
                    self.save_to_file()
                case "0":
                    break
                case _:
                    print("Invalid choice, please try again.")

    def enter_text(self):
        text = input("Enter text: ")
        self.ascii_art.text = text
        logger.info(f"Text set to: {text}")

    def change_font(self):
        new_font = input("Enter the new font or type 'random': ")
        if new_font.lower() == "random":
            self.ascii_art.font = random.choice(FigletFont.getFonts())
        elif new_font in FigletFont.getFonts():
            self.ascii_art.font = new_font
        else:
            print("Invalid font")
            return
        logger.info(f"Font set to: {self.ascii_art.font}")

    def change_width_and_height(self):
        try:
            width = int(input("Enter the width: "))
            height = int(input("Enter the height: "))
            self.ascii_art.width = Ascii.verify_width(width)
            self.ascii_art.height = max(0, height)
        except ValueError:
            print("Invalid input")
        logger.info(f"Width set to: {self.ascii_art.width}, Height set to: {self.ascii_art.height}")

    def change_color(self):
        color_prompt = input("Enter color code (e.g., '\\033[31m' for red) or 'default': ")
        self.ascii_art.color = color_prompt if color_prompt != "default" else "\033[39m"
        logger.info(f"Color set to: {self.ascii_art.color}")

    def save_to_file(self):
        file_name = input("Enter file name: ")
        self.ascii_art.save_art(file_name)
