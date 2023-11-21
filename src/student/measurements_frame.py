import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr

class MeasurementsFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 600, width: int = 800, pos_x: int = 0, pos_y: int = 0) -> None:
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        pass

    def place_objects(self) -> None:
        pass

    def destroy(self) -> None:
        pass
    
    def update_db(self, measurements: dict) -> bool:
        pass