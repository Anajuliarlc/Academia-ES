import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import student.student_frame_factory as sff
from gui.buttons import DefaultButton

class GoalsFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 480,
                 pos_x: int = 720, pos_y: int = 200) -> None:
        """Initializes the GoalsFrame class.

        :param window: The Tkinter window object.
        :type window: tk.Tk
        :param height: The height of the frame, defaults to 400.
        :type height: int, optional
        :param width: The width of the frame, defaults to 480.
        :type width: int, optional
        :param pos_x: The x-coordinate position of the frame, defaults to 720.
        :type pos_x: int, optional
        :param pos_y: The y-coordinate position of the frame, defaults to 200.
        :type pos_y: int, optional
        """
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        """Sets the design of the GoalsFrame.
        """
        self.config(bg = "#000F31")

    def clear_error_messages(self) -> None:
        """ Clears any error messages displayed on the frame.

        >>> import student.student_frame_factory as sff
        >>> frame = sff.StudentFrameFactory.get_frame("GoalsFrame", tk.Tk())
        >>> frame.error_messages = [tk.Label(frame, text="Error 1"), tk.Label(frame, text="Error 2")]
        >>> frame.clear_error_messages()
        >>> frame.error_messages
        []
        """
        try:
            if len(self.error_messages) > 0:
                for message in self.error_messages:
                    message.destroy()
        except AttributeError:
            pass
    
    def place_objects(self) -> None:
        """Places objects on the GoalsFrame.
        """

        self.label_manage_goals = tk.Label(self,
                                           text = "Gerenciar metas",
                                           font = ("Arial", 20, "bold"),
                                           bg = "#000F31",
                                           fg = "#FEFAD2")
        self.label_manage_goals.place(x = 0, y = 20, height = 30, width = 480)
        
        def view_goals() -> None:
            """Displays the ViewGoalsFrame.
            """
            self.destroy()
            sff.StudentFrameFactory.get_frame("ViewGoalsFrame", self.window)

        def set_goals() -> None:
            """Displays the SetGoalsFrame.
            """
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
        """Destroys the GoalsFrame.
        """
        super().destroy()

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)