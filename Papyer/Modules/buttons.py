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




class Buttons(Frame):
    def __init__(self, root):
        super().__init__(root)
        
        self.root = root
        self.filestorage = self.root.filestorage
        self.duplicatesVar = StringVar()
        self.duplicatesVar.set("show")

        self.duplicatesFrame = ttk.Labelframe(self, text = "Duplicates")
        self.duplicatesFrame.grid(column = 1, row = 0)

        self.duplicatesShow = ttk.Radiobutton(self.duplicatesFrame, command = self.duplicates,
                                             text = "Show", width = 10,
                                             variable = self.duplicatesVar, value = "show")
        self.duplicatesShow.grid(column = 0, row = 0)
        self.duplicatesHide = ttk.Radiobutton(self.duplicatesFrame, command = self.duplicates,
                                             text = "Hide", width = 10,
                                             variable = self.duplicatesVar, value = "hide")
        self.duplicatesHide.grid(column = 1, row = 0)
        self.duplicatesHighlight = ttk.Radiobutton(self.duplicatesFrame, command = self.duplicates,
                                             text = "Highlight", width = 10,
                                             variable = self.duplicatesVar, value = "highlight")
        self.duplicatesHighlight.grid(column = 2, row = 0)
        
        self.refreshBut = ttk.Button(self, command = self.root.refresh,
                                     text = "Refresh", width = 15)
        self.refreshBut.grid(column = 2, row = 0)

        self.columnconfigure(0, weight = 2)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        self.columnconfigure(3, weight = 2)


    def duplicates(self):
        self.root.filetree.toggleDuplicates(self.duplicatesVar.get())





        




   
        




