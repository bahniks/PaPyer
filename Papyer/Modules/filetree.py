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
from tkinter import messagebox
from tkinter import ttk
from collections import OrderedDict
import os

from menu import Popup
from window import placeWindow



class FileTree(ttk.Treeview):
    def __init__(self, root):
        super().__init__(root)

        self.root = root
        self.filestorage = self.root.filestorage
        self.options = self.root.options

        self["columns"] = ["directory", "type", "size"] + self.options["tags"]
        if not self.options["columnwidths"]:
            self.options["columnwidths"] = {tag:60 for tag in self.options["tags"]}
            self.options["columnwidths"]["#0"] = 400
            self.options["columnwidths"]["directory"] = 300
            self.options["columnwidths"]["type"] = 60
            self.options["columnwidths"]["size"] = 60
        self.column("#0", width = self.options["columnwidths"]["#0"], anchor = "w")
        self.heading("#0", text = "Filename", command = self.orderByFilename)
        self.column("directory", width = self.options["columnwidths"]["directory"], anchor = "w")
        self.heading("directory", text = "Directory", command = self.orderByDirectory)
        self.column("type", width = self.options["columnwidths"]["type"], anchor = "w")
        self.heading("type", text = "Type")
        self.column("size", width = self.options["columnwidths"]["size"], anchor = "e")
        self.heading("size", text = "Size")
        for label in self.options["tags"]:
            self.column(label, width = self.options["columnwidths"][label], anchor = "center")
            self.heading(label, text = label)
        
        self.bind("<1>", lambda e: self.clicked(e))
        self.bind("<Double-1>", lambda e: self.doubleClick(e))
        self.bind("<Control-a>", lambda e: self.selectAll())
        self.bind("<3>", lambda e: self.rightClicked(e))
        self.bind("<Delete>", lambda e: self.deleteFile())
        self.bind("<<TreeviewSelect>>", self.onSelection)
        
        self.tag_configure("duplicate", background = "white")
        
        self.duplicatesShown = False
        self.onlyDuplicates = False
        self.conditions = []
        self.filters = {}
        self.ordering = None

        self.initialize()


    def saveSettings(self):
        for col in self.options["tags"] + ["#0", "directory", "type", "size"]:
            try:
                self.options["columnwidths"][col] = self.column(col, "width")
            except Exception:
                pass


    def initialize(self):
        "initializes the treeview containing files"
        for file, info in self.filestorage.items():
            for condition in self.conditions:
                if not condition(file):
                    break
            else:
                tags = self.getTags(file)
                name, typ = os.path.splitext(info["file"])
                size = filesize(os.path.getsize(file))
                self.insert("", "end", file, text = name,
                            values = (info["dir"], typ[1:], size), tag = tags)
                for tag in info["tags"]:
                    if tag in self.options["tags"]:
                        self.set(file, tag, "x")


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
        region = self.identify("region", event.x, event.y)
        column = self.column(self.identify("column", event.x, event.y), "id")
        if item:
            if column in self.options["tags"]:
                if not column in self.filestorage.files[item]["tags"]:
                    for path in self.filestorage.filenames[os.path.basename(item)]:
                        self.set(path, column, "x")
                        self.filestorage.files[path]["tags"].add(column)
                else:
                    for path in self.filestorage.filenames[os.path.basename(item)]:
                        self.set(path, column, "")
                        try:
                            self.filestorage.files[path]["tags"].remove(column)
                        except KeyError:
                            pass
            self.root.notes.changeFile(item)
            self.root.tags.changeFile(item)
        elif region == "heading":
            if column in self.options["tags"]:
                self.orderByTag(column)
                

    def rightClicked(self, event):
        "called when tree item is right-clicked on"
        item = self.identify("item", event.x, event.y)
        region = self.identify("region", event.x, event.y)
        menu = Menu(self, tearoff = 0)
        column = self.column(self.identify("column", event.x, event.y), "id")
        if item:
            if not column:
                selected = self.selection()
                if item in selected and len(selected) > 1:                                        
                    menu.add_command(label = "Delete files", command = lambda: self.deleteFile())
                else:
                    self.selection_set('"{}"'.format(item.replace("\\", "\\\\")))
                    menu.add_command(label = "Delete file", command = lambda: self.deleteFile())
                    menu.add_command(label = "Rename file", command = lambda: self.renameFile())
        elif region == "heading":
            if column in self.options["tags"]:
                if column not in self.filters:
                    menu.add_command(label = "Leave only tagged", command = lambda: self.leaveTagged(column))
                else:
                    menu.add_command(label = "Show all", command = lambda: self.leaveTagged(column))
                menu.add_command(label = "Remove column", command = lambda: self.removeLabel(column))
        else:
            return
        menu.post(event.x_root, event.y_root)        


    def onSelection(self, e):
        self.root.statusBar.filesSelected()


    def selectAll(self):
        if len(self.selection()) == len(self.get_children()):
            self.selection_remove(self.get_children())
        else:
            self.selection_set(self.get_children())

                    
    def getTags(self, file):
        if os.path.basename(file) in self.filestorage.duplicates:
            tags = "duplicate"
        else:
            tags = ""
        return tags    
                

    def leave(self, letters, previous = []):
        def beginningWith(file):
            if self.options["capitalization"]:
                return self.filestorage.files[file]["file"].startswith(letters)
            else:
                return self.filestorage.files[file]["file"].lower().startswith(letters.lower())
        if previous:
            self.conditions.remove(previous.pop(0))
        self.conditions.append(beginningWith)
        previous.append(beginningWith)
        self.refresh()


    def find(self, letters, previous = []):
        def search(file):
            if self.options["capitalization"]:
                return letters in self.filestorage.files[file]["file"]
            else:
                return letters.lower() in self.filestorage.files[file]["file"].lower()
        if previous:
            self.conditions.remove(previous.pop(0))
        self.conditions.append(search)
        previous.append(search)
        self.refresh()


    def leaveTagged(self, tag):
        if tag not in self.filters:
            fun = lambda file: tag in self.filestorage.files[file]["tags"]
            self.conditions.append(fun)
            self.filters[tag] = fun
        else:
            self.conditions.remove(self.filters.pop(tag))
        self.refresh()
        

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
                                                    key = lambda i: i[1]["file"].lower()))     
        self.refresh()
        self.ordering = self.orderByFilename


    def orderByDirectory(self):
        "orders files by name of the parent directory"
        self.filestorage.files = OrderedDict(sorted(self.filestorage.files.items(),
                                                    key = lambda i: i[1]["dir"]))
        self.refresh()
        self.ordering = self.orderByDirectory


    def orderByTag(self, tag):
        self.filestorage.files = OrderedDict(reversed(sorted(self.filestorage.files.items(),
                                                             key = lambda i: tag in i[1]["tags"])))
        self.refresh()
        self.ordering = lambda: self.orderByTag(tag)


    def refresh(self):
        selected = self.selection()
        self.delete(*self.get_children())
        self.initialize()
        self.root.statusBar.shownChanged()
        self.root.statusBar.filesSelected()
        if self.ordering:
            temp = self.ordering
            self.ordering = None
            temp()
        if len(selected) == 1 and selected[0] in self.get_children():
            self.selection_set('"{}"'.format(selected[0].replace("\\", "\\\\")))
            

    def removeLabel(self, label):
        self.root.options["tags"].remove(label)
        self.root.refresh()
               

    def deleteFile(self):
        plural = "s" if len(self.selection()) > 1 else ""
        text = "Are you sure you want to delete the file{}?".format(plural)
        answ = messagebox.askyesno(message = text, icon = "question",
                                   title = "Delete file{}?".format(plural))
        if answ:
            for file in self.selection():
                os.remove(file)
                self.filestorage.removeFile(file)
        self.refresh()


    def renameFile(self):
        Rename(self.root, self.selection()[0])


    def keepDuplicates(self):
        if self.onlyDuplicates:
            self.conditions.remove(self.onlyDuplicates)
            self.onlyDuplicates = None
        else:
            self.onlyDuplicates = lambda f: (self.filestorage.files[f]["file"] in
                                             self.filestorage.duplicates)
            self.conditions.append(self.onlyDuplicates)
        self.refresh()



class Rename(Popup):
    def __init__(self, root, file):
        super().__init__(root, "Rename file")
        placeWindow(self, 598, 208)

        self.file = file

        self.nameVar = StringVar()
        self.nameVar.set(os.path.splitext(os.path.basename(file))[0])
        self.name = ttk.Entry(self, textvariable = self.nameVar, width = 50)
        self.name.grid(column = 2, columnspan = 2, row = 1, sticky = (E, W), pady = 5)


    def okFun(self):
        path, base = os.path.split(self.file)
        if "." in self.nameVar.get():
            newname = os.path.join(path, self.nameVar.get())
        else:
            newname = os.path.join(path, self.nameVar.get() + os.path.splitext(base)[1])
        os.rename(self.file, newname)
        self.root.filestorage.renameFile(self.file, newname)
        self.root.filetree.refresh()
        self.destroy()

    



def filesize(size, remainder = 0, order = 0):
    sizes = ["B", "KB", "MB", "GB", "TB", "PB", "EB"]
    if size // 1024 == 0:
        return "{}{}".format(size, sizes[order])
    else:
        return filesize(size // 1024, size % 1024, order + 1)

    
