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

from tkinter.filedialog import askopenfilenames, askdirectory, askopenfilename
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from collections import defaultdict, OrderedDict
import os





class FileStorage:
    "class for storing files for processing"  
    def __init__(self, root):
        self.root = root
        self.files = OrderedDict()
        self.addFiles()

    def __iter__(self):
        return iter(self.files)

    def __len__(self):
        return len(self.files)

    def addFiles(self):
        base = len(self.root.base) + 1
        for content in os.walk(self.root.base):
            directory = content[0]
            for file in content[2]:
                if not "py" in os.path.splitext(file)[1]:
                    self.files[os.path.join(directory, file)] = (file, directory[base:])

        
        
        









