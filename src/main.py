from db.db_connector import DBConnector
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
    """ 
    System class for Singleton Pattern application. 

    >>> system1 = System()
    >>> system2 = System()
    >>> system1 is system2
    True

    >>> system1.database
    <db.db_connector.DBConnector object at ...>
    """
    
    def __init__(self) -> None:
        self.user = None
        self.window = None
        self.database = DBConnector()

    def start(self) -> None:
        """ Starts the system. """
        ... #TODO: Implement the window start
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
