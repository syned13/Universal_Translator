from pathlib import Path
import Measure
import os
def main():
    dirPath = os.getcwd()
    fileName = "measures.txt"
    filePath = os.path.join(dirPath,fileName)


    lines = open(filePath,'r').read().splitlines()

    newMeasures = []
    measures = []

    for line in lines:
        splittedLine = line.split(" ")
        magnitude = 0
        unit = ""
        conversionUnit = ""
        try:
            magnitude = float(splittedLine[0])
            unit = splittedLine[1]
            conversionUnit = splittedLine[2]
        except ValueError:
            print("Archivo en formato incorrecto!")
            return
        except IndexError:
            print("Archivo en formato incorrecto!")
            return
        measure = Measure.Measure(magnitude,unit,conversionUnit)
        measure.convert()
        measures.append(measure)

    outputFile = open("convertedMeasures.txt", "w")

    for measure in measures:
        outputLine = "{} {} a {} -> {}\n".format(measure.magnitude, measure.unit, measure.conversionUnit, measure.targetMeasure)
        outputFile.write(outputLine)
    outputFile.close()
