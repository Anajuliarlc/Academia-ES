import sys
import os
sys.path.append(os.path.abspath("./src"))

from db.db_connector import DBConnector
import gui.window as wd
import login.login_frame_factory as lff
from typing import Any, Dict, Type, TypeVar

T = TypeVar('T', bound='SystemMeta')

class SystemMeta(type):
    """ System Metaclass for Singleton Pattern application. 
    
    >>> class Test(metaclass=SystemMeta): pass
    >>> a = Test()
    >>> b = Test()
    >>> a is b
    True
    """

    _instances: Dict[Type[T], T] = {}
    
    def __call__(cls: Type[T], *args: Any, **kwargs: Any) -> T:
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class System(metaclass = SystemMeta):
    """ Core application class. Carry out the system's database access and 
    GUI main window management.

    >>> system1 = System()
    >>> system2 = System()
    >>> system1 is system2
    True

    >>> system1.database
    <db.db_connector.DBConnector object at ...>
    """
    
    def __init__(self) -> None:
        """Initialize a new System object. 
        Automatically connects to the database.
        """
        self.user = None
        self.window = None
        self.database = DBConnector()

    def start(self) -> None:
        """ Boot the system. Create a new window and a login screen."""
        self.window = wd.Window()
        frame = lff.LoginFrameFactory.get_frame("LoginFrame", self.window)
        self.window.mainloop()
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
