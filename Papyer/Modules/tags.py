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


class Tags(ttk.Entry):
    def __init__(self, root):
        super().__init__(root)
        
        self.root = root
        self.filestorage = self.root.filestorage
        self.var = StringVar()
        self.currentFile = None
        self["width"] = 40
        self["textvariable"] = self.var
        self["state"] = "disabled"

        self.bind("<Tab>", lambda e: self.complete())
        

    def changeFile(self, file):
        self["state"] = "!disabled"
        if self.currentFile:
            tags = {tag.strip() for tag in self.var.get().split(",") if tag.strip()}
            labels = {label for label in self.root.options["tags"] if
                      label in self.filestorage.files[self.currentFile]["tags"]}
            tags |= labels
            for path in self.filestorage.filenames[os.path.basename(self.currentFile)]:
                self.filestorage.files[path]["tags"] = tags
                if path in self.root.filetree.get_children():                    
                    for tag in self.root.options["tags"]:
                        if tag in tags:
                            self.root.filetree.set(path, tag, "x")
                        else:
                            self.root.filetree.set(path, tag, "")
                    
        new = [tag for tag in self.filestorage.files[file]["tags"] if tag not in self.root.options["tags"]]
        self.var.set(", ".join(sorted(new)))
        self.currentFile = file


    def complete(self):
        last = self.var.get().split(",")[-1].lstrip()
        if last:
            tags = self.filestorage.getAllTags()
            fit = [tag for tag in tags if tag.startswith(last)]
            if len(fit) == 1:
                new = self.var.get()[0:-len(last)] + fit[0] + ", "
                self.var.set(new)
                self.icursor(len(self.var.get()))
        return "break"





        




   
        




