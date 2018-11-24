# Take advantage of OOP in modelling a deck of cards. Make it possible to
# shuffle a deck, to deal a single card from the deck and to deal a hand
# of five cards from the deck.

from random import shuffle as official_shuffle


class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        # return f"{self.value} of {self.suit}"
        return "{} of {}".format(self.value, self.suit)


class Deck:

    def __init__(self):
        suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        values = ('A', '2', '3', '4', '5', '6', '7', '8',
                  '9', '10', 'J', 'Q', 'K')
        self.cards = [Card(val, sui) for sui in suits for val in values]

    def count(self):
        return len(self.cards)

    def __repr__(self):
        # return f"Deck of {self.count()} cards"
        return "Deck of {} cards".format(self.count())

    def shuffle(self):
        if self.count() != 52:
            raise ValueError('Only full decks can be shuffled.')
        else:
            official_shuffle(self.cards)
        return self.cards

    def _deal(self, num):
        i = 0
        card_list = []
        while i < num and self.count() > 0:
            card_list.append(self.cards.pop())
            i += 1
        if self.count() == 0 and i < num:
            raise ValueError('All cards have been dealt.')
        return card_list

    def deal_card(self):
        # _deal(1) returns a list of one. pop() returns the Card out from
        # that list.
        return self._deal(1).pop()

    def deal_hand(self, num_of_cards):
        return self._deal(num_of_cards)

    def display_deck(self):
        i = 1
        print()
        print(f'The following {self.count()} cards ', end='')
        print('are remaining in the deck:\n')
        for crd in self.cards:
            if i % 5 == 0:
                print(crd)
            else:
                print(crd, end=', ')
            i += 1
        print('\n')


# Testing
# c1 = Card('A','Hearts')
# print(c1)
d1 = Deck()
print('Display the unshuffled deck:')
d1.display_deck()
d1.shuffle()
print('Display the shuffled deck:')
d1.display_deck()
print('Deal the tailing card of the deck')
print('Dealt: ', d1.deal_card())
d1.display_deck()
# Deal 5 cards from the tail of the deck
print('Dealt a hand: ', d1.deal_hand(5))
d1.display_deck()
print('Deal the last 46 remaining cards from the deck.')
print('\nDealt the following cards:\n', d1.deal_hand(46))
print('\nDisplay the empty deck:')
d1.display_deck()
#print('Try to deal one card from an empty deck.')
# d1.deal_card()

# d1.shuffle() # Shuffling an incomplete deck of cards should raise an error.
