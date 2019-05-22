import numpy as np

class Deck:
    #tracks the cards in each zone for a player: hand, deck, and discard
    #each zone has an 8 element array, with elements corresponding to the number of squirrels, beavers, owls, 
    #   their upgraded forms, wild cards, and total card count, respectively
    def __init__(self):
        self.deck = [5]*3 + [0]*4 + [15]
        self.hand = [0]*8
        self.discard = [0]*8
        
    def drawFive(self):
        #draws five random cards from deck to hand. Assumes deck contains at least 5 cards (a truth the game rules maintain)
        deckExpanded = []
        for i in range(7):
            deckExpanded += [i]*self.deck[i]
        drawn = np.random.choice(deckExpanded, 5, replace=False)
        for card in drawn:
            self.deck[card] -= 1
            self.deck[7] -= 1 #recall that idx 7 tracks the total card count in that zone
            self.hand[card] += 1
            self.hand[7] += 1
            
    def discardAll(self):
        #discards the entire hand
        for cardIdx in range(7):
            self.discard[cardIdx] += self.hand[cardIdx]
            self.discard[7] += self.hand[cardIdx] #recall that idx 7 tracks the total card count in that zone 
        self.hand = [0]*8
        
    def reshuffle(self):
        #recombines the discard into the deck
        for cardIdx in range(7):
            self.deck[cardIdx] += self.discard[cardIdx]
            self.deck[7] += self.discard[cardIdx] #recall that idx 7 tracks the total card count in that zone 
        self.discard = [0]*8
        
    def exchange(self, remove, add):
        #Removes a card with idx remove, adds one with idx add in its place
        self.deck[remove] -= 1
        self.deck[add] += 1