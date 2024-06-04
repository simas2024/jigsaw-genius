# Puzzle Solver Console App

## Installation

Installation instructions for a Python virtual environment, tested on the macOS platform using a Python 3.12 installation with brew.

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
     usage: SolvePuzzle [-h] --puzzle <file-path> [--hint <file-path>]

     Solves a puzzles.

     options:
     -h, --help            show this help message and exit
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
    Algorithm Execution Time: 11.22 seconds
    Write Puzzle Image: ./tmp_20240604144411/puzzled_image_a.png
    Write Puzzle Image: ./tmp_20240604144411/puzzled_image_b.png

Deactivate `venv`:

    deactivate

## Contributing
