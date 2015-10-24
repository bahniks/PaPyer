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
from os.path import basename
from tkinter import ttk
from collections import defaultdict, OrderedDict
import os




class FileTree(ttk.Treeview):
    def __init__(self, root):
        super().__init__(root)

        self.root = root
        self.filestorage = self.root.filestorage
        
        self["columns"] = ("directory", "tags")
        self.column("#0", width = 500, anchor = "w")
        self.heading("#0", text = "Filename")
        self.column("directory", width = 400, anchor = "w")
        self.heading("directory", text = "Directory")
        self.column("tags", width = 30, anchor = "center")
        self.heading("tags", text = "Tags", command = lambda e: print("hi"))
        

##        self.filesTree.bind("<3>", lambda e: self.popUp(e))
        self.bind("<Double-1>", lambda e: self.doubleClick(e))
##        self.filesTree.tag_configure("comment", background = commentColor())         

        self.initialize()



    def initialize(self):
        "initializes the treeview containing files"
        for file, infos in self.filestorage.files.items():
            self.insert("", "end", file, text = infos[0], values = (infos[1], ""))


    def doubleClick(self, event):
        """opens either the file or the directory containing the file based on the
            column double-clicked"""
        item = self.identify("item", event.x, event.y)
        if item:
            column = self.identify("column", event.x, event.y)
            if column == "#0":
                os.startfile(item)
            elif column == "#1":
                os.startfile(os.path.split(item)[0])





##    def refresh(self):
##        "refreshes the window - i.e. redraws the tree"
##        for item in self.filesTree.get_children(""):
##            self.filesTree.delete(item)
##        if self.shownFiles == "arenafiles":
##            self.initfiles = self.fileStorage.arenafiles
##        else:
##            self.initfiles = self.fileStorage.wrongfiles            
##        self.initialize()           
##        self.root.update()
##        

##
##    def popUp(self, event):
##        "called when tree item is right-clicked on"
##        item = self.filesTree.identify("item", event.x, event.y)
##        menu = Menu(self, tearoff = 0)
##        if item and self.shownFiles == "arenafiles":
##            if item in self.fileStorage.tagged:
##                menu.add_command(label = "Remove tag", command = lambda: self.untagFun(item))
##            else:
##                menu.add_command(label = "Add tag", command = lambda: self.tagFun(item))
##            menu.add_command(label = "Add comment", command = lambda: Comment(self, item))
##            selection = self.filesTree.selection()
##            if len(selection) > 1 and any([item == file for file in selection]):
##                menu.add_command(label = "Add comments", command = lambda: Comment(self, selection))
##            menu.add_separator()
##            if self.filesTree.identify("column", event.x, event.y) == "#0" and m.files == "pair":
##                menu.add_command(label = "Open paired file",
##                                 command = lambda: self.openRoomFile(item))
##                menu.add_separator()
##            menu.add_command(label = "Show track", command = lambda: self.showTracks(item))
##        if item and self.shownFiles == "wrongfiles" and len(self.filesTree.selection()) == 2:
##            menu.add_command(label = "Pair selected", command = lambda: self.forcePair())
##        menu.post(event.x_root, event.y_root)        
##
##
##
##    def untagFun(self, file):
##        "untags the file in the argument"
##        self.fileStorage.tagged.remove(file)
##        self.filesTree.set(file, "tag", "")
##
##
##    def tagFun(self, file):
##        "tags the file in the argument"
##        self.fileStorage.tag(file)
##        self.filesTree.set(file, "tag", "x")
##
##
##    def untagFilesFun(self):
##        "untags selected files"
##        for file in self.filesTree.selection():
##            if file in self.fileStorage.tagged:
##                self.untagFun(file)
##        self.root.update()
##
##
##    def tagFilesFun(self):
##        "tags selected files"
##        for file in self.filesTree.selection():
##            if file not in self.fileStorage.tagged:
##                self.tagFun(file)
##        self.root.update()
##                
##
##
##
##    def orderByTag(self):
##        "orders files by presence of tag"
##        self.fileStorage.arenafiles.sort(key = lambda i: (i in self.fileStorage.tagged),
##                                         reverse = True)
##        self.refresh()
##            
##
##    def orderByFilename(self):
##        "orders files by filename"
##        if self.shownFiles == "arenafiles":
##            self.fileStorage.arenafiles.sort(key = lambda i: basename(i))
##        else:
##            self.fileStorage.wrongfiles.sort(key = lambda i: basename(i))
##        self.refresh()
##
##
##    def orderByDirectory(self):
##        "orders files by name of the parent directory"
##        if self.shownFiles == "arenafiles":
##            self.fileStorage.arenafiles.sort(key = lambda i: os.path.split(i)[0])
##        else:
##            self.fileStorage.wrongfiles.sort(key = lambda i: os.path.split(i)[0])
##        self.refresh()            
##            
##        
##    
##            
##
