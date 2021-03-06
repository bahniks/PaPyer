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

from window import placeWindow



class TopMenu(Menu):
    def __init__(self, root):
        super().__init__(root)
        self.root = root

        self.menuFile = Menu(self)
        self.menuOptions = Menu(self)
        self.menuAbout = Menu(self)

        self.capitalizationVar = BooleanVar()
        if not self.root.options["capitalization"]:
            self.root.options["capitalization"] = False
        self.capitalizationVar.set(self.root.options["capitalization"])

        menuWidth = 8
        self.add_cascade(menu = self.menuFile, label = "{:^{}}".format("File", menuWidth))
        self.add_cascade(menu = self.menuOptions, label = "{:^{}}".format("Options", menuWidth))
        self.add_cascade(menu = self.menuAbout, label = "{:^{}}".format("About", menuWidth))

        self.menuFile.add_command(label = "Close", command = self.root.closeFun)

        self.menuOptions.add_command(label = "Add label", command = self.addLabel)
        self.menuOptions.add_separator()
        self.menuOptions.add_command(label = "Settings", command = self.openSettings)
        self.menuOptions.add_separator()
        self.menuOptions.add_checkbutton(label = "Ignore capitalization", command = self.capitalization,
                                         variable = self.capitalizationVar) 

        self.menuAbout.add_command(label = "About", command = self.about)
        self.menuAbout.add_command(label = "Version", command = self.version)


    def addLabel(self):
        Labels(self.root)

    def capitalization(self):
        self.update()
        self.root.options["capitalization"] = not self.capitalizationVar.get()

    def openSettings(self):
        pass

    def version(self):
        pass

    def about(self):
        pass


class Popup(Toplevel):
    def __init__(self, root, name):
        super().__init__(root)

        self.root = root
        self.title = name
        self.grab_set()
        self.focus_set()     
        self.resizable(False, False)

        self.buttonFrame = ttk.Frame(self)
        self.buttonFrame.grid(column = 0, row = 1)

        self.okBut = ttk.Button(self, text = "Ok", command = self.okFun)
        self.closeBut = ttk.Button(self, text = "Close", command = self.closeFun)
        
        self.okBut.grid(column = 3, row = 2, pady = 2)
        self.closeBut.grid(column = 2, row = 2, pady = 2)

    def okFun(self):
        pass

    def closeFun(self):
        self.destroy()


        
class Labels(Popup):
    def __init__(self, root):
        super().__init__(root, "Add label")
        placeWindow(self, 598, 208)

        self.var = StringVar()
        tags = [tag for tag in tuple(sorted(self.root.filestorage.getAllTags())) if
                tag not in self.root.options["tags"]]
        self.combo = ttk.Combobox(self, textvariable = self.var, values = tags)
        self.combo.grid(column = 2, columnspan = 2, row = 1)

    def okFun(self):
        new = self.var.get()
        if new:
            self.root.options["tags"].append(new)
            self.root.options["columnwidths"][new] = 60
            self.root.refresh()
        self.destroy()
        









