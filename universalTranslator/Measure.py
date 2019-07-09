import helpers
class Measure:
    def __init__(self,magnitude,unit, conversionUnit):
        self.magnitude = magnitude
        self.unit = unit
        self.conversionUnit = conversionUnit

    def convert(self):
        currentMeasureValue = helpers.getUnit(self.unit)
        futureMeasureValue = helpers.getUnit(self.conversionUnit)
        self.targetMeasure = helpers.convert(self.magnitude,currentMeasureValue,futureMeasureValue)
