import colorama
from colorama import Fore, Style, Back

class Table(object):

    color_map = {"WHITE": Fore.WHITE, "BLUE": Fore.BLUE, "GREEN": Fore.GREEN,
                 "BLACK": Fore.BLACK, "RED": Fore.RED, "YELLOW": Fore.YELLOW, "CYAN": Fore.CYAN, "MAGENTA": Fore.MAGENTA, "LIGHTBLACK": Fore.LIGHTBLACK_EX, "LIGHTBLUE": Fore.LIGHTBLUE_EX, "LIGHTCYAN": Fore.LIGHTCYAN_EX, "LIGHTGREEN": Fore.LIGHTGREEN_EX, "LIGHTMAGENTA": Fore.LIGHTMAGENTA_EX, "LIGHTRED": Fore.LIGHTRED_EX, "LIGHTWHITE": Fore.LIGHTWHITE_EX, "LIGHTYELLOW": Fore.LIGHTYELLOW_EX, "reset": Fore.RESET}

    def __init__(self, headers):
        self.max_cell_size_by_column = [0 for i in range(len(headers))]
        self.table = [headers]
        self.body_color = "WHITE"
        self.header_color = "WHITE"
        self.border_color = "WHITE"
        self.background_color = None

    def add_row(self, row):
        self.table.append(row)

    def check_max_cell_size_by_column(self):

        for i in self.table:
            col_ind = 0
            for j in i:
                self.max_cell_size_by_column[col_ind] = len(j) if len(
                    j) > self.max_cell_size_by_column[col_ind] else self.max_cell_size_by_column[col_ind]
                col_ind += 1

    def print_row(self, text, header=False):
        if header:
            print("| "+(Table.color_map[self.header_color] + str(text[1]) + Table.color_map["reset"])+" "*(self.max_cell_size_by_column[text[0]] - len(str(text[1])) + 1), end="")
        else:
            print("| "+(Table.color_map[self.body_color] + str(text[1]) + Table.color_map["reset"])+" "*(self.max_cell_size_by_column[text[0]] - len(str(text[1])) + 1), end="")
        

    def display(self):
        self.check_max_cell_size_by_column()
        print(Table.color_map[self.border_color]+"+"+(sum([i+2 for i in self.max_cell_size_by_column]
                                                          )+len(self.table[0]) - 1)*"-"+"+"+Table.color_map["reset"])
        for i in enumerate(self.table):
            for j in enumerate(i[1]):
                if i[0] == 0:
                    self.print_row(j, True)
                else:
                    self.print_row(j)
            print("|"+Table.color_map["reset"])
            print(Table.color_map[self.border_color]+"+"+(sum([i+2 for i in self.max_cell_size_by_column]
                                                              )+len(self.table[0]) - 1)*"-"+"+"+Table.color_map["reset"])

    def coloumn_headers(self,headers):
        pass
    
    def styles(self, header_color="WHITE", body_color="WHITE", border_color="WHITE", background_color=None):
        self.body_color = body_color.upper()
        self.border_color = border_color.upper()
        self.background_color = background_color
        self.header_color = header_color.upper()

class TableCell(object):
    pass

table = Table(["hello", "world", "what", "is", "happening"])
table.add_row(["23", "43", "55", "112", "42545"])
table.add_row(["22333", "3445", "None", "23434", "545555"])
table.add_row(["2352455", "79797", "9998", "2352455", "213422"])
table.styles(header_color="green", body_color="RED")
table.display()
