from Player import Player
from Board import Board

class Game:
    #Manages the flow of the game and the passage of time
    def __init__(self, cycles=9, player1AI=False, player2AI=True, boardRadius=5):
        self.player1 = Player(player1AI)
        self.player2 = Player(player2AI)
        self.board = Board(boardRadius, self)
        self.turn = 0
        self.activePlayer = 1
        self.maxCycles = cycles
        
    def playGame(self):
        while self.turn < self.maxCycles*3:
            if self.activePlayer == 1:
                endPhase = False
                while not endPhase:
                    pass
                    #for now, autoplay cards on all of these
                    #highlight p1 squirrel
                    #take squirrel moves with mouse
                    #have grab nut/drop nut, end phase buttons
                    #IF AI, instead do AI stuff
                while not endPhase:
                    pass
                    #highlight p1 beaver
                    #take beaver moves with mouse
                    #have eat tree, end phase buttons
                    #IF AI, instead do AI stuff
                while not endPhase:
                    pass
                    #highlight p1 owl
                    #take owl moves with mouse
                    #have end phase button
                #DO some exchange thing