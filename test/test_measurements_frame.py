import unittest
import sys
sys.path.append("./src")
import student.measurements_frame as mf
import tkinter as tk

class TestMeasurementsFrame(unittest.TestCase):
    window = tk.Tk()

    def test_update_db_happy_case(self):
        """ Verify if the update_db method is working in the happy case """        
        measurements = {"IdUser": 3,
                        "Weight": 80,
                        "Height": 1.80,	
                        "HighWaist": 65,
                        "LowWaist": 65,
                        "Bust": 90,
                        "Biceps": 30,
                        "Thigh": 50}
        frame = mf.MeasurementsFrame(tk.Tk())
        self.assertTrue(frame.update_db(measurements))


if __name__ == "__main__":
    unittest.main()