from Deck import Deck

class Player:
    #Tracks the state of a particular player: deck, piece locations, moves
    #plus the specific squirrel states (eaten and holding nut)
    #And gets their moves
    def __init__(self, playerType):
        if playerType == "HUMAN":
            self.isHuman = 1
        elif playerType == "AI":
            self.isHuman = 0
        else:
            raise ValueError(playerType)
        self.deck = Deck()
        self.trees = 0
        self.animalLocations = {"squirrel" : None, "beaver" : None, "owl" : None}
        self.squirrelMoves = 0
        self.beaverMoves = 0
        self.owlMoves = 0
        self.squirrelEaten = False
        self.squirrelHasNut = False