# Puzzle Solver Console App

## Installation

Installation instructions for a Python virtual environment, tested on the macOS AS platform using a Python 3.12 installation with brew.

    /opt/homebrew/bin/python3 --version
    Python 3.12.3

    /opt/homebrew/bin/python3 -m venv venv

    source venv/bin/activate

    pip3 install -r requirements.txt

## How to Use

Activate `venv`:

    source venv/bin/activate

Command:

    python SolvePuzzle.py --help
    usage: SolvePuzzle [-h] [-v] --puzzle <file-path> [--hint <file-path>]
    
    Solves a puzzles.
    
    options:
      -h, --help            show this help message and exit
      -v, --version         show program's version number and exit
      --puzzle <file-path>  puzzle file
      --hint <file-path>    hint puzzle file

Deactivate `venv`:

     deactivate

## Examples

### Example A

Activate `venv`:

    source venv/bin/activate

Command:
      
    python SolvePuzzle.py --puzzle ./images/ExampleA/puzzle_to_solve.png --hint ./images/ExampleA/hint.png
    Solve puzzle
    Algorithm Execution Time: 11.39 seconds
    Write Puzzle Image: ./tmp_20240605061134/solved_puzzle.png

Command:
      
    python SolvePuzzle.py --puzzle ./images/ExampleA/puzzle_to_solve.png
    Solve puzzle
    Algorithm Execution Time: 10.96 seconds
    Write Puzzle Image: ./tmp_20240605061109/solved_puzzle.png

Deactivate `venv`:

    deactivate

## Contributing
