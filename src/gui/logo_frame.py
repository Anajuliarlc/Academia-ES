import tkinter as tk
import sys  
sys.path.append("./src")
import gui.frame as fr
import gui.window as wd


class LogoFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 200, width: int = 1200,
                  pos_x: int = 0, pos_y: int = 0) -> None:
        """
        Initializes the LogoFrame class.

        :param window: The Tkinter window object.
        :type window: tk.Tk
        :param height: The height of the frame, defaults to 200.
        :type height: int, optional
        :param width: The width of the frame, defaults to 1200.
        :type width: int, optional
        :param pos_x: The x-coordinate position of the frame, defaults to 0.
        :type pos_x: int, optional
        :param pos_y: The y-coordinate position of the frame, defaults to 0.
        :type pos_y: int, optional
        """
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        """
        This method sets the background color of the frame to "#000F31".
        """
        self.config(bg = "#000F31")

    def place_objects(self) -> None:
        """Place the objects in the logo frame.

        This method is responsible for placing the logo image and name label in the logo frame.
        """

        logo = tk.PhotoImage(file="img/logo.png")
        width_logo = logo.width() // 100
        height_logo = logo.height() // 100
        logo = logo.subsample(width_logo, height_logo)
        logo_label = tk.Label(self, image=logo)
        logo_label.config(bd=0)
        logo_label.image = logo
        logo_label.place(x=550, y=5)

        name_label = tk.Label(
            self,
            text="Chi-Trapézio",
            font=("Arial", 32, "bold"),
            bg="#000F31",
            fg="#DF8350"
        )
        name_label.place(x=470, y=100)

    def destroy(self) -> None:
        """Destroys the logo frame.
        """
        super().destroy()

if __name__ == "__main__":
    mainframe = wd.Window()
    LogoFrame(mainframe)
    mainframe.mainloop()

