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

import os


class Notes(Text):
    def __init__(self, root):
        super().__init__(root)
        
        self.root = root
        self.filestorage = self.root.filestorage
        self["width"] = 40
        self["state"] = "disabled"
        self.currentFile = None
        

    def changeFile(self, file):
        self["state"] = "normal"
        if self.currentFile:
            text = self.get("1.0", "end").rstrip()
            for path in self.filestorage.filenames[os.path.basename(self.currentFile)]:
                self.filestorage.files[path]["note"] = text
        self.delete("1.0", "end")
        self.insert("1.0", self.filestorage.files[file]["note"].rstrip())
        self.currentFile = file





        




   
        




