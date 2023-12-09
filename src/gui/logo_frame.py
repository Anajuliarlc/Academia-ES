import tkinter as tk
import sys  
sys.path.append("./src")
import gui.frame as fr
import gui.window as wd


class LogoFrame(fr.Frame):
    """
    >>> root = tk.Tk()
    >>> root.active_frames = []
    >>> frame = LogoFrame(root, 200, 1200, 0, 0)
    >>> frame.pos_x, frame.pos_y, frame.width, frame.height
    (0, 0, 1200, 200)
    >>> frame in root.active_frames
    True
    """
    def __init__(self, window: tk.Tk, height: int = 200, width: int = 1200,
                  pos_x: int = 0, pos_y: int = 0) -> None:
        """Create a frame to be used as login in the application """
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self.config(bg = "#000F31")
        pass

    def place_objects(self) -> None:
        logo = tk.PhotoImage(file = "img/logo.png")
        width_logo = logo.width() // 100
        height_logo = logo.height() // 100
        logo = logo.subsample(width_logo, height_logo)
        logo_label = tk.Label(self, image = logo)
        logo_label.config(bd = 0)
        logo_label.image = logo
        logo_label.place(x = 550, y = 5)

        name_label = tk.Label(self, text = "Chi-Trapézio", font = ("Arial", 32, "bold"), 
                              bg = "#000F31", fg = "#DF8350")
        name_label.place(x = 470, y = 100)

    def destroy(self) -> None:
        super().destroy()


if __name__ == "__main__":
    # mainframe = wd.Window(connect = False)
    # LogoFrame(mainframe)
    # mainframe.mainloop()

    import doctest
    doctest.testmod(verbose=True)