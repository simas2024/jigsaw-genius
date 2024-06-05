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

## How to use with Docker

To use this application with Docker, follow these instructions:

### Building the Docker Image

To build the Docker image, run the following command in the directory containing the Dockerfile:

    docker build -t puzzle-solver .

This command builds a Docker image named `puzzle-solver`.

### Running the Application in Docker

To run the application using Docker, you can mount the current directory to the `/app` directory in the container. This allows the container to access and write files to your host directory. Use the following command to run the application:

    docker run -it -v .:/app --rm puzzle-solver --help

This command runs the puzzle Docker container, showing the help information as it would when running the application natively. Any command line arguments applicable to `SolvePuzzle.py` can be used after the image name.

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

### Example A with Docker

Run the following command in the directory containing the Dockerfile:

Command:
      
    docker run -it -v .:/app --rm puzzle-solver --puzzle ./images/ExampleA/puzzle_to_solve.png --hint ./images/ExampleA/hint.png
    Solve puzzle
    Algorithm Execution Time: 23.77 seconds
    Write Puzzle Image: /app/tmp_20240605081446/solved_puzzle.png

Command:
      
    docker run -it -v .:/app --rm puzzle-solver --puzzle ./images/ExampleA/puzzle_to_solve.png
    Solve puzzle
    Algorithm Execution Time: 22.85 seconds
    Write Puzzle Image: /app/tmp_20240605081558/solved_puzzle.png

## Benchmark

Command:

    --puzzle ./images/ExampleA/puzzle_to_solve.png --hint ./images/ExampleA/hint.png

| Plattform | Runtime | Time [seconds] |
| --- | --- | --- |
| Mac mini M1 16 GB | Native | 11.39  |
| Mac mini M1 16 GB | Docker | 22.85  |
| Raspberry 5 8 GB | Docker | 47.26 |