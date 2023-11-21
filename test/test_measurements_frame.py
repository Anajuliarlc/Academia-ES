import unittest
import src.student.measurements_frame as mf

class TestMeasurementsFrame(unittest.TestCase):

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
        self.assertTrue(mf.MeasurementsFrame.update_db(measurements))