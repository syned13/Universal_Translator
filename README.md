# Universal_Translator
Console app to convert different distance measures from the metric system.


## Installation

Clone this repository using the CLI.

```bash
git clone https://github.com/syned13/Universal_Translator.git
```

## Usage
You should put a .txt file called <b>measures.txt</b> in the proyect root directory

The file should have one conversion information per line, as follows: <br>
magnitude unit targetUnit<br>
anotherMagnitude unit targetUnit

Then you simply execute:
```bash
python run.py
```
A "convertedMeasures" file will be generated.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
