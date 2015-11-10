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

import os

from window import placeWindow
from filestorage import FileStorage
from filetree import FileTree
from selection import Select
from buttons import Buttons
from menu import TopMenu
from options import Options
from notes import Notes
from status import StatusBar
from tags import Tags



class GUI(Tk):
    "represents GUI"
    def __init__(self):
        super().__init__()
   
        self.option_add("*tearOff", FALSE)
        self.initialized = False
        self.title("Papyer")
        
        x, y = 1500, 500
        self.minsize(x, y)
        placeWindow(self, x, y)


        self.options = Options(self)
        self["menu"] = TopMenu(self)        

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
        self.filetree.grid(column = 0, row = 1, rowspan = 4, sticky = (N, S, E, W), columnspan = 4)

        self.scrollbar = ttk.Scrollbar(self, orient = VERTICAL, command = self.filetree.yview)
        self.scrollbar.grid(column = 4, row = 1, rowspan = 4, sticky = (N, S, E))
        self.filetree.configure(yscrollcommand = self.scrollbar.set)

        self.tags = Tags(self)
        self.tags.grid(column = 5, row = 2, sticky = (E, W), padx = 5)

        self.tagsLab = ttk.Label(text = "Tags")
        self.tagsLab.grid(column = 5, row = 1, padx = 5, pady = 2)

        self.notes = Notes(self)
        self.notes.grid(column = 5, row = 4, sticky = (N, S, E, W), padx = 5)

        self.notesLab = ttk.Label(text = "Notes")
        self.notesLab.grid(column = 5, row = 3, padx = 5, pady = 2)

        self.scrollNotes = ttk.Scrollbar(self, orient = VERTICAL, command = self.notes.yview)
        self.scrollNotes.grid(column = 6, row = 4, sticky = (N, S, W))
        self.notes.configure(yscrollcommand = self.scrollNotes.set)

        self.buttons = Buttons(self)
        self.buttons.grid(row = 5, column = 0, columnspan = 5, pady = 5, sticky = (E, W))

        self.statusBar = StatusBar(self)
        self.statusBar.grid(row = 6, column = 0, columnspan = 5, padx = 5, pady = 5, sticky = (E, W))

        self.columnconfigure(1, weight = 1)
        self.columnconfigure(3, weight = 1)
        self.columnconfigure(5, weight = 1)
        self.rowconfigure(4, weight = 1)

        self.bind("<Control-d>", lambda e: self.filetree.keepDuplicates())
        self.bind("<Control-a>", lambda e: self.filetree.selectAll())
        
 
        self.mainloop()



    def refresh(self):
        # do in a smarter way - check changes in the files
        self.filestorage.save()
        self.filestorage = FileStorage(self)
        self.filetree = FileTree(self)
        self.filetree.grid(column = 0, row = 1, rowspan = 2, sticky = (N, S, E, W), columnspan = 4)
        self.tags = Tags(self)
        self.tags.grid(column = 5, row = 2, sticky = (E, W), padx = 5)
        self.notes = Notes(self)
        self.notes.grid(column = 5, row = 4, sticky = (N, S, E, W), padx = 5)
        self.statusBar = StatusBar(self)
        self.statusBar.grid(row = 6, column = 0, columnspan = 5, padx = 5, pady = 5, sticky = (E, W))
        

    def closeFun(self):
        "ask for saving files on exit"
        self.filestorage.save()
        self.options.save()
        self.destroy()




     
            

def main():
    GUI()


if __name__ == "__main__":
    main()
