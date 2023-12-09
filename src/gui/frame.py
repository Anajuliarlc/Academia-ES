from abc import ABC, abstractmethod
import tkinter as tk
import sys
sys.path.append("./src")

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
        self.window.active_frames.append(self)

        self.design()
        self.place_objects()

        self.place(x = self.pos_x, y = self.pos_y,
                    height = self.height, width = self.width)
    
    @abstractmethod
    def design(self) -> None:       
        pass

    @abstractmethod
    def place_objects(self) -> None:
        pass

    @abstractmethod
    def destroy(self) -> None:
        super().destroy()
        self.window.active_frames.remove(self)

class FrameNotFound(ValueError):
    def __init__(self) -> None:
        """Raise when the frame type is not implemented"""        
        super().__init__("Frame not found")

class ExampleFrame(Frame):
    """
    >>> root = tk.Tk()
    >>> root.active_frames = []
    >>> frame = ExampleFrame(root, 600, 800, 0, 0)
    >>> frame.pos_x, frame.pos_y, frame.width, frame.height
    (0, 0, 800, 600)
    >>> frame in root.active_frames
    True
    """
    def __init__(self, window: tk.Tk, height: int = 600, width: int = 800,
                  pos_x: int = 0, pos_y: int = 0) -> None:
        """Create a frame to be used as example in the application """
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self["bg"] = "red"

    def place_objects(self) -> None:
        self.label = tk.Label(self, text = "Example Frame", font = ("Arial", 20))
        self.button = tk.Button(self, text = "Change Label")
        self.entry = tk.Entry(self)
        
        def change_label() -> None:
            self.label.config(text = self.entry.get())

        self.button["command"] = change_label

        self.label.place(x = 20, y = 20, height = 40, width = 200)
        self.button.place(x = 20, y = 60, height = 40, width = 200)
        self.entry.place(x = 20, y = 100, height = 40, width = 200)
        

    def destroy(self) -> None:
        super().destroy()
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()