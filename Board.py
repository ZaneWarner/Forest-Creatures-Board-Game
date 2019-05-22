class Board:
    "Tracks the hex board and its state"
    def __init__(self, radius):
        self.radius = radius
        self.tiles = {}
        for r in range(-radius, radius+1):
            for q in range(-radius, radius+1):
                if abs(r+q) <= radius:
                    self.tiles[(r,q)] = None
    
    