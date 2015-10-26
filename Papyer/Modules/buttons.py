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

        self.duplicatesBut = ttk.Button(self, command = self.duplicates,
                                        text = "Show duplicates", width = 15)
        self.duplicatesBut.grid(column = 0, row = 0)


    def duplicates(self):
        self.root.filetree.toggleDuplicates()
        if self.root.filetree.duplicatesShown:
            self.duplicatesBut["text"] = "Hide duplicates"
        else:
            self.duplicatesBut["text"] = "Show duplicates"





   
        




