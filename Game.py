from Player import Player
from Board import Board
from GUI import drawBoard, Button, TextDraw
import pygame, sys
from pygame.locals import *

#TODO: refactor while loops into eventCheck so that one time stuff per phase (like drawing phase info) is not redone over and over
#figure out how to un-draw text so it doesn't pile up

class Game:
    #Manages the flow of the game and the passage of time
    def __init__(self, cycles=9, playerCount=2, playerTypes=["HUMAN","AI"], boardRadius=5, windowSize=(800, 1000)):
        self.players = []
        for i in range(playerCount):
            self.players.append(Player(playerTypes[i]))
        self.board = Board(boardRadius, self)
        self.calendar = Calendar()
        self.activePlayer = 1
        self.maxCycles = cycles
        self.buttons = []
        pygame.init()
        self.gameSurface = pygame.display.set_mode(windowSize)
        self.view = drawBoard(self.board, windowSize, self.gameSurface)
        self.playGame()
        
    def playGame(self):
        endPhaseButton = Button([600, 200], 150, 50, " End Phase", self.calendar.advancePhase)
        self.buttons.append(endPhaseButton)
        endPhaseButton.draw(self.gameSurface)
        while self.calendar.day <= self.maxCycles*3:
            for player in self.players:
                player.deck.drawSix()
            while self.calendar.phase == "DAY":
                self.drawCalendarInfo()
                self.eventCheck()
            while self.calendar.phase == "DUSK":
                self.drawCalendarInfo()
                self.eventCheck()
            while self.calendar.phase == "NIGHT":
                self.drawCalendarInfo()
                self.eventCheck()
            while self.calendar.phase == "EXCHANGE":
                self.drawCalendarInfo()
                self.eventCheck()
                
    def drawCalendarInfo(self):
        dayDisplay = TextDraw([400, 100], 50, "Day: {}".format(self.calendar.day))
        phaseDisplay = TextDraw([400, 150], 50, "Current Phase: {}".format(self.calendar.phase))
        dayDisplay.draw(self.gameSurface)
        phaseDisplay.draw(self.gameSurface)
           
    def eventCheck(self):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                for button in self.buttons:
                    button.checkButtonClick(event.pos)
            if event.type == QUIT:
                pygame.quit()
                sys.exit() 
        pygame.display.update()
                    
class Calendar:
    #An object that tracks the passage of time in the game
    def __init__(self):
        self.day = 1
        self.phase = "DAY"
        self.sustainPhase = True
        
    def advancePhase(self):
        #Advances the game's phase and counts when this results in the beginning of a new day
        if self.phase == "DAY":
            self.phase = "DUSK"
        elif self.phase == "DUSK":
            self.phase = "NIGHT"
        elif self.phase == "NIGHT":
            self.phase = "EXCHANGE"
        elif self.phase == "EXCHANGE":
            self.phase = "DAY"
            self.day += 1
            
thisGame = Game()