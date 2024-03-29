# Universal_Translator
Console app to convert different length measures from the metric system.


## Installation

Clone this repository using the CLI.

```bash
git clone https://github.com/syned13/Universal_Translator.git
```

## Usage
You should put a .txt file called <b>measures.txt</b> in the proyect root directory

The file should have one conversion information per line, as follows: <br>
magnitude unit targetUnit<br>
anotherMagnitude unit targetUnit<br>

All units should be written following the International Metric System prefix convention. You can find more information here: https://www.nist.gov/pml/weights-and-measures/metric-si-prefixes 
Remember, <b>units of length</b>

Then you simply execute:
```bash
python run.py
```
A "convertedMeasures" file will be generated.

You can find an example on the "measuresExample.txt" file.

## Dependencies
You should have installed python 3.0 or newer.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Diagrams

![Alt text](CRC_Cards.jpg?raw=true "Title")
![Alt text](Class_Diagram.jpg?raw=true "Title")

## License
[MIT](https://choosealicense.com/licenses/mit/)
