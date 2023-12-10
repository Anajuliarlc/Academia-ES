import doctest
import unittest
import sys 
import os
sys.path.append(os.path.abspath("./src"))

import exc.exceptions as ex
import login.login_class as lg
import login.login_frame as lf
import gui.buttons as bt
import gui.entrytext as et
import gui.errorlabel as el
import gui.frame as fr
import gui.frame_factory as ff
import gui.logo_frame as lf
import gui.table as tb
import main as mn

suite1 = doctest.DocTestSuite(ex)
suite2 = doctest.DocTestSuite(lg)
suite3 = doctest.DocTestSuite(lf)
suite4 = doctest.DocTestSuite(ff, optionflags=doctest.ELLIPSIS)
suite5 = doctest.DocTestSuite(bt)
suite6 = doctest.DocTestSuite(et)
suite7 = doctest.DocTestSuite(el)
suite8 = doctest.DocTestSuite(fr)
suite9 = doctest.DocTestSuite(tb)
suite10 = doctest.DocTestSuite(mn, optionflags=doctest.ELLIPSIS)

all_suites = unittest.TestSuite([suite1, suite2, suite3, suite4, suite5, suite6,
                                 suite7, suite8, suite9, suite10])

runner = unittest.TextTestRunner(verbosity = 2)
runner.run(all_suites)