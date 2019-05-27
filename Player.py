from Deck import Deck

class Player:
    #Tracks the state of a particular player: deck, piece locations, moves
    #plus the specific squirrel states (eaten and holding nut)
    #And gets their moves
    def __init__(self, playerType):
        self.AI = playerType #True for AI, else False
        self.trees = 0
        self.deck = Deck()
        self.squirrelLocation = None
        self.beaverLocation = None
        self.owlLocation = None
        self.squirrelMoves = 0
        self.beaverMoves = 0
        self.owlMoves = 0
        self.eaten = False
        self.hasNut = False
        
    def moveSquirrel(self, destination):
        #Needs the board to compute shortest path
        #handle commands to plant nuts--can autograb nut when routing through a tree, though make sure shortest path routes intelligently between equivalent paths if so
        pass
    
    def moveBeaver(self, destination):
        #Needs the board to compute shortest path
        #handle commands to eat trees
        pass
    
    def moveOwl(self, destination):
        #Must build graph of tree paths or leave that to the player. Convenient can BFS from owl location
        pass
    
    def chooseReplacement(self):
        #Route deck replacements though this
        pass