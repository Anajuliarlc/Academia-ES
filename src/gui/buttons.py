import tkinter as tk
import sys  
sys.path.append("./src")

class MenuButton(tk.Button):
    """
    >>> root = tk.Tk()
    >>> button = MenuButton("Menu", lambda: print("Clicked"), root, 10, 20, 200, 50)
    >>> button.pos_x, button.pos_y, button.width, button.height
    (10, 20, 200, 50)
    """
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
    """
    >>> root = tk.Tk()
    >>> button = DefaultButton("Default", lambda: print("Clicked"), root, 10, 20, 300, 120)
    >>> button.pos_x, button.pos_y, button.width, button.height
    (10, 20, 300, 120)
    """
    def __init__(self, text, command, window, pos_x, pos_y, width = 300, height = 120, font = ("Arial", 28)):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        super().__init__(window, text = text, font = font, 
                                    bg = "#E29E6C", fg = "#FEFAD2", borderwidth=2, 
                                    highlightbackground="#000F31", 
                                    command = command)
        self.place(x = self.pos_x, y = self.pos_y, width = self.width, height = self.height)
   
if __name__ == "__main__":
    import doctest
    doctest.testmod()

"""
COMENTÁRIO PARA APAGAR DEPOIS:

Cores usadas:
    #DF8350 - Laranja escuro
    #FEFAD2 - Bege
    #E29E6C - Laranja claro
    #000F31 - Azul escuro
    
no botão padrão de 300x120, a fonte é Arial 28, mas se quiserem, dá pra mudar tbm 
tanto tamanho do botão, tanto o tamnho da font"""