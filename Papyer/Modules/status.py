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




class StatusBar(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.filestorage = self.root.filestorage

        self.numberOfFiles = ttk.Label(self)
        self.numberOfFiles.grid(column = 0, row = 0, padx = 10, sticky = W)

        self.selectedFiles = ttk.Label(self, text = "Number of selected files: 0")
        self.selectedFiles.grid(column = 1, row = 0, sticky = W)

        self.columnconfigure(1, weight = 1)

        self.filesChanged()

        
    def filesChanged(self):
        self.numberOfFiles["text"] = "Number of files: {}".format(len(self.filestorage.files))


    def filesSelected(self, number):
        self.selectedFiles["text"] = "Number of selected files: {}".format(number)

        

        


        









