import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.buttons as bt

class ThankYouFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 960, 
                 pos_x: int = 240, pos_y: int = 200) -> None:
        """Initialize the ThankYouFrame class.

        :param window: The Tkinter window object.
        :type window: tk.Tk
        :param height: The height of the frame, defaults to 400.
        :type height: int, optional
        :param width: The width of the frame, defaults to 960.
        :type width: int, optional
        :param pos_x: The x-coordinate position of the frame, defaults to 240.
        :type pos_x: int, optional
        :param pos_y: The y-coordinate position of the frame, defaults to 200.
        :type pos_y: int, optional
        """
        super().__init__(window, height, width, pos_x, pos_y)
        self.errors = []

    def design(self) -> None:
        """Design the ThankYouFrame."""
        self.config(bg = "#000F31")

    def place_objects(self) -> None:
        """Place objects in the ThankYouFrame."""
        title_label = tk.Label(self, text="Obrigado!",
                               font=("Arial", 18, "bold"),
                               bg = "#E29E6C", fg = "#FEFAD2")
        title_label.place(x=280, y=10, width=400, height=50)

        message_label = tk.Label(self, text="Sua solicitação foi enviada com sucesso!",
                                 font=("Arial", 14),
                                 bg = "#E29E6C", fg = "#FEFAD2")
        message_label.place(x=280, y=60, width=400, height=50)

        conclude_button = bt.DefaultButton(text = "Concluir",
                                           command = self.destroy,
                                           window = self, pos_x = 280, pos_y = 120,
                                           width=400)

    def destroy(self) -> None:
        """Destroy the ThankYouFrame."""
        super().destroy()
    