import pygame, sys, math
from pygame.locals import *

class drawBoard:
    def __init__(self, board, windowSize, gameSurface):
        #Eventually change tile side length to board size and do appropriate math
        #and pull pygame init up into an encapsulating class that also draws hands etc
        self.board = board
        self.radius = board.radius
        self.tileSideLength = min(windowSize)//30
        self.hexMath = hexagonMath()
        self.gameSurface = gameSurface
        boardCenter = [x//2 for x in windowSize]
        for key in self.board.tiles:
            tile = self.board.tiles[key]
            self.drawTile(tile, boardCenter)
            
    def drawTile(self, tile, boardCenter):
        r, q = tile.coords
        center = self.hexMath.calculateCenterFromHexCoords(r, q, self.tileSideLength, boardCenter)
        vertices = self.hexMath.calculateHexgonVertices(center, self.tileSideLength)
        pygame.draw.polygon(self.gameSurface, (255, 255, 255), vertices, 1) #color value is white
        if tile.tree is not None:
            if tile.tree.owningPlayer == 1:
                color = (255,0,0) #red
            else: color = (0,0,255) #blue
            vertices = self.hexMath.calculateHexgonVertices(center, self.tileSideLength*.8)
            pygame.draw.polygon(self.gameSurface, color, vertices, 1)
        if tile.animal is not None:
            if tile.animal.animalType == "squirrel":
                text = 'S'
            elif tile.animal.animalType == "beaver":
                text = 'B'
            elif tile.animal.animalType == "owl":
                text = 'O'
            if tile.animal.owningPlayer == 1:
                color = (255,0,0) #red
            else: color = (0,0,255) #blue
            font = pygame.font.Font('freesansbold.ttf', self.tileSideLength)
            textSurface = font.render(text, True, color)
            rect = textSurface.get_rect()
            rect.center = center
            self.gameSurface.blit(textSurface, rect)
            
class Button:
    def __init__(self, topleft, width, height, text, method):
        self.xrange = (topleft[0], topleft[0]+width)
        self.yrange = (topleft[1], topleft[1]+height)
        self.center = (topleft[0] + width/2, topleft[1] + height/2)
        self.fontSize = min(width//len(text), height)
        self.vertices = (topleft, 
                         (self.xrange[1], self.yrange[0]), 
                         (self.xrange[1], self.yrange[1]), 
                         (self.xrange[0], self.yrange[1]))
        self.text = text
        self.method = method
        
    def draw(self, gameSurface):
        pygame.draw.polygon(gameSurface, (255,255,255), self.vertices, 1)
        font = pygame.font.Font('freesansbold.ttf', self.fontSize)
        textSurface = font.render(self.text, True, (255,255,255))
        rect = textSurface.get_rect()
        rect.center = self.center
        gameSurface.blit(textSurface, rect)
        
    def checkButtonClick(self, clickPosition):
        if self.xrange[0] <= clickPosition[0] <= self.xrange[1] and self.yrange[0] <= clickPosition[1] <= self.yrange[1]:
            self.method()
            
class TextDraw:
    def __init__(self, center, fontSize, text):
        self.center = center
        self.fontSize = fontSize
        self.text = text
        
    def draw(self, gameSurface):
        font = pygame.font.Font('freesansbold.ttf', self.fontSize)
        textSurface = font.render(self.text, True, (255,255,255))
        rect = textSurface.get_rect()
        rect.center = self.center
        gameSurface.blit(textSurface, rect)

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