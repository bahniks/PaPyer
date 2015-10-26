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
#from os.path import basename
from tkinter import ttk
from collections import OrderedDict
import os




class FileTree(ttk.Treeview):
    def __init__(self, root):
        super().__init__(root)

        self.root = root
        self.filestorage = self.root.filestorage

        self.labels = ["Read", "Problem"] # load from a file
        
        self["columns"] = ["directory"] + self.labels
        self.column("#0", width = 400, anchor = "w")
        self.heading("#0", text = "Filename", command = self.orderByFilename)
        self.column("directory", width = 300, anchor = "w")
        self.heading("directory", text = "Directory", command = self.orderByDirectory)
        for label in self.labels:
            self.column(label, width = 60, anchor = "center")
            self.heading(label, text = label)
        

        self.bind("<1>", lambda e: self.clicked(e))
        self.bind("<Double-1>", lambda e: self.doubleClick(e))
        self.tag_configure("duplicate", background = "white")
        self.duplicatesShown = False

        self.initialize()



    def initialize(self):
        "initializes the treeview containing files"
        for file, info in self.filestorage.items():
            tags = self.getTags(file)
            self.insert("", "end", file, text = info["file"], values = (info["dir"], ""), tag = tags)


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


    def clicked(self, event):
        item = self.identify("item", event.x, event.y)
        if item:
            column = self.column(self.identify("column", event.x, event.y), "id")
            if column in self.labels:
                if not column in self.filestorage.files[item]["tags"]:
                    self.set(item, column, "x")
                    self.filestorage.files[item]["tags"].add(column)
                else:
                    self.set(item, column, "")
                    self.filestorage.files[item]["tags"].remove(column)

                    
    def getTags(self, file):
        if file in self.filestorage.duplicates:
            tags = "duplicate"
        else:
            tags = ""
        return tags    
                


    def leave(self, letters):
        self.delete(*self.get_children())
        for file, info in self.filestorage.items():
            if info["file"].startswith(letters):
                tags = self.getTags(file)
                self.insert("", "end", file, text = info["file"],
                            values = (info["dir"], ""), tag = tags)


    def toggleDuplicates(self):
        if self.duplicatesShown:
            self.tag_configure("duplicate", background = "white")
            self.duplicatesShown = False
        else:
            self.tag_configure("duplicate", background = "yellow")
            self.duplicatesShown = True
 

    def orderByFilename(self):
        "orders files by filename"
        self.filestorage.files = OrderedDict(sorted(self.filestorage.files.items(),
                                                    key = lambda i: i[1]["file"]))        
        self.refresh() 


    def orderByDirectory(self):
        "orders files by name of the parent directory"
        self.filestorage.files = OrderedDict(sorted(self.filestorage.files.items(),
                                                    key = lambda i: i[1]["dir"]))
        self.refresh()


    def refresh(self):
        self.delete(*self.get_children())
        self.initialize()




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
       
##            
##        
##    
##            
##
