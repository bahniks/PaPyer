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

def placeWindow(window, windowWidth = 200, windowHeight = 300, xShift = 0, yShift = -30):
    "moves the window to the center of a screen"    
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    xPosition = int((screenWidth - windowWidth) / 2) + xShift
    yPosition = max(int((screenHeight - windowHeight) / 2) + yShift, 10)
    window.geometry("+" + str(xPosition) + "+" + str(yPosition))
