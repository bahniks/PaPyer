#! python3
"""
Copyright 2015 Štěpán Bahník

This file is part of PaPyer.

PaPyer is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PaPyer is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with PaPyer.  If not, see <http://www.gnu.org/licenses/>.
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#from time import localtime, strftime

import os
#import sys


from window import placeWindow
from filestorage import FileStorage
from filetree import FileTree
from selection import Select
from buttons import Buttons



class GUI(Tk):
    "represents GUI"
    def __init__(self):
        super().__init__()
   
        self.option_add("*tearOff", FALSE)
        self.initialized = False
        self.title("Papyer")
        
        x, y = 800, 300
        self.minsize(x, y)
        placeWindow(self, x, y)

        self["menu"] = Menu(self)

        self.protocol("WM_DELETE_WINDOW", self.closeFun)

        self.base = os.getcwd()

        self.selectVar = StringVar()
        self.selectLabel = ttk.Label(self, text = "Select:")
        self.selectLabel.grid(column = 0, row = 0, padx = 10, pady = 5)
        self.select = Select(self, textvariable = self.selectVar)
        self.select.grid(column = 1, row = 0, sticky = (E, W))

        self.searchVar = StringVar()
        self.searchLabel = ttk.Label(self, text = "Search:")
        self.searchLabel.grid(column = 2, row = 0, padx = 10, pady = 5)
        self.search = ttk.Entry(self, textvariable = self.searchVar)
        self.search.grid(column = 3, row = 0, sticky = (E, W))

        self.filestorage = FileStorage(self)
        self.filetree = FileTree(self)
        self.filetree.grid(column = 0, row = 1, sticky = (N, S, E, W), columnspan = 4)

        self.scrollbar = ttk.Scrollbar(self, orient = VERTICAL, command = self.filetree.yview)
        self.scrollbar.grid(column = 4, row = 1, sticky = (N, S, E))
        self.filetree.configure(yscrollcommand = self.scrollbar.set)

        self.columnconfigure(1, weight = 1)
        self.columnconfigure(3, weight = 1)
        self.rowconfigure(1, weight = 1)

        self.buttons = Buttons(self)
        self.buttons.grid(row = 2, column = 0, columnspan = 5, pady = 5)

        self.mainloop()



    def closeFun(self):
        "ask for saving files on exit"
        self.filestorage.save()
        self.destroy()




     
            

def main():
    GUI()


if __name__ == "__main__":
    main()
