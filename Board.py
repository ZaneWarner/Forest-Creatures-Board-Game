class Board:
    #Tracks the hex board and its state
    #Hex tiles are indexed using an axial coordinate scheme
    def __init__(self, radius, game):
        assert(radius >= 2, "board must have a radius of at least 2")
        self.radius = radius
        self.game = game
        self.tiles = {}
        for r in range(-radius, radius+1):
            for q in range(-radius, radius+1):
                if abs(r+q) <= radius:
                    self.tiles[(r,q)] = None
        treeForPlayer = 0
        for coord in [(2,0),(0,2),(-2,2),(-2,0),(0,-2),(2,-2)]:
            #This assigns the starting trees to players in a fair fashion only for 1, 2, or 3 players // currently only 1 and 2 player games are within the scope of the game rules
            self.addTree(coord, treeForPlayer)
            treeForPlayer = (treeForPlayer+1)%len(self.game.players)
        
    def neighbors(self, r, q):
        #Returns a list of the neighboring hexes to the hex with given r, q
        neighbors = []
        for offset in [(1,0), (0,1),(-1,1),(-1,0),(0,-1),(1,-1)]:
            neighbors.append((r+offset[0],q+offset[1]))
        return neighbors
    
    def distance(self, source, destination):
        #Determines the distance from the source to the destination
        return (abs(source[0] - destination[0])
                + abs(source[0] + source[1] - destination[0] - destination[1])
                + abs(source[1] - destination[1])) / 2
                
    def addTree(self, coord, player):
        #Adds a tree to the board and updates player tree counts
        self.tiles[coord] = Tree(player)
        self.game.players[player].trees += 1
            
class Tree:
    #Represents the trees that can be put on the board
    def __init__(self, owningPlayer):
        self.owningPlayer = owningPlayer
        self.fruited = False
    