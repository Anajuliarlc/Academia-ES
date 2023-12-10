import sys
sys.path.append("./src")

import tkinter as tk
import pandas as pd

import gui.frame as fr
import gui.window as wd
import gui.buttons as bt
import student.student_frame_factory as sff
import main

class ProfileFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 960, 
                 pos_x: int = 240, pos_y: int = 200) -> None:
        """Initialize the ProfileFrame class.

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

    def design(self) -> None:
        """Design the ProfileFrame.
        """
        self.config(bg = "#000F31")

    def button_register_card(self):
        """Handle the button click event to register a card.
        """
        for frame in self.window.active_frames:
            if type(frame).__name__ != "MenuFrame" and type(frame).__name__ != "LogoFrame":
                frame.destroy()
        sff.StudentFrameFactory.get_frame("RegisterCardFrame", frame.window)

    def place_objects(self) -> None:
        """Place the objects in the ProfileFrame.
        """
        system = main.System()
        student_info = system.database.select("Student", "*", f"Where IdUser = {system.user}")
        user_info = system.database.select("User", "*", f"Where IdUser = {system.user}")

        person_info = pd.concat([student_info, user_info], axis = 1)
        
        blurred_cpf = person_info["CPF"][0][:3] + ".***" * 2 + "-**"

        self.info_label = tk.Label(self, text = f"\nNome: {person_info['UserName'][0]}\n\n" +
                                                f"Data de Nascimento: {person_info['BirthDate'][0]}\n\n" +
                                                f"Estado: {person_info['State'][0]}\n\n" +
                                                f"Cidade: {person_info['City'][0]}\n\n" +
                                                f"Telefone: {person_info['PhoneNumber'][0]}\n\n" +
                                                f"CPF: {blurred_cpf}\n",
                                                font = ("Arial", 16, "bold"), 
                                                bg = "#E29E6C", fg = "#FEFAD2",
                                                justify="left")
        
        self.info_label.place(x = 60, y = 50, width=400)

        card_info = system.database.select("Card", "CardNum, CardType", f"Where IdUser = {system.user}")

        blurred_card_num = card_info["CardNum"][0][:4] + " ****" * 3

        self.card_info_label = tk.Label(self, text = f"\nCartão: {blurred_card_num}\n\n" +
                                                f"Tipo: {card_info['CardType'][0]}\n",
                                                font = ("Arial", 16, "bold"), 
                                                bg = "#E29E6C", fg = "#FEFAD2",
                                                justify="left")
        self.card_info_label.place(x = 560, y = 50, width=300)
    
        self.button_register_card = bt.DefaultButton(text = "Registrar Cartão",
                                        command = self.button_register_card,
                                        window = self, pos_x = 560, pos_y = 220,
                                        width=300)
        
        self.button_register_card.config(background='#E29E6C',
                                         foreground='#FEFAD2',
                                         activebackground='#DF8350',
                                         borderwidth=5)
        

    def destroy(self) -> None:
        """Destroy the ProfileFrame.
        """
        super().destroy()

if __name__ == "__main__":
    mainframe = wd.Window()
    ProfileFrame(mainframe)
    mainframe.mainloop()