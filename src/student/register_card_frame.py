import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.buttons as bt
import student.register_card as rc

class RegisterCardFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 960, 
                 pos_x: int = 240, pos_y: int = 200) -> None:
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self.config(bg = "#000F31")

    def place_objects(self) -> None:
        self.title_label = tk.Label(self, text = "Registar Novo Cartão", font = ("Arial", 24, "bold"), 
                                    bg = "#E29E6C", fg = "#FEFAD2")
        self.title_label.place(x = 180, y = 0, width=600)

        self.name_label = tk.Label(self, text = "Nome no Cartão",
                                    font = ("Arial", 14), bg = "#E29E6C",
                                    fg = "#FEFAD2")
        self.name_label.place(x = 180, y = 50, width=200, height=50)

        self.name_entry = tk.Entry(self, font = ("Arial", 14), bg = "#E29E6C",
                                    fg = "#FEFAD2")
        self.name_entry.place(x = 380, y = 50, width=400, height=50)

        self.card_num_label = tk.Label(self, text = "Número do Cartão",
                                    font = ("Arial", 14), bg = "#E29E6C",
                                    fg = "#FEFAD2")
        self.card_num_label.place(x = 180, y = 100, width=200, height=50)

        self.card_num_entry = tk.Entry(self, font = ("Arial", 14), bg = "#E29E6C",
                                    fg = "#FEFAD2")
        self.card_num_entry.place(x = 380, y = 100, width=400, height=50)

        self.card_type_label = tk.Label(self, text = "Tipo do Cartão",
                                    font = ("Arial", 14), bg = "#E29E6C",
                                    fg = "#FEFAD2")
        self.card_type_label.place(x = 180, y = 150, width=200, height=50)

        # drop-down menu
        self.clicked = tk.StringVar()
        self.clicked.set("Tipo do Cartão")

        self.drop = tk.OptionMenu(self, self.clicked, "Crédito", "Débito")
        
        self.drop.config(background='#E29E6C', foreground='#FEFAD2', activebackground='#DF8350')
        self.drop.place(x=380, y=150, width=400, height=50)

        self.card_date_label = tk.Label(self, text = "Data de Validade",
                                    font = ("Arial", 14), bg = "#E29E6C",
                                    fg = "#FEFAD2")
        self.card_date_label.place(x = 180, y = 200, width=200, height=50)

        self.card_date_entry = tk.Entry(self, font = ("Arial", 14), bg = "#E29E6C",
                                    fg = "#FEFAD2")
        self.card_date_entry.place(x = 380, y = 200, width=400, height=50)

        self.card_cvv_label = tk.Label(self, text = "CVV",
                                    font = ("Arial", 14), bg = "#E29E6C",
                                    fg = "#FEFAD2")
        self.card_cvv_label.place(x = 180, y = 250, width=200, height=50)

        self.card_cvv_entry = tk.Entry(self, font = ("Arial", 14), bg = "#E29E6C",
                                    fg = "#FEFAD2")
        self.card_cvv_entry.place(x = 380, y = 250, width=400, height=50)

        self.button_register_card = bt.MenuButton(text = "Registrar Cartão",
                                        command = lambda: rc.send_request(self),
                                        window = self, pos_x = 180, pos_y = 310,
                                        width=600, height=50)

    def destroy(self) -> None:
        super().destroy()