import sys
import os
sys.path.append(os.path.abspath("./src"))

from db.db_connector import DBConnector
import gui.window as wd
import login.login_frame_factory as lff

class SystemMeta(type):
    """ System Metaclass for Singleton Pattern application. """

    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class System(metaclass = SystemMeta):
    def __init__(self) -> None:
        self.user = None
        self.window = None
        self.database = DBConnector()

    def start(self) -> None:
        """ Starts the system. """
        self.window = wd.Window()
        frame = lff.LoginFrameFactory.get_frame("LoginFrame", self.window)
        self.window.mainloop()
        
if __name__ == "__main__":
    system = System()
    system.start()
