import unittest

import sys 
import os
sys.path.append(os.path.abspath("./src")) # Adds src directory to python modules path.

from teacher.register import Register
import exc.exceptions as exc


class TestRegister(unittest.TestCase):
    pass