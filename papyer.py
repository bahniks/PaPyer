#! python3
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


from tkinter import messagebox
from tkinter import *

import os
import sys



def makeRoot():
    "makes root window for messagebox"
    root = Tk()
    root.withdraw()
    return root


def main():
    "starts CMM"
    modules = os.path.join(os.getcwd(), "Papyer", "Modules")
       
    # starting
    try:
        if modules not in sys.path:
            sys.path.append(modules)
        from starter import main as start
    except Exception as e:
        root = makeRoot()
        messagebox.showinfo(title = "Error", icon = "error", detail = e,
                            message = "Unable to start PaPyer! Try again.")
        root.destroy()
    else:
        start()

        
        
if __name__ == "__main__": main()

