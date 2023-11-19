import pandas as pd
import re

import sys 
import os
sys.path.append(os.path.abspath("./src")) # Adds src directory to python modules path.

import exc.exceptions as exc

# Temporary class while we don't have a database
class Access:
    def __init__(self, path: str) -> None:
        self.path = path
        self.table = None
        self.update()
    
    def update(self) -> None:
        self.table = pd.read_csv(self.path)

    def write(self) -> None:
        self.table.to_csv(self.path, index=False)

    def select(self, username: str) -> pd.DataFrame:
        return self.table[self.table['username'] == username]
    
    def insert(self, username: str, password: str) -> None:
        self.table = self.table.append({'CPF': username, 'Password': password}, ignore_index=True)
        self.update()
