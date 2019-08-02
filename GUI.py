import pygame, sys, math
import Board
import Game
from pygame.locals import *

class drawBoard:
    def __init__(self, board, windowSize):
        #Eventually change tile side length to board size and do appropriate math
        #and pull pygame init up into an encapsulating class that also draws hands etc
        pygame.init()
        self.board = board
        self.radius = board.radius
        self.tileSideLength = min(windowSize)//30
        self.hexMath = hexagonMath()
        self.gameSurface = pygame.display.set_mode(windowSize)
        boardCenter = [x//2 for x in windowSize]
        for key in self.board.tiles:
            tile = self.board.tiles[key]
            self.drawTile(tile, boardCenter) #hardcoded half of arbitrary board size... clean up later
        while True: #refactor into main game loop eventually
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit() 
            pygame.display.update()
            
    def drawTile(self, tile, boardCenter):
        r, q = tile.coords
        center = self.hexMath.calculateCenterFromHexCoords(r, q, self.tileSideLength, boardCenter)
        vertices = self.hexMath.calculateHexgonVertices(center, self.tileSideLength)
        pygame.draw.polygon(self.gameSurface, (255, 255, 255), vertices, 1) #middle value is an arbitrary color
        

class hexagonMath:
    def __init__(self):
        pass
        
    def calculateHexgonVertices(self, hexCenter, sideLength):
        #calculates x,y coordinates of a hexgon's vertices given its center and size
        #hexagons in this game are pointy-topped
        vertices = []
        for angle in [30, 90, 150, 210, 270, 330]:
            angle = math.radians(angle)
            x, y = math.cos(angle)*sideLength + hexCenter[0], math.sin(angle)*sideLength + hexCenter[1]
            vertices.append((x,y))
        return vertices
    
    def calculateCenterFromHexCoords(self, r, q, sideLength, boardCenter):
        x, y = q*2*sideLength + math.cos(math.radians(60))*r*2*sideLength + boardCenter[0],  -math.sin(math.radians(60))*r*2*sideLength + boardCenter[1]
        return (x,y)
        
thisGame = Game.Game()
drawer = drawBoard(thisGame.board, (800, 1000))