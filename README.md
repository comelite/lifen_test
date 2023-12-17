# Lifen Test

This project is a test for Lifen. It is a command line tool that allows you to retrieve all the first and last names of a document from a list of documents.

## Table of Contents

- [Getting Started](#getting-started)
      - [Prerequisites](#prerequisites)
- [Usage](#usage)
    - [Functionality](#functionality)
        - [Usage](#usage)
        - [Arguments](#arguments)
- [Linting and Type Checking](#linting-and-type-checking)
- [Testing](#testing)
- [Isort and Black](#isort-and-black)
- [Next Steps](#next-steps)

## Getting Started

### Prerequisites

```bash
git clone https://github.com/comelite/lifen_test.git
cd lifen_test
python -m venv .venv
.venv/Scripts/activate
pip install poetry
poetry install
```

## Usage

### Functionality

This project is a test for Lifen. It is a command line tool that allows you to retrieve all the first and last names of a document from a list of documents.
All the results are saved in a json file in the format:
```json
[
   [
      {
         "page_number":1,
         "names":[
            {
               "first_name":"John",
               "last_name":"Doe"
            },
            {
               "first_name":"Jane",
               "last_name":"Doe"
            }
         ]
      },
      {
         "page_number":2,
         "names":[
            {
               "first_name":"Jean",
               "last_name":"Dupont"
            },
            {
               "first_name":"Jacque",
               "last_name":"Marin"
            }
         ]
      }
   ]
]
```
    
#### Usage

```bash
poetry run python lifen_test/__main__.py --path-load <path_to_load> --path-save <path_to_save>
```

#### Arguments

| Argument | Description | Default |
| --- | --- | --- |
| `--path-load` | Path to load the data | `data/save/docs.json` |
| `--path-save` | Path to save the data | `data/save/docs_save.json` |

## Linting and Type Checking

The project uses [pylint](https://www.pylint.org/) for linting and [mypy](http://mypy-lang.org/) for type checking.

```bash
poetry run pylint ./lifen_test
poetry run mypy ./lifen_test
```

## Testing

The project uses [pytest](https://docs.pytest.org/en/latest/) for testing.

```bash
poetry run pytest ./tests/test.py
```

## Isort and Black

The project uses [isort](https://pycqa.github.io/isort/) and [black](https://github.com/psf/black) for formatting.

```bash
poetry run isort ./lifen_test
poetry run black ./lifen_test
```

## Next Steps

One idea is to improve sentence reconstruction. With my method, you can see that certain letters, such as j or g, which exceed the usual y_min, will distort certain retrievals.
This can be done by taking into account, for example, both the average point of a word and its minimum values. Or by using the maximum values in addition.

Another improvement could be to add more words to detect first and last names. Currently only 4 words are used for this purpose, but the list could be expanded.

We could also improve the tests. Currently, only the main functions are tested, but we could also test the functions that are used in the main functions.