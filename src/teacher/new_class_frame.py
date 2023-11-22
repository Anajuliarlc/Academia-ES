import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.window as wd
import teacher.teacher_frame_factory as tff
import gui.entrytext as et
import gui.buttons as bt
import main

class NewClass(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 960,
                  pos_x: int = 240, pos_y: int = 200) -> None:
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self.config(bg = "#000F31")

    def place_objects(self) -> None:
        label = tk.Label(self, text = "Nova aula", font = ("Arial", 24, "bold"),
                         bg = "#000F31", fg = "#FEFAD2")
        
        label.place(x = 400, y = 30, width = 150, height = 30)
        name_label = tk.Label(self, text = "Nome:", font = ("Arial", 16, "bold"),
                              bg = "#000F31", fg = "#FEFAD2")
        name_label.place(x = 200, y = 100, width = 100, height = 30)
        self.name_entry = et.EntryText(self, font = ("Arial", 16, "bold"),
                                        pos_x = 300, pos_y = 100,
                                        width = 400, height = 40)

        date_label = tk.Label(self, text = "Data:", font = ("Arial", 16, "bold"),
                              bg = "#000F31", fg = "#FEFAD2")
        date_label.place(x = 200, y = 160, width = 100, height = 30)
        self.date_entry = et.EntryText(self, font = ("Arial", 16, "bold"),
                                        pos_x = 300, pos_y = 160,
                                        width = 400, height = 40)

        description_label = tk.Label(self, text = "Descrição:",
                                     font = ("Arial", 16, "bold"),
                                     bg = "#000F31", fg = "#FEFAD2")
        description_label.place(x = 180, y = 220, width = 120, height = 30)
        self.description_entry = et.EntryText(self, font = ("Arial", 16, "bold"),
                                                pos_x = 300, pos_y = 220,
                                                width = 400, height = 40)

        create_button = bt.DefaultButton(text = "Criar",
                                         command = self.destroy,
                                         window = self, pos_x = 350, pos_y = 300,
                                         font = ("Arial", 16, "bold"),
                                         width = 100, height = 30)
    
        cancel_button = bt.DefaultButton(text = "Cancelar",
                                         command = self.destroy,
                                         window = self, pos_x = 550, pos_y = 300,
                                         font = ("Arial", 16, "bold"),
                                         width = 100, height = 30)

    def destroy(self) -> None:
        super().destroy()


if __name__ == "__main__":
    window = wd.Window(connect = False)
    frame = NewClass(window)
    window.mainloop()