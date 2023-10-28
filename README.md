# Amharic PreProcessing Toolkit (APP-TOOLKIT)

The Amharic PreProcessing Toolkit (APP-TOOLKIT) is a collection of Python modules and utilities designed for text processing and preprocessing tasks in Amharic. This toolkit provides functions for stemming, stopwords removal, transliteration, and other text cleaning tasks.

## Project Structure

The project is organized as follows:

- **app_toolkit/**: This directory contains the Python modules for the toolkit.

  - `stemmer.py`: Provides Amharic text stemming capabilities.
  - `stopwords_remover.py`: Removes stopwords from Amharic text.
  - `transliterate.py`: Transliterates Amharic text to other scripts or vice versa.
  - `cleaners/`: This subdirectory contains utility functions for text cleaning, such as duplicate removal.

- **data/**: You can store data files or resources in this directory if needed for text processing.

- **docs/**: This directory can be used for project documentation, but it's currently empty.

- **test/**: You can place your test files or scripts in this directory to test the functionality of the toolkit.

## Usage

To use the APP-TOOLKIT, you can import the required modules and functions into your Python scripts. Below is an example of how to use some of the toolkit's functionalities:

```python
from app_toolkit import stemmer, stopwords_remover, transliterate

# Example usage of stemming:
stemmed_word = stemmer.stem("አጭርኛ")
print(stemmed_word)  # Output: "አጭር"

# Example usage of stopwords removal:
text = "አጭርኛ ሰው ስቃይ ውጭ ማለት ይሄ ነው"
cleaned_text = stopwords_remover.remove_stopwords(text)
print(cleaned_text)  # Output: "ጭኛ ሰው ስቃይ ውጭ ማለት ነው"

# Example usage of transliteration:
transliterated_text = transliterate.felig_transliterate("አጭርኛ", "am")
print(transliterated_text)  # Output: "axarena"
```
