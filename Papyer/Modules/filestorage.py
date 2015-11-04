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

#from tkinter.filedialog import askopenfilenames, askdirectory, askopenfilename
from tkinter import *
#from tkinter import messagebox
from tkinter import ttk
from collections import OrderedDict
import os
import pickle


#File = namedtuple("File", ["file", "dir", "tags"])


class FileStorage:
    "class for storing files for processing"  
    def __init__(self, root):
        self.root = root
        self.files = OrderedDict()
        self.load()
        self.addFiles()

    def __iter__(self):
        return iter(self.files)

    def __len__(self):
        return len(self.files)
    
    def items(self):
        return self.files.items()

    def load(self):
        path = os.path.join(os.getcwd(), "papyer.data")
        if os.path.exists(path):
            with open(path, mode = "rb") as f:
                self.loaded = pickle.load(f)
        else:
            self.loaded = {}
    
    def addFiles(self):
        unique = {}
        self.duplicates = set()
        base = len(self.root.base) + 1
        count = 1
        for content in os.walk(self.root.base):
            directory = content[0]
            for file in content[2]:
                if not "py" in os.path.splitext(file)[1]:
                    path = os.path.normpath(os.path.join(directory, file))
                    if file in self.loaded:
                        tags = self.loaded[file]["tags"]
                        note = self.loaded[file]["note"]
                    else:
                        tags = set()
                        note = ""
                    self.files[path] = {"file": file,
                                        "dir": directory[base:],
                                        "tags": tags,
                                        "note": note}
                    if not file in unique:
                        unique[file] = path
                    else:
                        self.duplicates.add(path)
                        self.duplicates.add(unique[file])
                    count += 1

    def save(self):
        path = os.path.join(os.getcwd(), "papyer.data")
        if os.path.exists(path):
            os.remove(path)
        store = {}
        for file in self.files.values():
            filename = file["file"]
            store[file["file"]] = {"tags": file["tags"],
                                   "note": file["note"]}
        with open(path, mode = "wb") as f:
            pickle.dump(store, file = f)
        
        



        
        
        









