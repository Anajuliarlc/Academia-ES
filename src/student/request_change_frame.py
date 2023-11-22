import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.window as wd
import gui.buttons as bt
import gui.entrytext as et
import student.request_change as rc

class RequestChangeFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 960, 
                 pos_x: int = 240, pos_y: int = 200) -> None:
        super().__init__(window, height, width, pos_x, pos_y)
        self.errors = []

    def design(self) -> None:
        self.config(bg = "#000F31")

    def place_objects(self) -> None:
        title_label = tk.Label(self, text="Solicitar Alteração",
                               font=("Arial", 18, "bold"),
                               bg = "#E29E6C", fg = "#FEFAD2")
        title_label.place(x=280, y=10, width=400, height=50)

        # drop-down menu
        self.clicked = tk.StringVar()
        self.clicked.set("Motivo da solicitação")

        self.drop = tk.OptionMenu(self, self.clicked, "Alteração do professor",
                             "Alteração do horário", "Alteração do local",
                                "Alteração do tipo de aula")
        
        self.drop.config(background='#E29E6C', foreground='#FEFAD2', activebackground='#DF8350')
        self.drop.place(x=280, y=60, width=400, height=50)

        self.entry_label = tk.Label(self, text="Descreva sua situação",
                               font=("Arial", 14),
                               bg = "#E29E6C", fg = "#FEFAD2")
        self.entry_label.place(x=280, y=110, width=400, height=50)

        self.entry_text = et.EntryText(self, pos_x=280, pos_y=160, width=400, height=100)

        self.button_request_change = bt.MenuButton(text = "Enviar solicitação",
                                        window = self, pos_x = 280,
                                        pos_y = 240, width=400, height=50,
                                        command = lambda: rc.send_request(self))

    def destroy(self) -> None:
        super().destroy()

if __name__ == "__main__":
    mainframe = wd.Window(connect = False)
    RequestChangeFrame(mainframe)
    mainframe.mainloop()