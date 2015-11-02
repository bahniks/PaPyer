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


import pickle
import os


class Options(dict):
    def __init__(self, root):
        path = os.path.join(os.getcwd(), "papyer.options")
        if os.path.exists(path):
            with open(path, mode = "rb") as f:
                content = pickle.load(f)
                for key, value in content.items():
                    self[key] = value
        else:
            self["tags"] = []
           

    def save(self):
        path = os.path.join(os.getcwd(), "papyer.options")
        with open(path, mode = "wb") as f:
            content = {}
            for key, value in self.items():
                content[key] = value
            pickle.dump(content, f)
            
            
        




        
        
        









