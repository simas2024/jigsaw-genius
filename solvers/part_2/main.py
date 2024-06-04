# imports:
import cv2 as cv
import os
from edge_extraction_functions import edge_extraction
from match_and_order import get_classified_pieces, order_pieces
from list_to_image import convert_list_to_image

def solve(image_path, result_path):
    original_img = cv.imread(image_path)
    pieces_borders, pieces_countours, puzzle_pieces, puzzle_pieces_top_left_corner = edge_extraction(image_path)
    # print("done1")
    classified_pieces = get_classified_pieces(pieces_borders)
    # print("done2")
    puzzle_list, width, height, width_px, height_px= order_pieces(classified_pieces, pieces_borders)
    # print("done3")
    final_image = convert_list_to_image(width, height, width_px, height_px, puzzle_list, puzzle_pieces, puzzle_pieces_top_left_corner)
    # print("done4")

    print(f"Write Puzzle Image: {os.path.join(result_path,'puzzled_image_b.png')}")

    os.makedirs(result_path, exist_ok=True)
    cv.imwrite(os.path.join(result_path,'puzzled_image_b.png'),final_image)