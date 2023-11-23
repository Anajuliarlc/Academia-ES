import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import student.student_frame_factory as sff
from gui.buttons import DefaultButton

class GoalsFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 480,
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
        
        def view_goals() -> None:
            self.destroy()
            sff.StudentFrameFactory.get_frame("ViewGoalsFrame", self.window)

        def set_goals() -> None:
            self.destroy()
            sff.StudentFrameFactory.get_frame("SetGoalsFrame", self.window)

        # Create a button to view goals
        self.button_view_goals = DefaultButton(text = "Visualizar metas",
                                               command = view_goals,
                                               window = self,
                                               pos_x = 80, pos_y = 140,
                                               height = 50, width = 340)
        
        # Create a button set goals
        self.button_set_goals = DefaultButton(text = "Definir metas",
                                              command = set_goals,
                                              window = self,
                                              pos_x = 80, pos_y = 240,
                                              height = 50, width = 340)
        

    def destroy(self) -> None:
        super().destroy()
