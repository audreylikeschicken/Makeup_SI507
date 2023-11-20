import cv2 
import numpy as np
import math
from makeupLib import *


def draw_rects(img, rects, color,thickness = 2):
    '''
    Draws the rectangles defined by rects on img
    param img: image to draw rectangles on
    param rects: list of rectangles to draw, format [(x1, y1, x2, y2), ...]
    param color: color to draw the rectangles, (R, G, B) coordinate.
    '''
    for x1, y1, x2, y2 in rects:
        # Drawing your face
        cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness)

def draw_hexagon(img, hexs, color, thickness = 1):
    '''
    Connects the points defined by hexs on img
    param img: image to draw rectangles on
    param rects: list of rectangles to draw, format [(x1, y1, x2, y2), ...]
    param color: color to draw the rectangles, (R, G, B) coordinate.
    '''
    for pt_x1, pt_y1, pt_x2, pt_y2, pt_x3, pt_y3  in hexs:
        delta = 5
        # pt_x1 = pt_x4
        # pt_x2 = pt_x5
        # pt_x3 = pt_x6
        # pt_y4 = pt_y1 + delta
        # pt_y5 = pt_y2 + delta
        # pt_y6 = pt_y3 + delta
        cv2.line(img,(pt_x1, pt_y1),(pt_x2, pt_y2), color,thickness)
        cv2.line(img,(pt_x2, pt_y2),(pt_x3, pt_y3), color,thickness)
        cv2.line(img,(pt_x3, pt_y3),(pt_x3, pt_y3 + delta), color,thickness)
        cv2.line(img,(pt_x3, pt_y3 + delta),(pt_x2, pt_y2 + delta), color,thickness)
        cv2.line(img,(pt_x2, pt_y2 + delta),(pt_x1, pt_y1 + delta), color,thickness)
        cv2.line(img,(pt_x1, pt_y1 + delta),(pt_x1, pt_y1), color,thickness)

def fill_hexagon(img,hexs,color,thickness = 1):
    '''
    Fills in the convex polygon points defined by hexs on img
    param img: image to draw rectangles on
    param rects: list of rectangles to draw, format [(x1, y1, x2, y2), ...]
    param color: color to draw the rectangles, (R, G, B) coordinate.
    '''
    for pt_x1, pt_y1, pt_x2, pt_y2, pt_x3, pt_y3  in hexs:
        delta = 5
        points = np.array([[pt_x1, pt_y1],[pt_x2, pt_y2],[pt_x3, pt_y3],[pt_x3, pt_y3 + delta], \
            [pt_x2, pt_y2 + delta],[pt_x1, pt_y1 + delta]], dtype = np.int32)
            # np.int32 is an array type and specific conversion to an integer
        print(color)
        print(points)
        cv2.fillConvexPoly(img, points, color)

# CITATION: used for drawing rects, ellipses and making lines
# used and altered from https://docs.opencv.org/3.4/dc/da5/tutorial_py_drawing_functions.html
# cv2.line(img, p1, p2, (255, 0, 0), 3)

def draw_triangle(img,triangle,color,thickness = 2):
    '''
    Creates 3 coordinates defined by rects on img
    param img: image to draw rectangles on
    param rects: list of rectangles to draw, format [(x1, y1, x2, y2), ...]
    param color: color to draw the rectangles, (R, G, B) coordinate.
    '''
    for pt_x1, pt_y1, pt_x2, pt_y2, pt_x3, pt_y3, in triangle:
        cv2.line(img,(pt_x1, pt_y1),(pt_x2, pt_y2), color,thickness)
        cv2.line(img,(pt_x2, pt_y2),(pt_x3, pt_y3), color,thickness)
        cv2.line(img,(pt_x3, pt_y3),(pt_x1, pt_y1), color,thickness)

def fill_triangle(img,triangle,color,thickness = 1):
    '''
    Fills in the convex polygon with 3 coordinates defined by triangles on img
    param img: image to draw rectangles on
    param rects: list of rectangles to draw, format [(x1, y1, x2, y2), ...]
    param color: color to draw the rectangles, (R, G, B) coordinate.
    '''
    for pt_x1, pt_y1, pt_x2, pt_y2, pt_x3, pt_y3, in triangle:
        points = np.array([[pt_x1, pt_y1],[pt_x2, pt_y2],[pt_x3, pt_y3]], dtype = np.int32)
        print(color)
        print(points)
        cv2.fillConvexPoly(img, points, color)

def draw_ellipses(img, ellipses, color,thickness):
    '''
    Draws the rectangles defined by rects on img
    param img: image to draw rectangles on
    param rects: list of rectangles to draw, format [(x1, y1, x2, y2), ...]
    param color: color to draw the rectangles, (R, G, B) coordinate.
    '''
    for center_x1, center_y1, axes_x1, axes_y1 in ellipses:
        # Drawing your face
        cv2.ellipse(img,(center_x1,center_y1),(axes_x1,axes_y1), \
        0,0,360,color,thickness)

def get_eye(rects):
    eye_rects = [ ]

    for x1, y1, x2, y2 in rects:
        delta_1 = 15
        delta_2 = -43
        eye_x1 = int(0.3*x1) + int(0.7*x2) + delta_1
        eye_y1 = int(0.4*y1) + int(0.6*y2) + delta_2
        eye_x2 = int(0.4*x1) + int(0.6*x2) + delta_1
        eye_y2 = int(0.45*y1) + int(0.55*y2) + delta_2
        eye_x3 = int(0.5*x1) + int(0.5*x2) + delta_1
        eye_y3 = int(0.4*y1) + int(0.6*y2) + delta_2
        # eye_x4 = eye_x1 + delta
        # eye_y4 = eye_y1 + delta
        # eye_x5 = eye_x2 + delta
        # eye_y5 = eye_y2 + delta
        # eye_x6 = eye_x3 + delta
        # eye_y6 = eye_y3 + delta
        midpoint = int((x1 + x2)/2)
        distance_1 = midpoint - eye_x1
        distance_2 = midpoint - eye_x2
        distance_3 = midpoint - eye_x3
        reflect_x1 = 2*(distance_1) + (eye_x1)
        reflect_x2 = 2*(distance_2) + (eye_x2)
        reflect_x3 = 2*(distance_3) + (eye_x3)
        eye_rects.append((eye_x1,eye_y1,eye_x2,eye_y2,eye_x3,eye_y3))
        eye_rects.append((reflect_x1,eye_y1,reflect_x2,eye_y2,reflect_x3,eye_y3))
    return eye_rects

def find_cheeks (rects):
    '''
    Converts the rectangles in rects to cheek rectangles

    param rects: list of face rectangles to find the cheeks in,
    format [(x1, y1, x2, y2), ...]

    return: A list of the cheek coordinates, format [(x1, y1, x2, y2), ...]
    '''
    cheek_rects = []

    for x1, y1, x2, y2 in rects:

    # Draw a box around your cheeks
        # Figure out where cheek coordinates are
        cheek_x1 = int(0.8*x1) + int(0.4*x2) - 95
        cheek_y1 = int((y1 + y2) / 2) - 10
        # Draw a box around your cheeks
        # Figure out where cheek coordinates are
        cheek_x2 = int(0.8*x1) + int(0.4*x2) - 15
        cheek_y2 = int((y1 + y2) / 2) - 10

        cheek_rects.append((cheek_x1, cheek_y1, cheek_x1 + 35, cheek_y1 + 35))
        cheek_rects.append((cheek_x2, cheek_y2, cheek_x2 + 35, cheek_y2 + 35))

    return cheek_rects
