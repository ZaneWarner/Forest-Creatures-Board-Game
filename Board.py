
P1_TREE = "p1tree"
P2_TREE = "p2tree"
P1_FRUITED_TREE = "p1fruitedtree"
P2_FRUITED_TREE = "p2fruitedtree"

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
        for coord in [(2,0),(-2,2),(0,-2)]:
            self.tiles[coord] = P1_TREE
            game.player1.trees += 1
        for coord in [(0,2),(-2,0),(2,-2)]:
            self.tiles[coord] = P2_TREE
            game.player2.trees += 1
    
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
                
    
        
    
    