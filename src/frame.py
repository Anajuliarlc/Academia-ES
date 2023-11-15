from abc import ABC, abstractmethod
import tkinter as tk

class Frame(ABC, tk.Frame):

    def __init__(self, window: tk.Tk, height: int = 600, width: int = 800,
                  pos_x: int = 0, pos_y: int = 0) -> None:
        """Create a frame to be used in the application

        :param window: Window that will contain the frame
        :type window: tk.Tk
        :param height: Height of the frame, defaults to 600
        :type height: int, optional
        :param width: Width of the frame, defaults to 800
        :type width: int, optional
        :param pos_x: Position x of the frame on window, defaults to 0
        :type pos_x: int, optional
        :param pos_y: Position y of the frame on window, defaults to 0
        :type pos_y: int, optional
        """        
        super().__init__(window)
        self.window = window
        self.height = height
        self.width = width
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.desing()
        self.place_objects()

        self.place(x = self.pos_x, y = self.pos_y,
                    height = self.height, width = self.width)
    
    @abstractmethod
    def desing(self) -> None:       
        pass

    @abstractmethod
    def place_objects(self) -> None:
        pass

    @abstractmethod
    def destroy(self) -> None:
        pass