#!/usr/bin/env python
# coding: utf-8
# SolvePuzzle.py

''' solve puzzle '''

__version__ = '1.0.1'

import sys
import os
import argparse
import datetime
from PIL import Image
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(parent_dir,"jigsaw-genius","solvers","part_2_merged"))
from part_2_merged_solve import solve as solvea
sys.path.append(os.path.join(parent_dir,"jigsaw-genius","solvers","part_2"))
from main import solve as solveb
   
parser = argparse.ArgumentParser(prog='SolvePuzzle', description='Solves a puzzles.',
                                 epilog='Example: SolvePuzzle.py --puzzle ./images/ExampleA/puzzle_to_solve.png --hint ./images/ExampleA/hint.png')

parser.add_argument('--puzzle', type=str, required=True, default=None, help='puzzle file', metavar=('<file-path>'))

parser.add_argument('--hint', type=str, required=False, default=None, help='hint puzzle file', metavar=('<file-path>'))

args = parser.parse_args()

input_image = Image.open(args.puzzle)
if not(input_image is None):
  input_image.close()

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
subdirectory = "tmp_" + timestamp
current_directory = os.path.dirname(os.path.abspath(__file__ or '.'))
target_directory = os.path.join(current_directory, subdirectory)

print("Solve puzzle")
solvea(args.puzzle,args.hint,target_directory)
solveb(args.puzzle,target_directory)