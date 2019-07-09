import unittest
import sys
sys.path.append("../universalTranslator")
import Measure

class TestMeasureConvert(unittest.TestCase):

    def test_100kmAm(self):
        measure = Measure.Measure(100,"km","m")
        measure.convert()
        self.assertEqual(100000, measure.targetMeasure)

    def test_100mAKm(self):
        measure = Measure.Measure(100,"m","km")
        measure.convert()
        self.assertEqual(0.1, measure.targetMeasure)

    def test_10mAcm(self):
        measure = Measure.Measure(10,"m","cm")
        measure.convert()
        self.assertEqual(1000, measure.targetMeasure)

    def test_17mAmm(self):
        measure = Measure.Measure(17,"m","mm")
        measure.convert()
        self.assertEqual(17000, measure.targetMeasure)

if __name__ == '__main__':
    unittest.main()
