from Player import Player
from Board import Board

class Game:
    #Manages the flow of the game and the passage of time
    def __init__(self, cycles=9, playerCount=2, playerTypes=["HUMAN","AI"], boardRadius=5):
        self.players = []
        for i in range(playerCount):
            self.players.append(Player(playerTypes[i]))
        self.board = Board(boardRadius, self)
        self.calendar = Calendar()
        self.activePlayer = 1
        self.maxCycles = cycles
        
    def playGame(self):
        while self.calendar.day <= self.maxCycles*3:
            for player in self.players:
                player.deck.drawSix()
            while self.calendar.phase == "DAY":
                pass
                    #for now, autoplay cards on all of these
                    #highlight p1 squirrel
                    #take squirrel moves with mouse
                    #have grab nut/drop nut, end phase buttons
                    #IF AI, instead do AI stuff
            self.calendar.advancePhase()
            while self.calendar.phase == "DUSK":
                pass
                    #highlight p1 beaver
                    #take beaver moves with mouse
                    #have eat tree, end phase buttons
                    #IF AI, instead do AI stuff
            self.calendar.advancePhase()
            while self.calendar.phase == "NIGHT":
                pass
                    #highlight p1 owl
                    #take owl moves with mouse
                    #have end phase button
            self.calendar.advancePhase()
            while self.calendar.phase == "EXCHANGE":
                pass
                    #let player optionally exchange a card from hand
            self.calendar.advancePhase()
                    
class Calendar:
    #An object that tracks the passage of time in the game
    def __init__(self):
        self.day = 1
        self.phase = "DAY"
        
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