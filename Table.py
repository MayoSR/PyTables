import colorama
from colorama import Fore, Style, Back
import random

color_map = {
    "WHITE": Fore.WHITE,
    "BLUE": Fore.BLUE,
    "GREEN": Fore.GREEN,
    "BLACK": Fore.BLACK,
    "RED": Fore.RED,
    "YELLOW": Fore.YELLOW,
    "CYAN": Fore.CYAN,
    "MAGENTA": Fore.MAGENTA,
    "LIGHTBLACK": Fore.LIGHTBLACK_EX,
    "LIGHTBLUE": Fore.LIGHTBLUE_EX,
    "LIGHTCYAN": Fore.LIGHTCYAN_EX,
    "LIGHTGREEN": Fore.LIGHTGREEN_EX,
    "LIGHTMAGENTA": Fore.LIGHTMAGENTA_EX,
    "LIGHTRED": Fore.LIGHTRED_EX,
    "LIGHTWHITE": Fore.LIGHTWHITE_EX,
    "LIGHTYELLOW": Fore.LIGHTYELLOW_EX,
    "reset": Fore.RESET
}

brightness_map = {
    "BRIGHT": Style.BRIGHT,
    "NORMAL": Style.NORMAL,
    "DIM": Style.DIM
}

background_map = {
    "WHITE": Back.WHITE,
    "BLUE": Back.BLUE,
    "GREEN": Back.GREEN,
    "BLACK": Back.BLACK,
    "RED": Back.RED,
    "YELLOW": Back.YELLOW,
    "CYAN": Back.CYAN,
    "MAGENTA": Back.MAGENTA,
    "LIGHTBLACK": Back.LIGHTBLACK_EX,
    "LIGHTBLUE": Back.LIGHTBLUE_EX,
    "LIGHTCYAN": Back.LIGHTCYAN_EX,
    "LIGHTGREEN": Back.LIGHTGREEN_EX,
    "LIGHTMAGENTA": Back.LIGHTMAGENTA_EX,
    "LIGHTRED": Back.LIGHTRED_EX,
    "LIGHTWHITE": Back.LIGHTWHITE_EX,
    "LIGHTYELLOW": Back.LIGHTYELLOW_EX,
    "reset": Back.RESET
}

default_color_set = Fore.WHITE


class Table(object):

    def __init__(self, headers):
        self.max_cell_size_by_column = [0 for i in range(len(headers))]
        self.table_len = len(headers)
        self.table = []
        self.add_row(headers, header=True)
        self.body_color = "WHITE"
        self.header_color = "WHITE"
        self.border_color = "WHITE"
        self.background_color = None

    def add_row(self, row, header=False):

        self.table.append([TableCell(header, i, random.choice(list(color_map.keys())), random.choice(
            list(background_map.keys())), random.choice(list(brightness_map.keys()))) for i in row])

    def check_max_cell_size_by_column(self):

        for i in self.table:
            col_ind = 0
            for j in i:
                self.max_cell_size_by_column[col_ind] = j.get_text_length() if j.get_text_length(
                ) > self.max_cell_size_by_column[col_ind] else self.max_cell_size_by_column[col_ind]
                col_ind += 1

    def display(self):
        self.check_max_cell_size_by_column()
        print(color_map[self.border_color]+"+"+(sum([i+2 for i in self.max_cell_size_by_column]) +
                                                self.table_len - 1)*"-"+"+")
        for i in enumerate(self.table):
            for j in enumerate(i[1]):
                print("| "+j[1].get_pretty_text()+" " *
                      (self.max_cell_size_by_column[j[0]] - j[1].get_text_length())+ background_map["reset"]+" ", end="")
            print("|")
            print(color_map[self.border_color]+"+"+(sum([i+2 for i in self.max_cell_size_by_column]
                                                        )+self.table_len - 1)*"-"+"+")


class TableCell(object):

    def __init__(self, header, text, color=default_color_set, bg=default_color_set, style=default_color_set):
        self.text = text
        self.color = color
        self.bg = bg
        self.style = style
        self.header = header
        self.pretty_text = None
        self.set_styles_to_text()

    def get_text_length(self):
        return len(self.text)

    def get_text(self):
        return str(self.text)

    def set_styles_to_text(self):
        self.pretty_text = color_map[self.color] + background_map[self.bg] + \
            brightness_map[self.style] + self.text + color_map["reset"]
            
    def get_pretty_text(self):
        return self.pretty_text

    def set_text(self, text):
        self.pretty_text.replace(self.text,text)
        self.text = text
        self.set_styles_to_text()

    def set_color(self, color):
        self.color = color
        self.set_styles_to_text()

    def set_bg(self, bg):
        self.bg = bg
        self.set_styles_to_text()

    def set_style(self, style):
        self.style = style
        self.set_styles_to_text()


table = Table(["hello", "world", "what", "is", "happening"])
table.add_row(["23", "43", "55", "112", "42545"])
table.add_row(["22333", "3445", "None", "23434", "545555"])
table.add_row(["2352455", "79797", "9998", "2352455", "213422"])
table.display()
