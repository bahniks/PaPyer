#! python3
"""
Copyright 2015 Štěpán Bahník

This file is part of Papyer.

Carousel Maze Manager is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Carousel Maze Manager is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Papyer.  If not, see <http://www.gnu.org/licenses/>.
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



class GUI(Tk):
    "represents GUI"
    def __init__(self):
        super().__init__()
   
        self.option_add("*tearOff", FALSE)
        self.resizable(FALSE, FALSE)
        self.initialized = False
        self.title("Papyer")
        
        '''
        # used when size of the window is changed for placeWindow arguments     
        self.after(250, lambda: print(self.winfo_width()))
        self.after(250, lambda: print(self.winfo_height()))
        '''
        x, y = 1120, 810
        self.minsize(x, y)
        placeWindow(self, x, y)

        self["menu"] = Menu(self)

        self.protocol("WM_DELETE_WINDOW", self.closeFun)

        self.base = os.getcwd()

        self.filestorage = FileStorage(self)
        self.filetree = FileTree(self)
        self.filetree.grid(column = 0, row = 0, sticky = (N, S, E, W))

        self.scrollbar = ttk.Scrollbar(self, orient = VERTICAL, command = self.filetree.yview)
        self.scrollbar.grid(column = 1, row = 0, sticky = (N, S, E))
        self.filetree.configure(yscrollcommand = self.scrollbar.set)

        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        self.mainloop()



    def closeFun(self):
        "ask for saving files on exit"
        self.destroy()




     
            

def main():
    GUI()


if __name__ == "__main__":
    main()
