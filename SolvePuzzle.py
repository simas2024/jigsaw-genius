#!/usr/bin/env python
# coding: utf-8
# SolvePuzzle.py

''' solve puzzle '''

__version__ = '1.0.2'

import sys
if sys.version_info < (3, 12):
    sys.exit("This script requires Python 3.12 or higher. Please upgrade your Python version.")
import os
import argparse
import datetime

solversdir=os.path.join(os.path.dirname(os.path.abspath(__file__)),"solvers")

sys.path.append(os.path.join(solversdir,"part_2_merged"))
from part_2_merged_solve import solve as solveWithHint
sys.path.append(os.path.join(solversdir,"part_2"))
from main import solve as solve

parser = argparse.ArgumentParser(prog='SolvePuzzle', description='Solves a puzzles.',
                                 epilog='Example: SolvePuzzle.py --puzzle ./images/ExampleA/puzzle_to_solve.png --hint ./images/ExampleA/hint.png')

parser.add_argument('-v', '--version', action='version', version=f"SolvePuzzle v{__version__}")

parser.add_argument('--puzzle', type=str, required=True, default=None, help='puzzle file', metavar=('<file-path>'))

parser.add_argument('--hint', type=str, required=False, default=None, help='hint puzzle file', metavar=('<file-path>'))

args = parser.parse_args()

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
subdirectory = "tmp_" + timestamp
current_directory = os.path.dirname(os.path.abspath(__file__ or '.'))
target_directory = os.path.join(current_directory, subdirectory)

print("Solve puzzle")
if not(args.hint is None):
  solveWithHint(args.puzzle,args.hint,target_directory)
else:
  solve(args.puzzle,target_directory)