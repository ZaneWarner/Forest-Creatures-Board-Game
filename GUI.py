import pygame
import math
from pygame.locals import *

class drawBoard:
    def __init__(self, board, size):
        self.board = board
    

class hexagonMath:
    def __init__(self):
        pass
        
    def calculateHexgonVertices(self, hexCenter, sideLength):
        #calculates x,y coordinates of a hexgon's vertices given its center and size
        #hexagons in this game are pointy-topped
        vertices = []
        for angle in [30, 90, 150, 210, 270, 330]:
            angle = math.radians(angle)
            x, y = math.cos(angle)*sideLength + hexCenter, math.sin(angle)*sideLength + hexCenter
            vertices.append((x,y))
        return vertices
    
    def calculateCenterFromHexCoords(self, r, q, sideLength):
        x, y = q*sideLength + math.cos(math.radians(60))*r*sideLength,  -math.sin(math.radians(60))*r*sideLength
        return (x,y)
        
