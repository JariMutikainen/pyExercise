# Take advantage of OOP in modelling a deck of cards. Make it possible to
# shuffle a deck, to deal a single card from the deck and to deal a hand
# of five cards from the deck.

class Card:
    
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"
        # return "{} of {}".format(self.value,self.suit)"

# Testing
c1 = Card('A','Hearts')
print(c1)
