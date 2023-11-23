import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr

class GoalsFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 600, width: int = 2*480,
                 pos_x: int = 720, pos_y: int = 200) -> None:
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self.config(bg = "#000F31")

    def clear_error_messages(self) -> None:
        try:
            if len(self.error_messages) > 0:
                for message in self.error_messages:
                    message.destroy()
        except AttributeError:
            pass
    
    def place_objects(self) -> None:
        """Place objects on the frame
        """

        self.label_manage_goals = tk.Label(self,
                                           text = "Gerenciar metas",
                                           font = ("Arial", 20, "bold"),
                                           bg = "#000F31",
                                           fg = "#FEFAD2")
        self.label_manage_goals.place(x = 0, y = 20, height = 30, width = 480)
        
        # Create a button to view goals
        self.button_view_goals = tk.Button(self,
                                           text = "Visualizar metas",
                                           font = ("Arial", 20),
                                           bg = "#E29E6C",
                                           fg = "#FEFAD2")
        self.button_view_goals.place(x = 50, y = 100, height = 50, width = 380)

        # Create a button set goals
        self.button_set_goals = tk.Button(self,
                                          text = "Definir metas",
                                          font = ("Arial", 20),
                                          bg = "#E29E6C",
                                          fg = "#FEFAD2")
        self.button_set_goals.place(x = 50, y = 200, height = 50, width = 380)
        
        def view_goals() -> None:
            self.destroy()
            import student_frame_factory as sff
            self.window.change_frame(sff.StudentFrameFactory.get_frame("ViewGoalsFrame", self.window))
        
        self.button_view_goals["command"] = view_goals

        def set_goals() -> None:
            self.destroy()
            import student_frame_factory as sff
            self.window.change_frame(sff.StudentFrameFactory.get_frame("SetGoalsFrame", self.window))
        
        self.button_set_goals["command"] = set_goals

    def destroy(self) -> None:
        super().destroy()
