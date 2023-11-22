import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr

class SetGoalsFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 600, width: int = 800,
                 pos_x: int = 0, pos_y: int = 0) -> None:
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        pass

    def clear_error_messages(self) -> None:
        try:
            if len(self.error_messages) > 0:
                for message in self.error_messages:
                    message.destroy()
        except AttributeError:
            pass
    
    def place_objects(self) -> None:
        self.label = tk.Label(self, text="Definir metas de treino", font=("Arial", 20))
        self.label_goal_name = tk.Label(self, text = "Nome da meta")
        self.entry_goal_name = tk.Entry(self)

        self.clicked_time = tk.StringVar()
        self.clicked_time.set("Prazo da meta")

        self.label_goal_time = tk.Label(self, text = "Prazo da meta")
        self.entry_goal_time = tk.Entry(self)
        self.drop_goal_time = tk.OptionMenu(
            self, self.clicked_time,
            "Dias",
            "Semanas",
            "Meses",
            "Semestres",
            "Anos",
        )

        self.label_goal_description = tk.Label(self, text = "Descrição da\nmeta")
        self.entry_goal_description = tk.Entry(self)

        self.button = tk.Button(self, text = "Definir meta")
        
        self.clicked_type = tk.StringVar()
        self.clicked_type.set("Tipo de meta")

        self.label_goal_type = tk.Label(self, text = "Tipo de meta")
        self.drop_goal_type = tk.OptionMenu(
            self, self.clicked_type,
            "Perda de peso",
            "Ganho de massa muscular",
            "Melhora de condicionamento físico",
            "Melhora de flexibilidade e mobilidade",
            "Melhora de resistência cardiovascular",
            "Desempenho esportivo",
            "Saúde e bem-estar em geral",
            "Outro",
        )
        
        def set_goals() -> None:
            self.clear_error_messages()
            self.error_messages = []

            if self.entry_goal_name.get() == "":
                self.error_messages.append(tk.Label(self, text = "Dê um nome para a meta.",
                                              font = ("Arial", 10), fg = "red"))
            if self.clicked_type.get() == "Tipo de meta":
                self.error_messages.append(tk.Label(self, text = "Selecione o tipo da meta.",
                                              font = ("Arial", 10), fg = "red"))
            if self.clicked_time.get() == "Prazo da meta":
                self.error_messages.append(tk.Label(self, text = "Selecione o prazo da meta.",
                                              font = ("Arial", 10), fg = "red"))
            if not self.entry_goal_time.get().isnumeric():
                self.error_messages.append(tk.Label(self, text = "Defina um prazo para a meta.",
                                              font = ("Arial", 10), fg = "red"))
            if self.entry_goal_description.get() == "":
                self.error_messages.append(tk.Label(self, text = "Descreva a meta.",
                                              font = ("Arial", 10), fg = "red"))
            
            y_pos = 350
            for message in self.error_messages:
                message.place(x = 200, y = y_pos, height = 40, width = 400)
                y_pos += 40

            if len(self.error_messages) == 0:
                # falta a função para mandar para o bd
                self.destroy()
                import student_frame_factory as sff
                sff.StudentFrameFactory("ThankYouCard", self.window)

        self.button["command"] = set_goals

        self.label.place(x = 200, y = 20, height = 40, width = 400)

        self.label_goal_name.place(x = 200, y = 100, height = 40, width = 100)
        self.entry_goal_name.place(x = 300, y = 100, height = 40, width = 300)

        self.drop_goal_type.place(x = 300, y = 140, height = 40, width = 300)
        self.label_goal_type.place(x = 200, y = 140, height = 40, width = 100)

        self.label_goal_time.place(x = 200, y = 180, height = 40, width = 100)
        self.entry_goal_time.place(x = 300, y = 180, height = 40, width = 175)
        self.drop_goal_time.place(x = 475, y = 180, height = 40, width = 125)
        
        self.label_goal_description.place(x = 200, y = 220, height = 80, width = 100)
        self.entry_goal_description.place(x = 300, y = 220, height = 80, width = 300)
        
        self.button.place(x = 200, y = 300, height = 40, width = 400)

    def destroy(self) -> None:
        super().destroy()
    
    def update_db(self, goals: dict) -> bool:
        pass
