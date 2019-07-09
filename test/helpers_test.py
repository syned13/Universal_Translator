import unittest
import sys
sys.path.append("../universalTranslator")
import helpers

class TestHelpersGetUnit(unittest.TestCase):

    def test_km_1000(self):
        self.assertEqual(1000,helpers.getUnit("km"))
    def test_cm(self):
        self.assertEqual(0.01,helpers.getUnit("cm"))
    def test_mm(self):
        self.assertEqual(0.001,helpers.getUnit("mm"))

class TestHelpersConvert(unittest.TestCase):

    def test_100cmAm(self):
        self.assertEqual(1, helpers.convert(100,0.01,1))
    def test_200cmAkm(self):
        self.assertEqual(0.002,helpers.convert(200,0.01,1000))
    def test_15mAkm(self):
        self.assertEqual(0.015,helpers.convert(15,1,1000))
    def test_23kmAcm(self):
        self.assertEqual(2300000,helpers.convert(23,1000,0.01))



if __name__ == '__main__':
    unittest.main()
