# Translation Script

This script translates the content of a text file multiple times using random languages and finally translates it back to English.

## Requirements

- Python 3
- `deep_translator` library

## Installation

1. Install Python from [python.org](https://www.python.org/).
2. Install the `deep_translator` library using pip:

   ```sh
   pip install deep-translator
   ```

## Usage

1. Place the text you want to translate in a file named `original.txt` in the same directory as the script.
2. Run the script:

   ```sh
   python main.py
   ```
3. Enter the number of times you want to translate the text when prompted.
4. The translated text will be saved in a file named `resault.txt`.

## Example

```sh
Enter the number of times you want to translate: 5
translated 1
translated 2
translated 3
translated 4
translated 5
Done
```

## Notes

- The script uses Google Translate via the `deep_translator` library.
- The list of languages used for translation is predefined in the script.
- The idea is from the youtube chanel Twisted Translations
