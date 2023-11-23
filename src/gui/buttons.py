import tkinter as tk
import sys  
sys.path.append("./src")

class MenuButton(tk.Button):
    def __init__(self, text, command, window, pos_x, pos_y, width = 200, height = 50):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        super().__init__(window, text = text, font = ("Arial", 18), 
                                    bg = "#E29E6C", fg = "#FEFAD2", borderwidth=2, 
                                    highlightbackground="#000F31", 
                                    command = command)
        self.place(x = self.pos_x, y = self.pos_y, width = self.width, height = self.height)
    

class DefaultButton(tk.Button):
    def __init__(self, text, command, window, pos_x, pos_y, width = 400, height = 150, font = ("Arial", 28)):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        super().__init__(window, text = text, font = font, 
                                    bg = "#E29E6C", fg = "#FEFAD2", borderwidth=2, 
                                    highlightbackground="#000F31", 
                                    command = command)
        self.place(x = self.pos_x, y = self.pos_y, width = self.width, height = self.height)
   

"""
COMENTÁRIO PARA APAGAR DEPOIS:

Cores usadas:
    #DF8350 - Laranja escuro
    #FEFAD2 - Bege
    #E29E6C - Laranja claro
    #000F31 - Azul escuro
    
no botão padrão de 400x150, a fonte é Arial 28, mas se quiserem, dá pra mudar tbm
na tela de Progresso do Aluno, recomendo que seja 300x100 e fonte Arial 28 tbm"""