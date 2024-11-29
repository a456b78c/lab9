import os
import math
import logging
import random
import string
from pyfiglet import figlet_format, FigletFont
from lab4.Shared.classes.validators import Validators
from lab4.Shared.classes.incorrect_character_exception import IncorrectCharacterException
#import logger
logger = logging.getLogger(__name__)

class Ascii:
    def __init__(self, global_vars, text="", width=0, height=0, color="random", shadow="#", text_s="#", highlight="#", justify="left", validators=None, font_path=None):
        self.global_vars = global_vars
        self.text = text
        self.width = self.verify_width(width)
        self.height = height
        self.color = "\033[" + str(random.randint(31, 39)) + "m" if color == "random" else color
        self.color_reset = "\033[0m"
        self.shadow = shadow
        self.text_s = text_s
        self.highlight = highlight
        self.justify = justify
        self.validators = validators
        self.font = self.load_font(font_path) if font_path else None
        logger.info("Initialized Ascii class with parameters: text='%s', width=%d, height=%d, color='%s'", text, width, height, color)

    def print(self, is_random=False):
        if is_random:
            font = random.choice(FigletFont.getFonts())
            color = "\033[" + str(random.randint(31, 39)) + "m"
            logger.debug("Random font and color selected: font='%s', color='%s'", font, color)
        else:
            font = self.global_vars.font if hasattr(self.global_vars, 'font') else None
            color = self.global_vars.color if hasattr(self.global_vars, 'color') else self.color

        art = figlet_format(self.text, font=font, width=self.width)
        art = self.apply_padding(art)
        print(color + art + self.color_reset)
        logger.info("Generated ASCII art for text='%s'", self.text)
        return art

    def apply_padding(self, art):
        art_lines = art.splitlines()
        art_height = len(art_lines)
        height_diff = self.height - art_height
        padding = "\n" * (height_diff // 2) if height_diff > 0 else ""
        logger.debug("Applied padding to ASCII art")
        return padding + art + padding

    def verify_width(self, width):
        if width <= 0:
            try:
                return os.get_terminal_size().columns
            except OSError:
                return 220
        return width

    def load_font(self, font_path):
        if not font_path:
            return None
        keys = (list(string.ascii_uppercase) + list(string.digits) +
                ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=",
                 "+", "[", "]", ";", ":", "'", '"', ",", ".", "/", "<", ">", "?", " "])
        font = {}
        with open(font_path, "r") as file:
            i = 0
            for line in file:
                if line.strip() == "$":
                    i += 1
                elif i < len(keys):
                    key = keys[i]
                    font[key] = font.get(key, "") + line
        logger.info("Loaded font from path='%s'", font_path)
        return font
