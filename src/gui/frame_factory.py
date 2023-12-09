from abc import ABC, abstractmethod
import tkinter as tk

class FrameFactory(ABC):

    def __init__(self, type_, window: tk.Tk, height: int = 600, width: int = 800,
                  pos_x: int = 0, pos_y: int = 0) -> None:
        """Manage the creation of a frame to be used in the application

        :param type_: Type of frame to be created
        :type type_: str
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
        self.frame = self.get_frame(type_, window, height, width, pos_x, pos_y)

    @staticmethod
    @abstractmethod
    def get_frame(type_:str, window: tk.Tk, height: int = 600, width: int = 800,
                  pos_x: int = 0, pos_y: int = 0) -> 'fr.Frame':
        """Create a frame to be used in the application
        
        :param type_: Type of frame to be created
        :type type_: str
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
        pass

    def destroy(self) -> None:
        self.frame.destroy()


class TestFrameFactory(FrameFactory):
    """ Solely for testing purposes
    
    >>> root = tk.Tk()
    >>> factory = TestFrameFactory("test", root)
    >>> factory.frame
    <tkinter.Frame object ...>
    >>> factory.destroy()
    """
    @staticmethod
    def get_frame(type_:str, window: tk.Tk, height: int = 600, width: int = 800,
                  pos_x: int = 0, pos_y: int = 0) -> 'fr.Frame':
        return tk.Frame(window, height=height, width=width)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)