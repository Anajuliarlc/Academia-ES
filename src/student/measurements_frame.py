import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr

class MeasurementsFrame(fr.Frame):  
    def update_db(self, measurements: dict) -> bool:
        pass